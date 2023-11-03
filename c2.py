import pandas as pd
import lifelines
import matplotlib.pyplot as plt

gene_expression_data = pd.read_csv("gene_expression_data.csv")

survival_data = pd.read_csv("survival_data.csv")

# Merge gene expression and survival data
merged_data = pd.merge(gene_expression_data, survival_data, on="patient_id")

# Create Kaplan-Meier estimator
kmf = lifelines.KaplanMeierFitter()

# Fit the survival data to the Kaplan-Meier estimator
kmf.fit(merged_data["survival_time"], event_observed=merged_data["event"])

# Plot the Kaplan-Meier survival curve
plt.figure(figsize=(10, 6))
kmf.plot()
plt.title("Kaplan-Meier Survival Curve")
plt.xlabel("Time")
plt.ylabel("Survival Probability")
plt.show()
