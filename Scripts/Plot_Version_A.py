import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib as mpl
import pandas as pd
import seaborn as sns
import numpy as np

#load the dataframe
df1 = pd.read_csv("Data\\10_project_data_annotation.csv")
df2 = pd.read_csv("Data\\10_project_data_signals.csv")


# Create subplots: One for each column in df2 plus an additional one for annotations
fig, axs = plt.subplots(nrows=len(df2.columns) + 1, figsize=(18, 9), sharex=True)
fig.subplots_adjust(hspace=0)  # Adjust subplot spacing
xlim = [0, 20000]  # Define the x-axis limit


# Iterate over each column in df2 and create a plot
i = 0
for col in df2.columns:
    df2[col].plot(ax=axs[i], color='#505050')  # Plot the column data
    axs[i].set_xlim(xlim)  # Set x-axis limit
    axs[i].set_ylim(0, 1.3)  # Set y-axis limit
    axs[i].set_yticks([0, 0.5, 1])  # Set y-axis ticks
    axs[i].set_ylabel(col)  # Set y-axis label to the column name
    axs[i].xaxis.grid(True)  # Add grid to the x-axis
    i += 1  # Move to the next subplot


# Code to plot annotations
axs[-1].set_xlabel('Genomic position', fontsize=10)  # Set x-axis label for the last subplot
axs[-1].set_ylabel('Annotations', fontsize=10)  # Set y-axis label for the last subplot
axs[-1].set_ylim(-0.5, 1.5)  # Set y-axis limit for the last subplot
axs[-1].set_yticks([0, 1])  # Set y-axis ticks for the last subplot
axs[-1].set_yticklabels(['−', '+'])  # Set y-axis tick labels for the last subplot
axs[-1].xaxis.grid(True)  # Add grid to the x-axis



# Plot the annotations from df1 on the last subplot
for _, r in df1.iterrows():
    marker = '|'  # Default marker for annotations
    lw = 1  # Default line width
    if r['type'] == 'exon':  # If the annotation type is exon
        marker = None  # No marker for exon
        lw = 8  # Wider line width for exon
    y = 1 if r['strand'] == '+' else 0  # Set y position based on strand
    axs[-1].plot((r['start'], r['stop']), (y, y),
                 marker=marker, lw=lw,
                 solid_capstyle='butt',
                 color='#505050')  # Plot the annotation


plt.show()  # Display the plot