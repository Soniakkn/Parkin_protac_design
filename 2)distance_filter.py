import os
import pandas as pd

# Define the folder containing Excel files
excel_folder = "/path/to/directory/"
output_file = "filtered_pdbs.xlsx"

# Initialize a dictionary to store PDB IDs for each lysine
lysine_dict = {}

# Iterate over all Excel files in the folder
for excel_file in os.listdir(excel_folder):
    if excel_file.endswith(".xlsx"):
        file_path = os.path.join(excel_folder, excel_file)
        df = pd.read_excel(file_path, index_col=0)  # Load Excel file
        
        # Iterate over each PDB file (row) in the DataFrame
        for pdb_id, row in df.iterrows():
            for lysine, distance in row.items():
                if isinstance(distance, (int, float)) and distance < 20: #distance cut off can be changed 
                    if lysine not in lysine_dict:
                        lysine_dict[lysine] = []
                    lysine_dict[lysine].append(f"{pdb_id} ({distance:.2f})")

# Convert the dictionary to a DataFrame
max_rows = max(len(v) for v in lysine_dict.values())  # Find the maximum column height
output_df = pd.DataFrame({key: value + [""] * (max_rows - len(value)) for key, value in lysine_dict.items()})

# Save the output to an Excel file
output_df.to_excel(output_file, index=False)
print(f"Filtered data saved to {output_file}")
