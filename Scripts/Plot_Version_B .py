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
fig, axs = plt.subplots(2, 1, figsize=(18, 5), sharex=True)
fig.subplots_adjust(hspace=0)  # Adjust the vertical spacing between subplots to zero
xlim = [0, 20000]  # Define the x-axis limit

# Stack the data from df2 columns into a 2D array
data = np.vstack([df2['P1'], df2['P2'], df2['P3'], df2['P4']])

# Create the heatmap on the first subplot
sns.heatmap(data, cmap='Greys', cbar=False, yticklabels=['P1', 'P2', 'P3', 'P4'], ax=axs[0])
axs[0].xaxis.grid(True, linestyle = 'dotted', linewidth=2)  # Add grid to the x-axis of the first subplot with dotted linestyle
# Add solid outline for heatmap
axs[0].spines['top'].set_visible(True)
axs[0].spines['right'].set_visible(True)
axs[0].spines['left'].set_visible(True)
axs[0].spines['bottom'].set_visible(True)


# Set x-axis ticks for both subplots
xticks = np.arange(0, 20001, 2500)
axs[0].set_xticks(xticks)
axs[1].set_xticks(xticks)

# Set x-axis limit and labels for the second subplot
axs[1].set_xlim(xlim)
axs[1].set_xlabel('Genomic position', fontsize=10)
axs[1].set_ylabel('Annotations', fontsize=10)
axs[1].set_ylim(-0.5, 1.5)  # Set y-axis limit for the second subplot
axs[1].set_yticks([0, 1])  # Set y-axis ticks for the second subplot
axs[1].set_yticklabels(['−', '+'])  # Set y-axis tick labels for the second subplot
axs[1].xaxis.grid(True, linestyle = 'dotted', linewidth=2)  # Add grid to the x-axis of the second subplot with dotted linestyle

# Plot the annotations from df1 on the second subplot
for _, r in df1.iterrows():
    marker = '|'  # Default marker for annotations
    markersize = 10  # Marker size
    lw = 2  # Default line width
    if r['type'] == 'exon':  # If the annotation type is exon
        marker = None  # No marker for exon
        lw = 15  # Wider line width for exon
    y = 1 if r['strand'] == '+' else 0  # Set y position based on strand
    axs[1].plot((r['start'], r['stop']), (y, y),
                marker=marker, lw=lw,
                solid_capstyle='butt',
                color='#505050')  # Plot the annotation

# Display the plot
plt.show()