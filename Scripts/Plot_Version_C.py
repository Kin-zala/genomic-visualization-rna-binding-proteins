import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib as mpl
import pandas as pd
import seaborn as sns
import numpy as np

#load the dataframe
df1 = pd.read_csv("Data\\10_project_data_annotation.csv")
df2 = pd.read_csv("Data\\10_project_data_signals.csv")


# Create a figure with two subplots vertically aligned
fig, (ax1, ax2) = plt.subplots(nrows=2, figsize=(18, 7), sharex=True)  # Use unpacking for 2 subplots

fig.subplots_adjust(hspace=0)  # Adjust the vertical spacing between subplots to zero
xlim = [0, 20000]  # Define the x-axis limit

# Define a color list for P1-P4
colors = ['#06C2AC', '#9A0EEA', '#FFD700', '#929591']  # Custom colors for each column

# Plot each column with its corresponding color
for i, col in enumerate(df2.columns):
    if col in ['P1', 'P2', 'P3', 'P4']:
        ax1.plot(df2[col], color=colors[i], label=col)  # Plot P1-P4 with custom colors and labels
    else:
        ax1.plot(df2[col], color='#aaaaaa')  # Plot other columns with a default color

# Set the properties for the first subplot (ax1)
ax1.set_xlim(xlim)  # Set the x-axis limit
ax1.set_ylim(0, 1.3)  # Set the y-axis limit
ax1.set_yticks([0, 0.5, 1])  # Set y-axis ticks
ax1.set_ylabel('Values', fontsize=10)  # Set y-axis label
ax1.xaxis.grid(True, linestyle='dotted', linewidth=2)  # Add a dotted grid to the x-axis
ax1.legend(loc="upper left")  # Add a legend for P1-P4 in the upper left corner

# Set the properties for the second subplot (ax2)
ax2.set_xlabel('Genomic position', fontsize=10)  # Set x-axis label
ax2.set_ylabel('Annotations', fontsize=10)  # Set y-axis label
ax2.set_ylim(-0.5, 1.5)  # Set the y-axis limit
ax2.set_yticks([0, 1])  # Set y-axis ticks
ax2.set_yticklabels(['−', '+'])  # Set y-axis tick labels
ax2.xaxis.grid(True, linestyle='dotted', linewidth=2)  # Add a dotted grid to the x-axis

# Plot the annotations from df1 on the second subplot (ax2)
for _, r in df1.iterrows():
    marker = '|'  # Default marker for annotations
    markersize = 10  # Marker size
    lw = 2  # Default line width
    if r['type'] == 'exon':  # If the annotation type is exon
        marker = None  # No marker for exon
        lw = 15  # Wider line width for exon
    y = 1 if r['strand'] == '+' else 0  # Set y position based on strand
    ax2.plot((r['start'], r['stop']), (y, y),
             marker=marker, lw=lw,
             solid_capstyle='butt',
             color='#505050')  # Plot the annotation

# Display the plot
plt.show()