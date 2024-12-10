import numpy as np
import math
from sklearn.cluster import DBSCAN

from utils import *
from constants import *


class Feature_Extraction:
    def __init__(self, epsilon, min_samples):
        self.epsilon = epsilon
        self.min_samples = min_samples
        self.pointCloud = None

    def cluster_datapoints(self):
        data_points = np.array(self.pointCloud)

        dbscan = DBSCAN(eps=self.epsilon, min_samples=self.min_samples)
        labels = dbscan.fit_predict(data_points)

        return labels
    
    def extract_features(self):
        labels = self.cluster_datapoints()
        clusters = set(labels)
        return labels, clusters



