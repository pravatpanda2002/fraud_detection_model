# Fraud Detection — MLOps Project


A complete fraud detection ML project with Streamlit frontend.

## Quick Start
```bash
pip install -r requirements.txt
cd src && python generate_data.py
python train.py
cd .. && streamlit run src/app.py
```

## Project Structure
```
fraud-detection/
├── src/
│   ├── generate_data.py
│   ├── preprocess.py
│   ├── train.py
│   ├── predict.py
│   └── app.py              ← Streamlit frontend
├── tests/
│   └── test_model.py
├── requirements.txt
└── README.md
```
