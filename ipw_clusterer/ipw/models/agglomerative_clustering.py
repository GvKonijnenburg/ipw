import numpy as np
import pandas as pd
from sklearn import metrics
from sklearn.cluster import AgglomerativeClustering

def agglomerative_clustering(dist_matrix: np.ndarray, clusters, random_state: int = None):
    # setup results dataframe
    df_prep = []
    for n in clusters:
        df_prep.append((n, np.nan, np.nan, np.nan))  
    
    df = pd.DataFrame(df_prep, columns=['n', 'sc', 'vrc', 'dbi']) 
    
    # initialize VRC and labels
    best_vrc = 0
    best_labels = None

    for i in df.index:
        model = AgglomerativeClustering(
            n_clusters = df.loc[i, 'n'],
            metric = 'precomputed',
            linkage = 'average').fit(dist_matrix)
          
        vrc = metrics.calinski_harabasz_score(dist_matrix, model.labels_)
        if vrc > best_vrc:    
            best_vrc = vrc
            best_labels = model.labels_
        
        df.loc[i, 'sc'] = metrics.silhouette_score(dist_matrix, model.labels_, metric="precomputed")
        df.loc[i, 'vrc'] = metrics.calinski_harabasz_score(dist_matrix, model.labels_)
        df.loc[i, 'dbi'] = metrics.davies_bouldin_score(dist_matrix, model.labels_)

    return df, best_labels
