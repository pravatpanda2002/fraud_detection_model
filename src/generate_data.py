# src/generate_data.py
# Generates sample credit card transaction data for fraud detection
# This is synthetic data — not real customer data

import pandas as pd
import numpy as np
import os

def generate_transactions(n_samples=1000, fraud_rate=0.10, random_state=42):
    """
    Generate synthetic transaction data.
    
    Columns:
    - transaction_id  : unique ID for each transaction
    - amount          : transaction amount in rupees
    - hour            : hour of the day (0-23)
    - day_of_week     : 0=Monday, 6=Sunday
    - merchant_type   : type of merchant (grocery, electronics, etc.)
    - customer_age    : age of the customer
    - num_prev_txns   : number of previous transactions by this customer
    - avg_txn_amount  : average transaction amount for this customer
    - is_fraud        : 1 = fraud, 0 = legitimate (target column)
    """
    
    print("Generating sample transaction data...")
    np.random.seed(random_state)
    
    n_fraud    = int(n_samples * fraud_rate)
    n_legit    = n_samples - n_fraud

    # ── Legitimate transactions ───────────────────────────────────
    legit = {
        "transaction_id"  : [f"TXN{str(i).zfill(5)}" for i in range(n_legit)],
        "amount"          : np.random.lognormal(mean=6.5, sigma=1.0, size=n_legit).round(2),
        "hour"            : np.random.choice(range(8, 22), size=n_legit),   # daytime
        "day_of_week"     : np.random.randint(0, 7, size=n_legit),
        "merchant_type"   : np.random.choice(
                                ["grocery", "restaurant", "retail", "pharmacy", "fuel"],
                                size=n_legit),
        "customer_age"    : np.random.randint(22, 65, size=n_legit),
        "num_prev_txns"   : np.random.randint(5, 200, size=n_legit),
        "avg_txn_amount"  : np.random.lognormal(mean=6.2, sigma=0.8, size=n_legit).round(2),
        "is_fraud"        : [0] * n_legit,
    }

    # ── Fraudulent transactions ───────────────────────────────────
    fraud = {
        "transaction_id"  : [f"TXN{str(i).zfill(5)}" for i in range(n_legit, n_samples)],
        "amount"          : np.random.lognormal(mean=8.5, sigma=1.5, size=n_fraud).round(2),  # higher amounts
        "hour"            : np.random.choice([0,1,2,3,4,22,23], size=n_fraud),               # late night
        "day_of_week"     : np.random.randint(0, 7, size=n_fraud),
        "merchant_type"   : np.random.choice(
                                ["electronics", "online", "jewellery", "fuel", "retail"],
                                size=n_fraud),
        "customer_age"    : np.random.randint(18, 70, size=n_fraud),
        "num_prev_txns"   : np.random.randint(0, 10, size=n_fraud),                           # fewer history
        "avg_txn_amount"  : np.random.lognormal(mean=5.5, sigma=0.5, size=n_fraud).round(2),
        "is_fraud"        : [1] * n_fraud,
    }

    # ── Combine and shuffle ───────────────────────────────────────
    df = pd.concat([pd.DataFrame(legit), pd.DataFrame(fraud)], ignore_index=True)
    df = df.sample(frac=1, random_state=random_state).reset_index(drop=True)

    return df


def save_data(df, filepath="../data/transactions.csv"):
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    df.to_csv(filepath, index=False)
    print(f"Data saved to: {filepath}")


if __name__ == "__main__":
    df = generate_transactions(n_samples=1000, fraud_rate=0.10)
    
    print(f"Created {len(df)} transactions")
    print(f"Fraud cases: {df['is_fraud'].sum()} ({df['is_fraud'].mean()*100:.1f}%)")
    print(f"\nSample data:")
    print(df.head(5).to_string())
    
    save_data(df)
