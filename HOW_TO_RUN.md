# How to Run — Fraud Detection Project
**Author: Suresh D R | AI Product Developer & Technology Mentor**
*MLOps Syllabus — Deploy and Retrain ML Models on AWS*

---

## What You Will Do
```
Step 0  → Install VS Code and open the project
Step 1  → Set up project folder inside VS Code
Step 2  → Install libraries using VS Code terminal
Step 3  → Generate sample data
Step 4  → Train the model
Step 5  → Run predictions from terminal
Step 6  → Run tests
Step 7  → Launch Streamlit frontend
Step 8  → Push everything to GitHub
Step 9  → Create a branch and improve the model
Step 10 → Open Pull Request and merge
```

---

## STEP 0 — Install VS Code and Open the Project

### 0a — Install VS Code

1. Open browser → go to `https://code.visualstudio.com`
2. Click **Download for Windows** (or Mac/Linux)
3. Run the installer → click **Next** on every screen → click **Finish**
4. VS Code opens automatically

### 0b — Install the Python Extension in VS Code

1. Open VS Code
2. Click the **Extensions icon** on the left sidebar (looks like 4 squares)
3. Search: `Python`
4. Click **Python** by Microsoft → click **Install** → wait for install ✅

### 0c — Unzip and Open the Project in VS Code

1. Download `fraud-detection.zip`
2. Right click the zip → **Extract All** → choose Desktop → click **Extract**
3. Open VS Code → click **File** (top menu) → **Open Folder**
4. Navigate to Desktop → click `fraud-detection` → click **Select Folder**
5. VS Code opens — all files are visible in the **left sidebar** ✅

### 0d — Open Terminal Inside VS Code

> All commands run inside VS Code terminal — NOT in CMD, NOT in PowerShell separately.

**How to open the terminal:**
1. In VS Code → click **Terminal** in the top menu bar
2. Click **New Terminal**
3. A terminal panel opens at the **bottom** of VS Code

**Change terminal to Git Bash (Windows only):**
1. In the terminal panel → look at the top right of the terminal → click the **dropdown arrow** (▾) next to the + icon
2. Click **Select Default Profile**
3. Click **Git Bash**
4. Click **Terminal** → **New Terminal** again to open a fresh Git Bash terminal

**You will see this in the terminal:**
```
Suresh D R@DESKTOP MINGW64 ~/Desktop/fraud-detection
$
```

> ⚠️ If you see `PS C:\Users\...>` — that is PowerShell. Repeat the steps above to switch to Git Bash.

**You are now ready. Run all commands in this VS Code Git Bash terminal.**

---

## STEP 1 — Set Up Project Folder Inside VS Code

**In the VS Code terminal, confirm you are in the right folder:**

```bash
pwd
```

**You will see:**
```
/c/Users/Suresh D R/Desktop/fraud-detection
```

**Create subfolders:**
```bash
mkdir src tests data models
```

**Create all code files using VS Code sidebar:**
1. In the left sidebar — right click on the `src` folder → **New File**
2. Type the filename → press Enter → file opens → paste the code → `Ctrl+S` to save
3. Repeat for each file:

| File | Folder |
|------|--------|
| `generate_data.py` | `src/` |
| `preprocess.py` | `src/` |
| `train.py` | `src/` |
| `predict.py` | `src/` |
| `app.py` | `src/` |
| `test_model.py` | `tests/` |
| `requirements.txt` | root folder |
| `README.md` | root folder |
| `.gitignore` | root folder |

**After adding all files, your VS Code left sidebar looks like:**
```
fraud-detection/
├── 📁 src/
│   ├── 📄 app.py
│   ├── 📄 generate_data.py
│   ├── 📄 predict.py
│   ├── 📄 preprocess.py
│   └── 📄 train.py
├── 📁 tests/
│   └── 📄 test_model.py
├── 📁 data/          ← empty for now
├── 📁 models/        ← empty for now
├── 📄 .gitignore
├── 📄 requirements.txt
└── 📄 README.md
```

---

---

## STEP 2 — Install Libraries

**In the VS Code terminal (Git Bash at the bottom):**

