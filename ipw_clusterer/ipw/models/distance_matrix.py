import math
import numpy as np
import pandas as pd

def distance_matrix(df: pd.DataFrame) -> np.ndarray:
    n = len(df)
    returnvalue = np.zeros((n, n))

    for i in range(n):
        for j in range(i+1, n):
            vector_i = df.iloc[i]
            vector_j = df.iloc[j]
        
            similarity = np.dot(vector_i, vector_j) / (np.linalg.norm(vector_i) * np.linalg.norm(vector_j))
            similarity = max(-1.0, min(1.0, similarity)) # to remove corner cases from rounding

            distance = np.arccos(similarity) / math.pi # arrcos returns a value on interval [0 - pi]

            returnvalue[i][j] = returnvalue[j][i] = distance
    return returnvalue





