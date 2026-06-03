"""
This script categorizes gene expression levels based on RNA-Seq read counts.
The categorization is as follows:
- High Expression: Read count >= 500
- Medium Expression: Read count > 50 and < 500
- Low Expression: Read count <= 50
The script uses a predefined dictionary of gene names and their corresponding read counts.
"""

# Sample gene expression data (gene name: read count)
gene_data = {
    "GAPDH": 1250,    # Housekeeping gene (usually very high)
    "TP53": 310,      # Tumor suppressor (medium expression)
    "BRCA1": 45,      # DNA repair gene (low expression)
    "MYC": 620,       # Transcription factor (high expression)
    "IL6": 12         # Cytokine (low expression when healthy)
}

# Categorize and print the expression levels for each gene
print("---RNA-Seq Expression Summary---")

# Loop through the gene data and categorize each gene based on its read count
for gene_name, count in gene_data.items():

    # Determine the expression category based on the read count
    if count >= 500:
        category = "High"
    elif count > 50 and count < 500:
        category = "Medium"
    else:
        category = "Low"

    # Print the gene name, read count, and expression category
    print(f"Gene: {gene_name}, Read Count: {count}, Status: {category}")
    print("-------------------------------")