```bash
pip install -r requirements.txt
```

**You will see all libraries downloading and installing one by one. Wait for it to finish completely.**

To verify everything installed:
```bash
pip show scikit-learn
pip show streamlit
```

**You will see version information for each library. ✅**

> ⚠️ If you see `pip not found` — try `pip3 install -r requirements.txt`

---

## STEP 3 — Generate Sample Data

**In the VS Code terminal:**

```bash
cd src
python generate_data.py
```

**You will see:**
```
Generating sample transaction data...
Created 1000 transactions
Fraud cases: 100 (10.0%)
Data saved to: ../data/transactions.csv
```

```bash
# Go back to project root and verify
cd ..
ls data/
```

**You will see:**
```
transactions.csv
```

---

## STEP 4 — Train the Model

**In the VS Code terminal:**

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

Training Random Forest...

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

```bash
# Go back and verify model was saved
cd ..
ls models/
```

**You will see:**
```
fraud_model.pkl
```

---

## STEP 5 — Test Predictions from Terminal

**In the VS Code terminal:**

```bash
cd src
python predict.py
```

**You will see:**
```
Transaction 1: ₹450   | grocery     | Hour:14 => LEGITIMATE (96.0%) [LOW]
Transaction 2: ₹45,000 | electronics | Hour:3  => FRAUD      (88.0%) [HIGH]
Transaction 3: ₹1,200  | restaurant  | Hour:19 => LEGITIMATE (94.0%) [LOW]
Transaction 4: ₹120,000| jewellery   | Hour:1  => FRAUD      (91.0%) [HIGH]
```

---

## STEP 6 — Run Tests

**In the VS Code terminal:**

```bash
# Go back to project root first
cd ..

# Run all tests
pytest tests/test_model.py -v
```

**You will see:**
```
tests/test_model.py::test_model_file_exists        PASSED
tests/test_model.py::test_model_loads              PASSED
tests/test_model.py::test_prediction_keys          PASSED
tests/test_model.py::test_prediction_is_binary     PASSED
tests/test_model.py::test_confidence_range         PASSED
tests/test_model.py::test_risk_level_valid         PASSED
tests/test_model.py::test_legitimate_prediction    PASSED
tests/test_model.py::test_fraud_prediction         PASSED

8 passed in 1.23s ✅
```

---

## STEP 7 — Launch Streamlit Frontend

**In the VS Code terminal — make sure you are in the project root:**

```bash
# Confirm you are in fraud-detection/ folder
pwd

# Launch the app
streamlit run src/app.py
```

**You will see:**
```
You can now view your Streamlit app in your browser.

Local URL: http://localhost:8501
Network URL: http://192.168.x.x:8501
```

**Your browser opens automatically** with the fraud detection app!

### How to Use the App
1. Enter **Transaction Amount** — try ₹500 (normal) vs ₹95,000 (suspicious)
2. Select **Hour** — try 14:00 (daytime) vs 02:00 (late night)
3. Select **Day of Week** — Monday to Sunday
4. Select **Merchant Type** — grocery vs jewellery vs electronics
5. Enter **Customer Age**, **Previous Transactions**, **Average Amount**
6. Click **🔍 Predict — Is This Fraud?**
7. See the result — FRAUD or LEGITIMATE, confidence %, risk level

### Test These Combinations in the App

| Scenario | Amount | Hour | Merchant | Expected |
|----------|--------|------|----------|----------|
| Normal purchase | ₹500 | 14:00 | Grocery | ✅ LEGITIMATE |
| Late night electronics | ₹45,000 | 03:00 | Electronics | 🚨 FRAUD |
| Lunch at restaurant | ₹1,200 | 13:00 | Restaurant | ✅ LEGITIMATE |
| Midnight jewellery | ₹1,20,000 | 01:00 | Jewellery | 🚨 FRAUD |

**To stop the app:** Press `Ctrl + C` in the terminal.

---

## STEP 8 — Push Everything to GitHub

---

### 8a — Create a GitHub Account (if you don't have one)

1. Open browser → go to `https://github.com`
2. Click **Sign up** (top right)
3. Enter your **email**, **password**, **username**
   - Username example: `sureshdr-mlops` — this is permanent and public
