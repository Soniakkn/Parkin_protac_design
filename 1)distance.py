import os
import pandas as pd
import MDAnalysis as mda

# Define the folder containing PDB files
pdb_folder = "/path/to/directory/"
output_file = "output_file.xlsx"

# Initialize a dictionary to store results
distance_dict = {}

# Iterate over all PDB files in the folder
for pdb_file in os.listdir(pdb_folder):
    if pdb_file.endswith(".pdb"):
        pdb_path = os.path.join(pdb_folder, pdb_file)
        u = mda.Universe(pdb_path)

        # Select O atom of CYS 431 in Chain A
        cys_431 = u.select_atoms("resname CYS and resid 431 and name SG and segid A")
        if len(cys_431) == 0:
            print(f"Skipping {pdb_file}: SG atom of CYS 431 not found in Chain A")
            continue

        # Select all LYS residues in Chain C (NZ atom)
        lysines = u.select_atoms("resname LYS and name NZ and segid C")

        # Store distances in a dictionary
        distances = {}
        for lys in lysines:
            lys_resid = lys.resid
            distance = cys_431[0].position - lys.position
            distance_value = (distance**2).sum()**0.5  # Euclidean distance
            distances[f"LYS_{lys_resid}"] = distance_value

        distance_dict[pdb_file] = distances

# Convert to DataFrame
df = pd.DataFrame.from_dict(distance_dict, orient="index").fillna("NA")

# Save to Excel
df.to_excel(output_file, index=True)
print(f"Distance data saved to {output_file}")

