import math
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np
from matplotlib.ticker import MaxNLocator  
from sklearn import metrics

def silhouette(dist_matrix, labels):
    n_clusters = labels.max() + 1
    # Compute the silhouette scores for each sample
    sample_silhouette_values = metrics.silhouette_samples(dist_matrix, labels, metric = 'precomputed')
    min_sil = math.floor(min(sample_silhouette_values) / 0.2) * 0.2
    max_sil = max(sample_silhouette_values)

    fig, ax = plt.subplots(1, 1)
    fig.set_size_inches(18, 7)

    ax.set_xlim([min_sil, 1])
    # The (n_clusters+1)*10 is for inserting blank space between silhouette plots of individual clusters,
    # to demarcate them clearly.    
    ax.set_ylim([0, len(labels) + (n_clusters + 1) * 10])

    # The silhouette_score gives the average value for all the samples.
    # This gives a perspective into the density and separation of the formed
    # clusters
    silhouette_avg = metrics.silhouette_score(dist_matrix, labels, metric = 'precomputed')

    y_lower = 10
    for i in range(n_clusters):
        # Aggregate the silhouette scores for samples belonging to
        # cluster i, and sort them
        ith_cluster_silhouette_values = sample_silhouette_values[labels == i]

        ith_cluster_silhouette_values.sort()

        size_cluster_i = ith_cluster_silhouette_values.shape[0]
        y_upper = y_lower + size_cluster_i

        color = cm.nipy_spectral(float(i) / n_clusters)
        ax.fill_betweenx(
            np.arange(y_lower, y_upper),
            0,
            ith_cluster_silhouette_values,
            facecolor=color,
            edgecolor=color,
            alpha=0.7,
        )

        # Label the silhouette plots with their cluster numbers at the middle
        ax.text(min_sil, y_lower + 0.5 * size_cluster_i, str(i))

        # Compute the new y_lower for next plot
        y_lower = y_upper + 10  # 10 for the 0 samples

        ax.set_title("Silhouette plot for each cluster")
        ax.set_xlabel("Silhouette coefficient")
        ax.set_ylabel("Cluster label")

        # The vertical line for average silhouette score of all the values
        ax.axvline(x=silhouette_avg, color="red", linestyle="--")

        ax.set_yticks([])  # Clear the yaxis labels / ticks
        xticks = np.arange(min_sil, 1.1, 0.2)  
        ax.set_xticks(xticks)