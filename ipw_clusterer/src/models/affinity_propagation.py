import numpy as np
import pandas as pd
from sklearn import metrics
from sklearn.cluster import AffinityPropagation

def affinity_propagation(distance_matrix: np.ndarray, dampings: np.ndarray, random_state: int = None):
    # setup results dataframe
    df = pd.DataFrame(index = dampings, columns=['Clusters', 'SC', 'VRC', 'DBI']) 

    # initialize VRC and labels
    best_VRC = 0
    best_labels = None
    centers = None

    # run clustering model
    for damping in df.index:
        model = AffinityPropagation(
            damping = damping,
            max_iter = 500,
            affinity = 'precomputed',
            verbose = False,
            random_state = random_state).fit(distance_matrix)
        
        n = len(model.cluster_centers_indices_)
        df.loc[damping]['Clusters'] = n
        
        if n > 1:
            VRC = metrics.calinski_harabasz_score(distance_matrix, model.labels_)
            if VRC > best_VRC:
                best_VRC = VRC
                best_labels = model.labels_
                centers = model.cluster_centers_indices_
    
            df.loc[damping]['SC'] = metrics.silhouette_score(distance_matrix, model.labels_, metric="precomputed")
            df.loc[damping]['VRC'] = metrics.calinski_harabasz_score(distance_matrix, model.labels_)
            df.loc[damping]['DBI'] = metrics.davies_bouldin_score(distance_matrix, model.labels_)

    return df, best_labels, centers
