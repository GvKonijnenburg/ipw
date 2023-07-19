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
    
    df = pd.DataFrame(df_prep, columns=['eps', 'min_samples', 'Clusters', 'SC', 'VRC', 'DBI']) 

    # initialize VRC and labels
    best_VRC = 0
    best_labels = None

    # run clustering model
    for i in df.index:
        model = DBSCAN(
            eps = df.loc[i]['eps'],
            min_samples = int(df.loc[i]['min_samples']),
            metric = 'precomputed').fit(dist_matrix)
        
        n = max(model.labels_) + 1
        df.loc[i, 'Clusters'] = n
        
        if n > 1:
            VRC = metrics.calinski_harabasz_score(dist_matrix, model.labels_)
            if VRC > best_VRC:
                best_VRC = VRC
                best_labels = model.labels_
    
            df.loc[i, 'SC'] = metrics.silhouette_score(dist_matrix, model.labels_, metric="precomputed")
            df.loc[i, 'VRC'] = metrics.calinski_harabasz_score(dist_matrix, model.labels_)
            df.loc[i, 'DBI'] = metrics.davies_bouldin_score(dist_matrix, model.labels_)

    return df, best_labels