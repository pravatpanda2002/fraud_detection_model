# Fraud Detection Project — Complete Execution & GitHub Guide

**Author: Suresh D R | AI Product Developer & Technology Mentor**
*MLOps Syllabus — Deploy and Retrain ML Models on AWS*

---

## What You Will Do

```
Step 1  → Set up project folder
Step 2  → Install libraries
Step 3  → Generate data
Step 4  → Train the model
Step 5  → Run predictions from terminal
Step 6  → Run tests
Step 7  → Launch Streamlit app (frontend)
Step 8  → Push everything to GitHub
Step 9  → Create a feature branch and improve
Step 10 → Open Pull Request and merge
Step 11 → Tag as v1.0.0
```

---

## Project Files You Need

```
fraud-detection/
├── src/
│   ├── generate_data.py   ← creates 1000 sample transactions
│   ├── preprocess.py      ← cleans data and creates features
│   ├── train.py           ← trains Random Forest and saves model
│   └── predict.py         ← loads model and makes predictions
├── tests/
│   └── test_model.py      ← 8 automated tests
├── app.py                 ← Streamlit web app with dropdowns
├── requirements.txt       ← all libraries
├── .gitignore             ← excludes data, models, venv
└── README.md              ← project description
```

---

## STEP 1 — Create Project Folder

Open **Git Bash** and run:

```bash
cd ~/Desktop
mkdir fraud-detection
cd fraud-detection
mkdir src tests data models
```

Copy all the provided files into the correct folders.

Verify:
```bash
ls
ls src/
```

**You should see:**
```
app.py  README.md  requirements.txt  .gitignore  src/  tests/  data/  models/

src/: generate_data.py  preprocess.py  train.py  predict.py
```

---

## STEP 2 — Install Libraries

```bash
pip install -r requirements.txt
```

**You will see** all libraries installing one by one. Wait for it to finish.

Verify:
```bash
pip show scikit-learn streamlit
```

---

## STEP 3 — Generate Sample Data

```bash
cd src
python generate_data.py
```

**You will see:**
```
Generating sample transaction data...
Created 1000 transactions
Fraud cases: 100 (10.0%)
Data saved to ../data/transactions.csv
```

Verify:
```bash
cd ..
ls data/
```

**You will see:** `transactions.csv`

---

## STEP 4 — Train the Model

```bash
cd src
python train.py
```

**You will see:**
```
=============================================
  Fraud Detection Model Training
=============================================
Data loaded: 1000 rows, 9 columns
Fraud cases: 100 (10.0%)

Train: 800 rows | Test: 200 rows
Model trained!

=============================================
  Model Results
=============================================
  Accuracy  : 0.92
  Precision : 0.88
  Recall    : 0.80
  F1 Score  : 0.84
  ROC-AUC   : 0.95
=============================================

Model saved to: ../models/fraud_model.pkl
```

Verify:
```bash
cd ..
ls models/
```

**You will see:** `fraud_model.pkl`

---

## STEP 5 — Run Predictions from Terminal

```bash
cd src
python predict.py
```

**You will see:**
```
Transaction 1: Amount ₹450 | Hour 14:00
  Result     : LEGITIMATE
  Confidence : 96.0%
  Risk       : LOW

Transaction 2: Amount ₹45000 | Hour 3:00
  Result     : FRAUD
  Confidence : 88.0%
  Risk       : HIGH
```

---

## STEP 6 — Run Tests

```bash
cd ..
pytest tests/test_model.py -v
```

**You will see:**
```
tests/test_model.py::test_model_file_exists    PASSED
tests/test_model.py::test_model_loads          PASSED
tests/test_model.py::test_output_keys          PASSED
tests/test_model.py::test_prediction_is_binary PASSED
tests/test_model.py::test_confidence_range     PASSED
tests/test_model.py::test_risk_level_valid     PASSED
tests/test_model.py::test_legit_transaction    PASSED
tests/test_model.py::test_fraud_transaction    PASSED

8 passed in 1.23s ✅
```

---

## STEP 7 — Launch the Streamlit App

```bash
# Make sure you are in fraud-detection folder (not inside src/)
cd ~/Desktop/fraud-detection

streamlit run app.py
```

**You will see:**
```
  You can now view your Streamlit app in your browser.
  Local URL: http://localhost:8501
```

Your browser opens automatically at `http://localhost:8501`

### What the App Looks Like

```
┌─────────────────────────────────────────────┐
│  🔍 Fraud Detection System                  │
│  MLOps Course — Suresh D R                  │
├──────────────────┬──────────────────────────┤
│ 💰 Amount (₹)    │ 🏪 Merchant Type         │
│ [  1000       ]  │ [grocery ▼]              │
│                  │                          │
│ 🕐 Hour          │ 👤 Customer Age           │
│ [14:00 (Day) ▼] │ [====35====]             │
│                  │                          │
│ 📅 Day of Week   │ 📊 Previous Transactions │
│ [Wednesday   ▼] │ [   50   ]               │
│                  │                          │
│                  │ 📈 Avg Amount (₹)        │
│                  │ [   800  ]               │
├──────────────────┴──────────────────────────┤
│      [ 🔍 Check for Fraud ]                 │
├─────────────────────────────────────────────┤
│  ✅ LEGITIMATE TRANSACTION                  │
│  Prediction: LEGITIMATE                     │
│  Confidence: 4.0%   Risk: 🟢 LOW           │
└─────────────────────────────────────────────┘
```

