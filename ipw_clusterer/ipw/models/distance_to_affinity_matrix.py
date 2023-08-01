import math
import numpy as np

def distance_to_affinity_matrix(dist_matrix):
    return np.cos(dist_matrix * math.pi * 0.5)
