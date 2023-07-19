import numpy as np
import pandas as pd
from sklearn import metrics
from sklearn.cluster import SpectralClustering

def spectral_clustering(dist_matrix: np.ndarray, clusters, random_state: int = None):
    aff_matrix = 2 - dist_matrix
    
    # setup results dataframe
    df = pd.DataFrame(index = clusters, columns=['SC', 'VRC', 'DBI']) 

    # initialize VRC and labels
    best_VRC = 0
    best_labels = None

    for n in df.index:
        model = SpectralClustering(
            n_clusters = n,
            random_state = random_state, 
            affinity = 'precomputed',
            verbose = False,
            assign_labels='discretize').fit(aff_matrix)
            
        VRC = metrics.calinski_harabasz_score(dist_matrix, model.labels_)
        if VRC > best_VRC:    
            best_VRC = VRC
            best_labels = model.labels_
        
        df.loc[n]['SC'] = metrics.silhouette_score(dist_matrix, model.labels_, metric="precomputed")
        df.loc[n]['VRC'] = metrics.calinski_harabasz_score(dist_matrix, model.labels_)
        df.loc[n]['DBI'] = metrics.davies_bouldin_score(dist_matrix, model.labels_)

    return df, best_labels
