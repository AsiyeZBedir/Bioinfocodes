import pandas as pd
import numpy as np
from scipy.stats import ttest_ind

# Load gene expression data (example format: gene_name, cancer_samples, normal_samples)
data = pd.read_csv("gene_expression_data.csv")

cancer_samples = data['cancer_samples']
normal_samples = data['normal_samples']

# Perform a two-sample t-test to identify differentially expressed genes
p_values = []
differentially_expressed_genes = []

for gene in data['gene_name']:
    gene_expression_cancer = data[gene_name == gene]['cancer_samples']
    gene_expression_normal = data[gene_name == gene]['normal_samples']

    # Perform t-test
    p_value = ttest_ind(gene_expression_cancer, gene_expression_normal).pvalue
    p_values.append(p_value)

    # Define a significance threshold
    significance_threshold = 0.05

    if p_value < significance_threshold:
        differentially_expressed_genes.append(gene)

# Output differentially expressed genes
print("Differentially Expressed Genes:")
print(differentially_expressed_genes)
