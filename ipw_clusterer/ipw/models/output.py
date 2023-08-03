import numpy as np

def output(dist_matrix, results, labels):
    print('Cluster size per cluster')
    for i in range(min(labels), max(labels+1)):
        print(f'Cluster {i}: {sum(labels == i)}')
    print('----')
    best = results[results['sc'] == np.nanmax(results['sc'])]
    n = best.index[0]
    print('Best result:')
    print('----')
    for column in best:
        if column == 'damping': # for Affinity Propagation
            print(f'Affinity Propagation damping Factor: {best.iloc[0][column]}')
        elif column == 'eps': # for DBScan
            print(f'DBScan epsilon: {best.iloc[0][column]}')
        elif column == 'min_samples': # for DBScan
            print(f'DBScan Weight for core points: {best.iloc[0][column]}')
        elif column == 'n':
            print(f'Number of clusters: {best.iloc[0][column]}')
        elif column == 'sc':
            print(f'Silhouette Coefficient: {best.iloc[0][column]:0.3f}')
        elif column == 'vrc':
            print(f'Calinski-Harabasz Index / Variance Ratio Criterion: {best.iloc[0][column]:0.3f}')
        elif column == 'dbi':
            print(f'Davies-Bouldin Index: {best.iloc[0][column]:0.3f}')

