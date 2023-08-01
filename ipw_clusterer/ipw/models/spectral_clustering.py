from .distance_to_affinity_matrix import distance_to_affinity_matrix
import numpy as np
import pandas as pd
from sklearn import metrics
from sklearn.cluster import SpectralClustering

def spectral_clustering(dist_matrix: np.ndarray, clusters, random_state: int = None):
    aff_matrix = distance_to_affinity_matrix(dist_matrix)
        
    # setup results dataframe
    df_prep = []
    for n in clusters:
        df_prep.append((n, np.nan, np.nan, np.nan))  
    
    df = pd.DataFrame(df_prep, columns=['n', 'sc', 'vrc', 'dbi']) 

    # initialize VRC and labels
    best_vrc = 0
    best_labels = None

    for i in df.index:
        model = SpectralClustering(
            n_clusters = df.loc[i, 'n'],
            random_state = random_state, 
            affinity = 'precomputed',
            verbose = False,
            assign_labels='discretize').fit(aff_matrix)
            
        VRC = metrics.calinski_harabasz_score(dist_matrix, model.labels_)
        if VRC > best_vrc:    
            best_vrc = VRC
            best_labels = model.labels_
        
        df.loc[i, 'sc'] = metrics.silhouette_score(dist_matrix, model.labels_, metric="precomputed")
        df.loc[i, 'vrc'] = metrics.calinski_harabasz_score(dist_matrix, model.labels_)
        df.loc[i, 'dbi'] = metrics.davies_bouldin_score(dist_matrix, model.labels_)

    return df, best_labels
