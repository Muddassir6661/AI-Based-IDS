import argparse
import pandas as pd
import numpy as np
import pickle
import os
import warnings
from sklearn.exceptions import InconsistentVersionWarning
warnings.filterwarnings("ignore", category=InconsistentVersionWarning)
from datetime import datetime
from collections import Counter

# Color codes
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RESET = "\033[0m"

def load_model(model_path, scaler_path):
    with open(model_path, "rb") as f:
        model = pickle.load(f)
    with open(scaler_path, "rb") as f:
        scaler = pickle.load(f)
    return model, scaler

def preprocess(df, scaler):
    df.columns = df.columns.str.strip()
    if "Label" in df.columns:
        df = df.drop(columns=["Label"])
    df.replace([np.inf, -np.inf], np.nan, inplace=True)
    df.dropna(inplace=True)
    scaled = scaler.transform(df)
    return scaled, df.index

def predict(model, data):
    predictions = model.predict(data)
    labels = {0: "BENIGN", 1: "DDoS Detected", 2: "PortScan Detected"}
    return [labels[p] for p in predictions]

def main():
    parser = argparse.ArgumentParser(description="AI-Based Intrusion Detection System")
    parser.add_argument("--file", type=str, required=True, help="Path to input CSV file")
    parser.add_argument("--model", type=str, default="ids_model.pkl", help="Path to trained model")
    parser.add_argument("--scaler", type=str, default="scaler.pkl", help="Path to scaler")
    parser.add_argument("--output", type=str, default=None, help="Path to save results CSV")
    args = parser.parse_args()

    if not os.path.exists(args.file):
        print(f"{RED}Error: File '{args.file}' not found.{RESET}")
        return
    if not os.path.exists(args.model):
        print(f"{RED}Error: Model '{args.model}' not found.{RESET}")
        return

    print(f"\n{YELLOW}Loading model...{RESET}")
    model, scaler = load_model(args.model, args.scaler)

    print(f"{YELLOW}Reading traffic data...{RESET}")
    df = pd.read_csv(args.file)

    print(f"{YELLOW}Preprocessing data...{RESET}")
    data, index = preprocess(df, scaler)

    print(f"{YELLOW}Analyzing traffic...{RESET}\n")
    results = predict(model, data)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    output_rows = []

    for i, result in enumerate(results):
        ts = datetime.now().strftime("%H:%M:%S")
        if result == "BENIGN":
            print(f"{GREEN}[{ts}] Flow {i+1}: {result}{RESET}")
        else:
            print(f"{RED}[{ts}] Flow {i+1}: {result}{RESET}")
        output_rows.append({"Flow": i+1, "Timestamp": ts, "Result": result})

    summary = Counter(results)
    print(f"\n{YELLOW}--- Summary ({timestamp}) ---{RESET}")
    for label, count in summary.items():
        if label == "BENIGN":
            print(f"{GREEN}{label}: {count} flows{RESET}")
        else:
            print(f"{RED}{label}: {count} flows{RESET}")

    if args.output:
        output_df = pd.DataFrame(output_rows)
        output_df.to_csv(args.output, index=False)
        print(f"\n{YELLOW}Results saved to: {args.output}{RESET}")

if __name__ == "__main__":
    main()