# AI-Based Intrusion Detection System

A machine learning-based Intrusion Detection System (IDS) that classifies network traffic as benign or malicious using the CICIDS2017 dataset.

---

## Features
- Detects DDoS and Port Scan attacks from network traffic data
- Trained on CICIDS2017 dataset with 1,041,288 network flows
- Achieves 99.99% classification accuracy using Random Forest
- Color coded CLI output with timestamps
- Save results to CSV with --output flag

---

## Tech Stack
| Component | Tool |
|---|---|
| Dataset | CICIDS2017 |
| Data Processing | pandas, numpy |
| Machine Learning | scikit-learn |
| Model Storage | pickle |
| CLI Interface | argparse |
| Notebook | Google Colab |

---

## Project Structure
```
AI-Based-IDS/
├── ids.py              # CLI tool
├── ids_model.pkl       # Trained Random Forest model
├── scaler.pkl          # StandardScaler
├── test_sample.csv     # Sample test data
└── IDS_Notebook.ipynb  # Full ML pipeline notebook
```

---

## Installation
```bash
pip install scikit-learn pandas numpy
```

---

## Usage
```bash
# Basic usage
python ids.py --file traffic.csv

# Save results to file
python ids.py --file traffic.csv --output results/results.csv

# Custom model path
python ids.py --file traffic.csv --model ids_model.pkl --scaler scaler.pkl
```

---

## Sample Output
```
Loading model...
Reading traffic data...
Preprocessing data...
Analyzing traffic...

[19:47:14] Flow 1: BENIGN
[19:47:14] Flow 9: DDoS Detected
[19:47:14] Flow 10: PortScan Detected

--- Summary ---
BENIGN: 729 flows
DDoS Detected: 121 flows
PortScan Detected: 150 flows
```

---

## Model Performance

| Model | Accuracy | DDoS F1 | PortScan F1 |
|---|---|---|---|
| Random Forest | 100% | 1.00 | 1.00 |
| Decision Tree | 100% | 1.00 | 1.00 |
| Logistic Regression | 100% | 0.99 | 0.99 |
| SVM (LinearSVC) | 100% | 0.99 | 0.99 |

---

## Dataset
CICIDS2017 — Canadian Institute for Cybersecurity
- Monday: Benign traffic
- Friday Afternoon: DDoS attacks
- Friday Afternoon: Port Scan attacks

---

## Future Scope
- Live network traffic monitoring
- Real-time alert system
- Web dashboard for visualization
- Deep learning models for improved accuracy
- IP blocking via firewall integration
- Support for all CICIDS2017 attack categories

---

## Author
Developed as a college mini project.
```

Then scroll down, add commit message:
```
Add detailed README