4. Click **Create account**
5. Check your email → click the verification link GitHub sends
6. Choose **Free** plan → click Continue

---

### 8b — Configure Git with Your Identity (run once)

Open **Git Bash** and run:

```bash
git config --global user.name "Suresh D R"
git config --global user.email "your-email@gmail.com"
```

> ⚠️ Use the **same email** as your GitHub account

Verify:
```bash
git config --list
```

You will see your name and email printed. ✅

---

### 8c — Generate a Personal Access Token (GitHub Password Replacement)

GitHub no longer accepts your account password for pushing code.
You need a **Personal Access Token** instead. Do this once:

1. Log in to `https://github.com`
2. Click your **profile picture** → **Settings**
3. Scroll all the way down the left sidebar → click **Developer settings**
4. Click **Personal access tokens** → **Tokens (classic)**
5. Click **Generate new token** → **Generate new token (classic)**
6. Fill in:
   - **Note:** `fraud-detection-push`
   - **Expiration:** 90 days
   - **Select scopes:** tick ✅ **repo** (the top checkbox — this gives full repo access)
7. Scroll down → click **Generate token**
8. **COPY THE TOKEN IMMEDIATELY** — it looks like `ghp_xxxxxxxxxxxxxxxxxxxx`
   - ⚠️ You can NEVER see this token again after closing the page
   - Save it in Notepad or somewhere safe

---

### 8d — Create a New Repository on GitHub

1. On GitHub → click the **+** icon (top right corner)
2. Click **New repository**
3. Fill in:

| Field | What to Enter |
|-------|--------------|
| Repository name | `fraud-detection` |
| Description | `Fraud Detection ML project with Streamlit frontend` |
| Public or Private | **Public** |
| Add a README file | ❌ Do NOT tick this |
| Add .gitignore | ❌ Do NOT tick this |
| Choose a license | None |

4. Click **Create repository**
5. GitHub shows your empty repo — **copy the URL** at the top:
```
https://github.com/your-username/fraud-detection.git
```

---

### 8e — Initialise Git in Your Project Folder

Open **Git Bash** → navigate to your project:

```bash
cd ~/Desktop/fraud-detection
pwd
```

**You will see:**
```
/c/Users/Suresh D R/Desktop/fraud-detection
```

Initialise Git:
```bash
git init
```

**You will see:**
```
Initialized empty Git repository in .../fraud-detection/.git/
```

---

### 8f — Check What Git Will Track

```bash
git status
```

**You will see your code files listed — BUT:**
- `data/` folder → NOT listed ✅ (.gitignore protecting it)
- `models/` folder → NOT listed ✅ (.gitignore protecting it)
- `.env` → NOT listed ✅ (.gitignore protecting it)

Only your code files appear. Perfect.

---

### 8g — Stage and Commit All Files

```bash
# Stage all files
git add .

# Check what is staged (all green = ready to commit)
git status

# Make your first commit
git commit -m "Initial commit — fraud detection project with Streamlit frontend"
```

**You will see:**
```
[main (root-commit) a1b2c3d] Initial commit — fraud detection project with Streamlit frontend
 8 files changed, 350 insertions(+)
 create mode 100644 .gitignore
 create mode 100644 README.md
 create mode 100644 requirements.txt
 create mode 100644 src/app.py
 create mode 100644 src/generate_data.py
 create mode 100644 src/predict.py
 create mode 100644 src/preprocess.py
 create mode 100644 src/train.py
 create mode 100644 tests/test_model.py
```

---

### 8h — Connect to GitHub and Push

```bash
# Rename branch from master to main
git branch -M main

# Connect your laptop to your GitHub repo
# (paste YOUR url from Step 8d)
git remote add origin https://github.com/your-username/fraud-detection.git

# Verify the connection
git remote -v
```

**You will see:**
```
origin  https://github.com/your-username/fraud-detection.git (fetch)
origin  https://github.com/your-username/fraud-detection.git (push)
```

Now push:
```bash
git push -u origin main
```

