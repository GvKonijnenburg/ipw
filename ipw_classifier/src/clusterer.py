from typing import List
from models import Case
import numpy as np

def main(cases: List[Case], randomstate: int = None):
    n = len(cases)
   
    # create affinity matrix
    af_matrix = np.zeros((n, n))  
    for i in range(n):
        for j in range(i, n):
            af_matrix[i][j] = af_matrix[j][i] = cases[i].distance(cases[j])



    
