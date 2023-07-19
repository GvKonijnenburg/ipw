from ..plots.silhouette import silhouette
from ..plots.histogram_labels import histogram_labels

def output(dist_matrix, sc_results, sc_labels):

    print('Cluster size per cluster')
    for i in range(max(sc_labels+1)):
        print(f'Cluster {i}: {sum(sc_labels == i)}')
    print('----')
    best = sc_results[sc_results['VRC'] == max(sc_results['VRC'])]
    n = best.index[0]
    print(f'Best results at {n} clusters')
    print('----')
    print(f'Silhouette Coefficient: {best.loc[0, "SC"]:0.3f}')
    print(f'Calinski-Harabasz Index / Variance Ratio Criterion: {best.loc[0, "VRC"]:0.3f}')
    print(f'Davies-Bouldin Index: {best.loc[0, "DBI"]:0.3f}')

    histogram_labels(sc_labels)
    silhouette(dist_matrix, sc_labels)

