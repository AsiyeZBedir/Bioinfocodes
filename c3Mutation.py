import pandas as pd
import matplotlib.pyplot as plt

mutation_data = pd.read_csv("mutation_data.csv")

# Analyze and visualize mutation frequencies
mutation_counts = mutation_data['mutation_status'].value_counts()
mutation_labels = mutation_counts.index
mutation_values = mutation_counts.values

plt.figure(figsize=(8, 6))
plt.bar(mutation_labels, mutation_values, color='lightblue')
plt.title("Mutation Frequency in Cancer Genes")
plt.xlabel("Mutation Status")
plt.ylabel("Frequency")
plt.show()
