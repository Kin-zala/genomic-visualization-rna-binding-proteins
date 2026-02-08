# Genomic Visualization of RNA Binding Protein Signals

This repository contains a visualization project focused on recreating genomic signal plots for fictitious RNA binding protein (RBP) data alongside genomic annotations.  
The project demonstrates the use of Python-based data visualization tools to represent multi-track genomic signals and transcript structures.

## 📊 Project Overview

The goal of this exercise is to recreate example figures showing:

- Signal intensities of four RNA binding proteins (P1–P4)
- Genomic annotations including transcripts, exons, and DNA strand orientation
- Coordinated visualization using shared genomic coordinates

All visualizations are implemented in a Jupyter notebook using Python.

## 🧬 Data Description

### 1. Genomic Annotations
**File:** `10_project_data_annotations.csv`

- Contains fictitious transcript information
- Each transcript consists of one or more exons
- Transcripts are located on either the '+' or '-' DNA strand
- Used for the bottom annotation panel in the visualization

### 2. RNA Binding Protein Signals
**File:** `10_project_data_signals.csv`

- Contains artificial signal intensity values
- Four RNA binding proteins: P1, P2, P3, and P4
- Values are plotted across genomic positions

## 🛠️ Tools & Libraries Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Jupyter Notebook

## 📁 Repository Structure

```text
├── data/        # Input CSV files
├── notebooks/   # Jupyter notebook with visualization code
├── figures/     # Exported plots (PNG)
├── exports/     # HTML version of the notebook
├── README.md
└── requirements.txt'''


1.1. Version A

![image-alt](https://github.com/Kin-zala/data-visualization-bioinformatics/blob/b20c3a19f060d32a2b914a4040d2e03b5d684eb1/1.1%20Version_1.png)
