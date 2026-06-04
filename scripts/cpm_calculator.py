"""
CPM (Counts Per Million) Calculator
This script calculates the CPM values for a set of genes based on their raw read counts and the total sequencing depth.
The CPM normalization allows for comparison of gene expression levels across different samples by accounting for differences in sequencing depth.
"""

# Sample raw read counts for a set of genes
raw_counts = {
    "ACTB": 15000,   # Actin beta (Structural gene, very high)
    "GAPDH": 8500,   # Metabolic gene (High)
    "TNF": 450,      # Immune signaling gene (Medium)
    "SNAI1": 25      # Development gene (Low)
}

# Calculate the sum of raw counts and using .values() to get the counts from the dictionary
total_reads = sum(raw_counts.values())

# Calculate the scaling factor for CPM normalization
scaling_factor = total_reads/ 1000000

# Print the results
print(f"Total Sequencing Depth: {total_reads} reads")
print(f"Scaling Factor: {scaling_factor}")
print("--- Normalized CPM Values ---")

# Calculate and print the CPM values for each gene
for gene_name, count in raw_counts.items():

    cpm = count / scaling_factor

    print(f"Gene {gene_name}, Raw Count: {count} ---> CPM: {round(cpm, 2)}")

print("------------------------------------")
