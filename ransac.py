import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import open3d as o3d

class RANSAC:
    """
    RANSAC Class
    """
    def __init__(self, point_cloud, max_iterations,            
                 distance_ratio_threshold):
        self.point_cloud = point_cloud
        self.max_iterations = max_iterations
        self.distance_ratio_threshold = distance_ratio_threshold
