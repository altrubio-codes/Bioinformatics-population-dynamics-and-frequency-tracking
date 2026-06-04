"""
This script calculates the fold change in gene expression between control and treatment conditions for a set of genes.
It identifies which genes are upregulated, downregulated, or have no significant change based on the calculated fold change values.
The fold change is calculated as the ratio of treatment expression to control expression,
and thresholds are set to determine the regulation status of each gene.
"""

# Dictionaries basis for control and treatment gene expression data
control_data = {
    "MYC" : 100,
    "TP53" : 200,
    "EGFR" : 300,
    "BRCA1" : 400,
    "PTEN" : 500
}

# Dictionary to look up treatment gene expression data
treatment_data ={
    "MYC" : 300,
    "TP53" : 250,
    "EGFR" : 350,
    "BRCA1" : 450,
    "PTEN" : 50
}

# Looping through each gene in the control data to calculate fold change and determine regulation status
for gene in control_data:
    control_value = control_data[gene]
    treatment_value = treatment_data[gene]
    
    fold_change = treatment_value / control_value
    
    # Condition to determine if the gene is upregulated, downregulated, or has no significant change based on fold change thresholds
    if fold_change >= 3.0:
        print(f"{gene} is upregulated with a fold change of {fold_change:.2f}")
    elif fold_change <= 0.5:
        print(f"{gene} is downregulated with a fold change of {fold_change:.2f}")
    else:
        print(f"{gene} has no significant change with a fold change of {fold_change:.2f}")
