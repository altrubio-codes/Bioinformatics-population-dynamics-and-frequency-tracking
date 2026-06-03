gene_data = {
    "GAPDH": 1250,    # Housekeeping gene (usually very high)
    "TP53": 310,      # Tumor suppressor (medium expression)
    "BRCA1": 45,      # DNA repair gene (low expression)
    "MYC": 620,       # Transcription factor (high expression)
    "IL6": 12         # Cytokine (low expression when healthy)
}


print("---RNA-Seq Expression Summary---")

for gene_name, count in gene_data.items():

    if count >= 500:
        category = "High"
    elif count > 50 and count < 500:
        category = "Medium"
    else:
        category = "Low"

    print(f"Gene: {gene_name}, Read Count: {count}, Status: {category}")
    print("-------------------------------")
