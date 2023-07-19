import numpy as np
import pandas as pd
from sklearn import metrics
from sklearn.cluster import AffinityPropagation

def affinity_propagation(distance_matrix: np.ndarray, dampings: np.ndarray, random_state: int = None):
    # setup results dataframe
    df_prep = []
    for damping in dampings:
        df_prep.append((damping, np.nan, np.nan, np.nan, np.nan))  
    
    df = pd.DataFrame(df_prep, columns=['damping', 'n', 'sc', 'vrc', 'dbi']) 
    
    # initialize VRC and labels
    best_vrc = 0
    best_labels = None
    centers = None

    # run clustering model
    for i in df.index:
        model = AffinityPropagation(
            damping = df.loc[i, 'damping'],
            max_iter = 500,
            affinity = 'precomputed',
            verbose = False,
            random_state = random_state).fit(distance_matrix)
        
        n = len(model.cluster_centers_indices_)
        df.loc[i, 'n'] = n
        
        if n > 1:
            vrc = metrics.calinski_harabasz_score(distance_matrix, model.labels_)
            if vrc > best_vrc:
                best_vrc = vrc
                best_labels = model.labels_
                centers = model.cluster_centers_indices_
    
            df.loc[i, 'sc'] = metrics.silhouette_score(distance_matrix, model.labels_, metric="precomputed")
            df.loc[i, 'vrc'] = metrics.calinski_harabasz_score(distance_matrix, model.labels_)
            df.loc[i, 'dbi'] = metrics.davies_bouldin_score(distance_matrix, model.labels_)

    return df, best_labels, centers
