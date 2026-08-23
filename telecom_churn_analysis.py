import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("telecom_customer_churn_dataset.csv")


# Customer Base Analysis

total_customers = df.shape[0]
print("Total Customers:", total_customers)


# Overall Churn Analysis

churn_count = df[df['Churn'] == 'Yes'].shape[0]
print("Churn Count:", churn_count)


# Overall Churn Rate

churn_rate = churn_count / total_customers * 100
print("Churn Rate:", round(churn_rate, 2), "%")


# Churn Rate by Contract Type

total_by_contract = df.groupby('Contract').size()
churn_by_contract = df[df['Churn'] == 'Yes'].groupby('Contract').size()
churn_rate_by_contract = churn_by_contract / total_by_contract * 100

print("Churn Rate by Contract:")
print(churn_rate_by_contract.round(2))


# Churn Rate by Payment Method

total_by_paymentmethod = df.groupby('PaymentMethod').size()
churn_by_payment_method = df[df['Churn'] == 'Yes'].groupby('PaymentMethod').size()
churn_rate_by_payment_method = churn_by_payment_method / total_by_paymentmethod * 100

print("Churn Rate by Payment Method:")
print(churn_rate_by_payment_method.round(2))


# Churn Rate by Internet Service

total_by_internetservice = df.groupby('InternetService').size()
churn_by_internetservice = df[df['Churn'] == 'Yes'].groupby('InternetService').size()
churn_rate_by_internetservice = churn_by_internetservice / total_by_internetservice * 100

print("Churn Rate by Internet Service:")
print(churn_rate_by_internetservice.round(2))


# Churn Rate by Senior Citizen

total_by_seniorcitizen = df.groupby('SeniorCitizen').size()
churn_by_seniorcitizen = df[df['Churn'] == 'Yes'].groupby('SeniorCitizen').size()
churn_rate_by_seniorcitizen = churn_by_seniorcitizen / total_by_seniorcitizen * 100

print("Churn Rate by Senior Citizen:")
print(churn_rate_by_seniorcitizen.round(2))


# Churn Rate by Tenure Group

df['tenure_group'] = pd.cut(
    df['tenure'],
    bins=[0, 12, 24, 48, 72],
    labels=['0-12', '13-24', '25-48', '49-72']
)

total_by_tenure = df.groupby('tenure_group', observed=True).size()
churn_by_tenure = df[df['Churn'] == 'Yes'].groupby(
    'tenure_group', observed=True
).size()

churn_rate_by_tenure = churn_by_tenure / total_by_tenure * 100

print("Churn Rate by Tenure:")
print(churn_rate_by_tenure.round(2))


# Churn Rate by Monthly Charges

df['monthly_charge_group'] = pd.cut(
    df['MonthlyCharges'],
    bins=[0, 30, 60, 90, 120],
    labels=['0-30', '31-60', '61-90', '91-120']
)

total_by_monthly_charge = df.groupby(
    'monthly_charge_group', observed=True
).size()

churn_by_monthly_charge = df[df['Churn'] == 'Yes'].groupby(
    'monthly_charge_group', observed=True
).size()

churn_rate_by_monthly_charge = (
    churn_by_monthly_charge / total_by_monthly_charge
) * 100

print("Churn Rate by Monthly Charge:")
print(churn_rate_by_monthly_charge.round(2))


# Highest Churn Customer Segment

segment_analysis = df.groupby(
    ['Contract', 'InternetService', 'PaymentMethod']
).agg(
    total_customers=('Churn', 'size'),
    churned_customers=('Churn', lambda x: (x == 'Yes').sum())
)

segment_analysis['churn_rate'] = (
    segment_analysis['churned_customers']
    / segment_analysis['total_customers']
) * 100

segment_analysis['churn_rate'] = segment_analysis['churn_rate'].round(2)

print("Highest Churn Customer Segments:")
print(
    segment_analysis
    .sort_values('churn_rate', ascending=False)
    .head(10)
)


# Visualizations

# 1. Customer Churn Count

churn_counts = df['Churn'].value_counts()

plt.figure(figsize=(6, 4))
plt.bar(churn_counts.index, churn_counts.values)
plt.title("Customer Churn Count")
plt.xlabel("Churn")
plt.ylabel("Number of Customers")
plt.show()


# 2. Churn Rate by Contract

plt.figure(figsize=(7, 4))
plt.bar(
    churn_rate_by_contract.index,
    churn_rate_by_contract.values
)
plt.title("Churn Rate by Contract")
plt.xlabel("Contract")
plt.ylabel("Churn Rate (%)")
plt.show()


# 3. Churn Rate by Payment Method

plt.figure(figsize=(8, 4))
plt.bar(
    churn_rate_by_payment_method.index,
    churn_rate_by_payment_method.values
)
plt.title("Churn Rate by Payment Method")
plt.xlabel("Payment Method")
plt.ylabel("Churn Rate (%)")
plt.xticks(rotation=15)
plt.show()


# 4. Churn Rate by Internet Service

plt.figure(figsize=(7, 4))
plt.bar(
    churn_rate_by_internetservice.index,
    churn_rate_by_internetservice.values
)
plt.title("Churn Rate by Internet Service")
plt.xlabel("Internet Service")
plt.ylabel("Churn Rate (%)")
plt.show()


# 5. Churn Rate by Tenure Group

plt.figure(figsize=(7, 4))
plt.bar(
    churn_rate_by_tenure.index.astype(str),
    churn_rate_by_tenure.values
)
plt.title("Churn Rate by Tenure Group")
plt.xlabel("Tenure Group (Months)")
plt.ylabel("Churn Rate (%)")
plt.show()