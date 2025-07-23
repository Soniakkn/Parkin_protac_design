# Parkin PROTAC Ternary Complex Analysis

This repository contains three Python scripts designed to assist in the selection of suitable ternary complexes involving the Parkin E3 ligase. These tools evaluate the spatial proximity between the **catalytic cysteine** of Parkin and the **lysine residues** of the Protein of Interest (POI), helping assess the feasibility of **ubiquitin transfer**.

---

## Scripts Overview

### 1. `distance.py`
- **Purpose**: Calculates the distances between the **catalytic cysteine** (Cys431) of Parkin and **all lysine residues** in the POI for each ternary complex.
- **Usage**: Helps understand which lysines are accessible from the catalytic site.

---

### 2. `distance_filter.py`
- **Purpose**: Filters and identifies **active lysine residues** that lie within a user-defined cutoff distance (e.g., = 20 Å) from the catalytic cysteine.
- **Usage**: Helps shortlist lysines potentially capable of accepting ubiquitin based on spatial proximity.

---

### 3. `common_pdb.py`
- **Purpose**: Reports how many lysine residues lie within the cutoff distance in **each ternary complex**.
- **Usage**: Useful for ranking or selecting ternary complexes based on the number of accessible lysines.

---

## Application

These scripts are intended to:
- Support structure-based design of Parkin-based PROTACs.
- Aid in **ternary complex evaluation** for ubiquitin accessibility.
- Guide **rational PROTAC design** targeting lysine residues near Parkin's catalytic cysteine.