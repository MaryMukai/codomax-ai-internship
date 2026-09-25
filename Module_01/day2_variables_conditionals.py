"""
Codomax Internship - Module 1 (Day 2)
Variables, Data Types, and Conditionals
Context: Evaluating single M-Pesa transaction limits and risk factors
"""

# Transaction attributes (Variables & Data Types)
sender_phone = "0712345678"          # string
receiver_phone = "0799999999"        # string
transaction_amount = 65000.0         # float
is_first_time_recipient = True       # boolean
transaction_hour = 23                # integer (11 PM)

# Risk Evaluation Logic (Conditionals)
risk_score = 0
risk_reasons = []

if transaction_amount > 50000:
    risk_score += 40
    risk_reasons.append("High amount threshold reached (> KES 50,000)")

if is_first_time_recipient:
    risk_score += 20
    risk_reasons.append("First-time transfer to recipient")

if transaction_hour >= 22 or transaction_hour <= 4:
    risk_score += 30
    risk_reasons.append("Late-night transaction window")

# Display Assessment Output
print(f"Transaction: {sender_phone} -> {receiver_phone}")
print(f"Amount: KES {transaction_amount:,.2f}")
print(f"Calculated Risk Score: {risk_score}/100")

if risk_reasons:
    print("Risk Factors Identified:")
    for reason in risk_reasons:
        print(f"  - {reason}")

if risk_score >= 50:
    print("\nAction Required: TRANSACTION FLAGGED FOR PIN & OTP VERIFICATION")
else:
    print("\nAction Required: TRANSACTION APPROVED")
