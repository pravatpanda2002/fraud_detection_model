# src/app.py
# Streamlit frontend for Fraud Detection Model
# Run with: streamlit run src/app.py

import os, sys
import streamlit as st
import numpy as np

sys.path.insert(0, os.path.dirname(__file__))
from predict import load_model, predict

# ── Page config ───────────────────────────────────────────────────
st.set_page_config(
    page_title="Fraud Detection App",
    page_icon="🔍",
    layout="centered"
)

# ── Load model ────────────────────────────────────────────────────
@st.cache_resource
def get_model():
    return load_model("models/fraud_model.pkl")

# ── Header ────────────────────────────────────────────────────────
st.title("🔍 Fraud Detection System")
st.markdown("**MLOps Course — Suresh D R | AI Product Developer**")
st.markdown("---")
st.markdown("Fill in the transaction details below and click **Predict** to check if it is fraud.")

# ── Input Form ───────────────────────────────────────────────────
st.subheader("📋 Transaction Details")

col1, col2 = st.columns(2)

with col1:
    amount = st.number_input(
        "Transaction Amount (₹)",
        min_value=1,
        max_value=1000000,
        value=5000,
        step=100,
        help="Enter the transaction amount in rupees"
    )

    hour = st.selectbox(
        "Hour of Transaction",
        options=list(range(0, 24)),
        index=14,
        format_func=lambda x: f"{x:02d}:00  {'🌙 Late Night' if x < 5 or x >= 22 else '☀️ Daytime' if 8 <= x < 20 else '🌆 Evening'}",
        help="Hour when the transaction happened (0 = midnight, 23 = 11pm)"
    )

    day_of_week = st.selectbox(
        "Day of Week",
        options=[0, 1, 2, 3, 4, 5, 6],
        format_func=lambda x: ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"][x],
        index=2,
        help="Day when the transaction happened"
    )

    merchant_type = st.selectbox(
        "Merchant Type",
        options=["grocery", "restaurant", "retail", "pharmacy", "fuel", "electronics", "online", "jewellery"],
        index=0,
        help="Type of shop or merchant where transaction happened"
    )

with col2:
    customer_age = st.slider(
        "Customer Age",
        min_value=18,
        max_value=80,
        value=35,
        help="Age of the customer"
    )

    num_prev_txns = st.number_input(
        "Number of Previous Transactions",
        min_value=0,
        max_value=500,
        value=50,
        step=5,
        help="How many transactions has this customer made before?"
    )

    avg_txn_amount = st.number_input(
        "Customer's Average Transaction Amount (₹)",
        min_value=1,
        max_value=500000,
        value=3000,
        step=100,
        help="What is this customer's usual transaction amount?"
    )

# ── Show computed risk signals ────────────────────────────────────
st.markdown("---")
st.subheader("📊 Risk Signals")

sig_col1, sig_col2, sig_col3 = st.columns(3)

is_night   = (hour >= 22) or (hour <= 5)
is_weekend = day_of_week >= 5
amount_ratio = round(amount / (avg_txn_amount + 1), 2)

with sig_col1:
    st.metric("Late Night Transaction", "⚠️ YES" if is_night else "✅ NO")

with sig_col2:
    st.metric("Weekend Transaction", "⚠️ YES" if is_weekend else "✅ NO")

with sig_col3:
    st.metric("Amount vs Customer Average", f"{amount_ratio}x",
              delta=f"{'HIGH' if amount_ratio > 5 else 'NORMAL'}",
              delta_color="inverse")

# ── Predict Button ────────────────────────────────────────────────
st.markdown("---")

if st.button("🔍 Predict — Is This Fraud?", use_container_width=True, type="primary"):
    try:
        model = get_model()

        transaction = {
            "amount"         : amount,
            "hour"           : hour,
            "day_of_week"    : day_of_week,
            "merchant_type"  : merchant_type,
            "customer_age"   : customer_age,
            "num_prev_txns"  : num_prev_txns,
            "avg_txn_amount" : avg_txn_amount,
        }

        result = predict(model, transaction)

        st.markdown("---")
        st.subheader("🎯 Prediction Result")

        if result["prediction"] == "FRAUD":
            st.error(f"🚨 FRAUD DETECTED")
            st.markdown(f"### ❌ This transaction is flagged as **FRAUD**")
        else:
            st.success(f"✅ LEGITIMATE TRANSACTION")
            st.markdown(f"### ✅ This transaction appears **LEGITIMATE**")

        res_col1, res_col2, res_col3 = st.columns(3)

        with res_col1:
            st.metric("Prediction", result["prediction"])

        with res_col2:
            st.metric("Fraud Confidence", f"{result['confidence']}%")

        with res_col3:
            risk_emoji = {"HIGH": "🔴", "MEDIUM": "🟡", "LOW": "🟢"}
            st.metric("Risk Level", f"{risk_emoji[result['risk_level']]} {result['risk_level']}")

        # Progress bar showing fraud probability
        st.markdown("**Fraud Probability:**")
        st.progress(result["confidence"] / 100)

        # Explanation
        st.markdown("---")
        st.subheader("💡 Why This Prediction?")

        reasons = []
        if is_night:
            reasons.append("🌙 Transaction happened during late night hours (high fraud signal)")
        if is_weekend:
            reasons.append("📅 Transaction happened on a weekend")
        if amount_ratio > 5:
            reasons.append(f"💰 Amount is {amount_ratio}x higher than customer's average (suspicious)")
        if num_prev_txns < 5:
            reasons.append("👤 Customer has very few previous transactions (new/unusual activity)")
        if merchant_type in ["electronics", "jewellery", "online"]:
            reasons.append(f"🏪 {merchant_type.capitalize()} purchases have higher fraud rates")

        if reasons:
            for r in reasons:
                st.markdown(f"- {r}")
        else:
            st.markdown("- No major risk signals detected in this transaction")

    except FileNotFoundError:
        st.error("⚠️ Model not found! Please run `python src/train.py` first to train the model.")

# ── Footer ────────────────────────────────────────────────────────
st.markdown("---")
st.markdown("*MLOps Syllabus — Deploy and Retrain ML Models on AWS | Suresh D R*")