### How to Use the App

1. Change the **Amount** — try ₹500 vs ₹95000
2. Change the **Hour** — try 14:00 (day) vs 2:00 (night)
3. Change the **Merchant Type** — try grocery vs jewellery
4. Change **Previous Transactions** — try 100 vs 1
5. Click **Check for Fraud**
6. See the result — FRAUD or LEGITIMATE with confidence and risk level

### Stop the App

Press `Ctrl + C` in terminal to stop Streamlit.

---

## STEP 8 — Initialise Git and Push to GitHub

### 8a — Initialise Git

```bash
cd ~/Desktop/fraud-detection

git init
git branch -M main
```

### 8b — Check Status

```bash
git status
```

**You will see** all your files listed — but NOT `data/` or `models/` — .gitignore is protecting them. ✅

### 8c — Stage and Commit

```bash
git add .
git status
git commit -m "Initial commit — fraud detection ML project with Streamlit app"
```

### 8d — Create Repo on GitHub

1. Go to `https://github.com`
2. Click **+** → **New repository**
3. Name: `fraud-detection`
4. Description: `Fraud Detection ML project with Streamlit frontend`
5. Set to **Public**
6. **Do NOT** add README or .gitignore
7. Click **Create repository**
8. Copy the URL shown

### 8e — Connect and Push

```bash
git remote add origin https://github.com/your-username/fraud-detection.git
git push -u origin main
```

When asked for password → use your **Personal Access Token** (not GitHub password)

### 8f — Verify on GitHub

Open: `https://github.com/your-username/fraud-detection`

**You will see** all your files. Notice:
- ✅ `src/`, `tests/`, `app.py`, `requirements.txt` are there
- ❌ `data/` and `models/` are NOT there — .gitignore protected them

---

## STEP 9 — Create a Feature Branch and Improve the Model

```bash
git checkout -b feature/improve-model
```

Open `src/train.py` in VS Code and change:
```python
# Change this line
model = RandomForestClassifier(n_estimators=100, max_depth=5, ...)

# To this
model = RandomForestClassifier(n_estimators=200, max_depth=10, ...)
```

Save the file. Retrain:

```bash
cd src
python train.py
cd ..
```

Commit and push:

```bash
git add src/train.py
git commit -m "Improve model — 200 trees, depth 10 for better accuracy"
git push origin feature/improve-model
```

---

## STEP 10 — Open Pull Request and Merge on GitHub

1. Go to GitHub → your repo
2. Click **Compare & pull request** (yellow banner)
3. Title: `Improve Random Forest — more trees, better accuracy`
4. Description:
```
What changed:
- Increased n_estimators from 100 to 200
- Increased max_depth from 5 to 10

Why:
- More trees = more stable predictions
- Better fraud detection accuracy
```
5. Click **Create pull request**
6. Click **Merge pull request** → **Confirm merge**

Pull the merge back to your laptop:

```bash
git checkout main
git pull
```

---

## STEP 11 — Tag as Version 1.0.0

```bash
git tag -a v1.0.0 -m "Version 1.0.0 — Random Forest fraud detection with Streamlit"
git push origin --tags
```

On GitHub → click **Tags** → you will see `v1.0.0`

---

## STEP 12 — See Your Full Commit History

```bash
git log --oneline
```

**You will see:**
```
e5f6g7h (HEAD -> main, tag: v1.0.0, origin/main) Merge feature/improve-model
d4e5f6g Improve model — 200 trees, depth 10 for better accuracy
a1b2c3d Initial commit — fraud detection ML project with Streamlit app
```

---

## Quick Command Reference for This Project

```bash
# Run the full pipeline
pip install -r requirements.txt
cd src && python generate_data.py
python train.py
python predict.py
cd ..
pytest tests/test_model.py -v
streamlit run app.py

# Git workflow
git init
git branch -M main
git add .
git commit -m "message"
git remote add origin <url>
git push -u origin main

# Branch workflow
git checkout -b feature/branch-name
git add .
git commit -m "message"
git push origin feature/branch-name
# → open PR on GitHub → merge → 
git checkout main && git pull
```

---

## Common Errors and Fixes

| Error | Fix |
|-------|-----|
| `Model not found` | Run `python src/train.py` first |
| `ModuleNotFoundError: streamlit` | Run `pip install -r requirements.txt` |
| `streamlit not recognized` | Use `python -m streamlit run app.py` |
| `touch not recognized` | Use Git Bash, not CMD |
| `Authentication failed` | Use Personal Access Token as password |
| `src refspec main does not match` | Run `git branch -M main` first |
| `Port 8501 already in use` | Run `streamlit run app.py --server.port 8502` |

---

*MLOps Syllabus — Deploy and Retrain ML Models on AWS*
*Author: Suresh D R | AI Product Developer & Technology Mentor*
