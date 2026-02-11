# Genomic Visualization of RNA Binding Proteins

This repository contains exercises and code for visualizing **RNA binding protein signals** alongside **genomic annotations**. The goal is to recreate three types of visualizations using **Python, Matplotlib, and Seaborn**.

## Repository Structure

- `Data/` – Contains CSV files with artificial datasets:
  - `10_project_data_annotations.csv`: Genomic annotations including transcripts and exons.
  - `10_project_data_signals.csv`: Signals for four RNA binding proteins (P1, P2, P3, P4).

- `Plot_Images/` – Optional folder for saving example output plots.

- `Scripts/` – Optional standalone Python scripts for each version:
  - `plot_version_a.py`, `plot_version_b.py`, `plot_version_c.py`

- `Visualization_Exercise_1.ipynb` – Complete code for Version A, B, and C visualizations with explanations.

- `Requirements.txt` - text for requirement list for this exercise.

## Exercises Overview

1. **Version A**: Individual line plots for each protein with genomic annotations below.  
2. **Version B**: Heatmap representation of protein signals with annotations below.  
3. **Version C**: Colored overlay line plots for all proteins with annotations below.  

## Libraries Used

- Python 3.x
- `pandas`, `numpy`, `matplotlib`, `seaborn`

## How to Use

1. Clone the repository:
```bash
git clone https://github.com/Kin-zala/genomic-visualization-rna-binding-proteins.git
```
2. Open the Jupyter notebook in notebooks/ and run the cells.

3. Alternatively, run the Python scripts in scripts/ to generate individual visualizations.

## The output
![image-alt](https://github.com/Kin-zala/genomic-visualization-rna-binding-proteins/blob/fbed4dbc5ba7cd6628edde082c0cb2427b9cf107/Version_A_visualization.png)

### 1.2 Version B
![image-alt](https://github.com/Kin-zala/genomic-visualization-rna-binding-proteins/blob/fbed4dbc5ba7cd6628edde082c0cb2427b9cf107/Version_B_visualization.png)

### 1.3 Version C
![image-alt](https://github.com/Kin-zala/genomic-visualization-rna-binding-proteins/blob/fbed4dbc5ba7cd6628edde082c0cb2427b9cf107/Version_C_visualization.png)
