import pandas as pd
import lifelines
import matplotlib.pyplot as plt

genomic_data = pd.read_csv("genomic_data.csv")
survival_data = pd.read_csv("survival_data.csv")

merged_data = pd.merge(genomic_data, survival_data, on="patient_id")

# Perform survival analysis
kmf = lifelines.KaplanMeierFitter()
kmf.fit(merged_data["survival_time"], event_observed=merged_data["event"])

# Plot survival curves
plt.figure(figsize=(10, 6))
kmf.plot()
plt.title("Kaplan-Meier Survival Analysis with Genomic Features")
plt.xlabel("Time")
plt.ylabel("Survival Probability")
plt.show()
