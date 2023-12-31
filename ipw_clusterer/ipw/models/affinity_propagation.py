import math
import numpy as np
import pandas as pd
from sklearn import metrics
from sklearn.cluster import AffinityPropagation
from .distance_to_affinity_matrix import distance_to_affinity_matrix

def affinity_propagation(dist_matrix: np.ndarray, dampings: np.ndarray, random_state: int = None):
    aff_matrix = distance_to_affinity_matrix(dist_matrix)

    # setup results dataframe
    df_prep = []
    for damping in dampings:
        df_prep.append((damping, np.nan, np.nan, np.nan, np.nan))  
    
    df = pd.DataFrame(df_prep, columns=['damping', 'n', 'sc', 'vrc', 'dbi']) 
    
    # initialize VRC and labels
    best_sc = 0
    best_labels = None
    centers = None

    # run clustering model
    for i in df.index:
        model = AffinityPropagation(
            damping = df.loc[i, 'damping'],
            max_iter = 500,
            affinity = 'precomputed',
            verbose = False,
            random_state = random_state).fit(aff_matrix)
        
        n = len(model.cluster_centers_indices_)
        df.loc[i, 'n'] = n
        
        if n > 1:
            sc =metrics.silhouette_score(dist_matrix, model.labels_, metric="precomputed")
            if sc > best_sc:
                best_sc = sc
                best_labels = model.labels_
                centers = model.cluster_centers_indices_
    
            df.loc[i, 'sc'] = metrics.silhouette_score(dist_matrix, model.labels_, metric="precomputed")
            df.loc[i, 'vrc'] = metrics.calinski_harabasz_score(dist_matrix, model.labels_)
            df.loc[i, 'dbi'] = metrics.davies_bouldin_score(dist_matrix, model.labels_)

    return df, best_labels, centers
