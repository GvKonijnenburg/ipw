import numpy as np
import pandas as pd
from sklearn import metrics
from sklearn.cluster import DBSCAN

def dbscan(dist_matrix: np.ndarray, eps_arr, min_samples_arr, random_state: int = None):
    # setup results dataframe
    df_prep = []
    for eps in eps_arr:
        for min_samples in min_samples_arr:
            df_prep.append((eps, min_samples, 0, 0, 0, 0))    
    
    df = pd.DataFrame(df_prep, columns=['eps', 'min_samples', 'n', 'sc', 'vrc', 'dbi']) 

    # initialize VRC and labels
    best_vrc = 0
    best_labels = None

    # run clustering model
    for i in df.index:
        model = DBSCAN(
            eps = df.loc[i, 'eps'],
            min_samples = int(df.loc[i, 'min_samples']),
            metric = 'precomputed').fit(dist_matrix)
        
        n = max(model.labels_) + 1
        df.loc[i, 'n'] = n
        
        if n > 1:
            vrc = metrics.calinski_harabasz_score(dist_matrix, model.labels_)
            if vrc > best_vrc:
                best_vrc = vrc
                best_labels = model.labels_
    
            df.loc[i, 'sc'] = metrics.silhouette_score(dist_matrix, model.labels_, metric="precomputed")
            df.loc[i, 'vrc'] = metrics.calinski_harabasz_score(dist_matrix, model.labels_)
            df.loc[i, 'dbi'] = metrics.davies_bouldin_score(dist_matrix, model.labels_)

    return df, best_labels