from enum import auto, Enum

class Model(Enum):
    AFFINITY_PROPAGATION = auto()
    AGGLOMERATIVE_CLUSTERING = auto()
    DBSCAN = auto()
    SPECTRAL_CLUSTERING = auto()

    def col(self, n):
        if self == Model.AFFINITY_PROPAGATION: 
            return f'af_labels{n}'
        elif self == Model.AGGLOMERATIVE_CLUSTERING:
            return f'ac_labels{n}'
        elif self == Model.DBSCAN:
            return f'db_labels{n}'
        elif self == Model.SPECTRAL_CLUSTERING:
            return f'sc_labels{n}'
        else:
            raise ValueError(f'Unknown model enum: {self.value}')