**GitHub will ask for login:**
- **Username** → your GitHub username (example: `drsuresh8453`)
- **Password** → paste the **Personal Access Token** you copied in Step 8c

**You will see:**
```
Enumerating objects: 12, done.
Counting objects: 100% (12/12), done.
Writing objects: 100% (12/12), 8.50 KiB | 1.21 MiB/s, done.
To https://github.com/your-username/fraud-detection.git
 * [new branch]      main -> main
branch 'main' set up to track 'origin/main'.
```

---

### 8i — Verify Everything on GitHub

Open your browser:
```
https://github.com/your-username/fraud-detection
```

**You will see:**
- ✅ All your code files listed
- ✅ `src/`, `tests/` folders visible
- ✅ `README.md` displayed at the bottom
- ❌ `data/` folder NOT there — .gitignore worked
- ❌ `models/` folder NOT there — .gitignore worked

Click on any file to view its contents.
Click **Commits** to see your commit history with your name and message. ✅

**Your project is now live on GitHub!**

---

## STEP 9 — Create a Branch and Improve the Model

This is how professional teams work — never change main directly.

```bash
# Create a feature branch
git checkout -b feature/improve-model

# Open src/train.py in VS Code
# Find these two lines:
#   n_estimators=100
#   max_depth=5
# Change them to:
#   n_estimators=200
#   max_depth=10
# Save the file

# Retrain with improved settings
cd src
python train.py
cd ..

# Commit the improvement
git add src/train.py
git commit -m "Improve model — 200 trees, depth 10 for better accuracy"

# Push the branch to GitHub
git push origin feature/improve-model
```

---

## STEP 10 — Open Pull Request and Merge

### On GitHub:
1. Go to your repository
2. You will see a banner: *"feature/improve-model had recent pushes"*
3. Click **Compare & pull request**
4. Fill in:
   - **Title:** `Improve Random Forest — more trees, better accuracy`
   - **Description:**
     ```
     What changed:
     - n_estimators: 100 → 200 (more stable predictions)
     - max_depth: 5 → 10 (captures more complex patterns)
     ```
5. Click **Create pull request**
6. Click **Merge pull request** → **Confirm merge**

### Pull the merge back to your laptop:
```bash
git checkout main
git pull
```

---

## STEP 11 — Tag This as Version 1.0

```bash
git tag -a v1.0.0 -m "Version 1.0.0 — Fraud detection with Streamlit frontend"
git push origin --tags
```

Go to GitHub → **Tags** → see `v1.0.0` listed ✅

---

## Final Check — See Everything You Did

```bash
git log --oneline
```

**You will see:**
```
f6g7h8i (HEAD -> main, tag: v1.0.0) Merge feature/improve-model
e5f6g7h Improve model — 200 trees, depth 10
a1b2c3d Initial commit — fraud detection project with Streamlit frontend
```

---

## Common Errors and Fixes

| Error | Fix |
|-------|-----|
| `touch not recognized` | Use Git Bash, not CMD |
| `ModuleNotFoundError: streamlit` | Run `pip install -r requirements.txt` |
| `Model not found` | Run `python src/train.py` first |
| `src refspec main does not match` | Run `git branch -M main` first |
| `Authentication failed` | Use Personal Access Token as password |
| `Updates were rejected` | Run `git pull` first, then push |
| Port 8501 already in use | Run `streamlit run src/app.py --server.port 8502` |

---

## Summary of All Commands

```bash
# Setup
pip install -r requirements.txt

# Run pipeline
cd src
python generate_data.py
python train.py
python predict.py
cd ..
pytest tests/test_model.py -v
streamlit run src/app.py

# Git workflow
git init
git add .
git commit -m "message"
git branch -M main
git remote add origin <url>
git push -u origin main

# Branch workflow
git checkout -b feature/name
git add .
git commit -m "message"
git push origin feature/name
# open PR on GitHub → merge
git checkout main
git pull

# Tag release
git tag -a v1.0.0 -m "message"
git push origin --tags
```

---

*MLOps Syllabus — Deploy and Retrain ML Models on AWS*
*Author: Suresh D R | AI Product Developer & Technology Mentor*
