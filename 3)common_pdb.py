import pandas as pd
import re

# Load the Excel file
file_path = "filtered_pdbs.xlsx"  # Update the path if needed
xls = pd.ExcelFile(file_path)
df = pd.read_excel(xls, sheet_name="Sheet1")

# Function to extract PDB names and distances (retain values in parentheses)
def extract_pdb_info(entry):
    if isinstance(entry, str):
        match = re.match(r"(\S+)\s*(\(.*?\))?", entry)
        if match:
            pdb_name = match.group(1)
            distance = match.group(2) if match.group(2) else ""
            return pdb_name, distance
    return None, None

# Apply extraction function to all dataframe values
df_extracted = df.applymap(lambda x: extract_pdb_info(x)[0])
df_distances = df.applymap(lambda x: extract_pdb_info(x)[1])

# Count occurrences of each PDB across lysine columns
pdb_counts = df_extracted.stack().value_counts()

# Set threshold for common PDBs (e.g., appearing in at least 70% of the lysine columns)
threshold = int(len(df_extracted.columns) * 0.3)
common_pdbs = pdb_counts[pdb_counts >= threshold]

# Create a dictionary mapping common PDBs to their corresponding lysines with distances
common_pdbs_dict = {}
for pdb in common_pdbs.index:
    lysine_entries = []
    for col in df_extracted.columns:
        if pdb in df_extracted[col].values:
            distances = df_distances[col][df_extracted[col] == pdb].dropna().tolist()
            lysine_entries.append(f"{col} {' '.join(distances)}")
    common_pdbs_dict[pdb] = ", ".join(lysine_entries)

# Convert to DataFrame and save to an Excel file
common_pdbs_df = pd.DataFrame(list(common_pdbs_dict.items()), columns=["PDB", "Lysines & Distances"])
common_pdbs_df.to_excel("common_pdbs.xlsx", index=False)

# Display common PDBs
print("Common PDBs saved to common_pdbs.xlsx")

