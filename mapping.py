import open3d as o3d
import numpy as np
import pandas as pd

class Mapping:
    def __init__(self,points):
        self.pcd = o3d.geometry.PointCloud()
        self.pcd.points = o3d.utility.Vector3dVector(points)

    def preprocess(self, neighbors=10, std_ratio=2.0):
        # Extract outliers
        if len(self.pcd.points) == 0:
            print("Point cloud is empty. Skipping preprocessing.")
            return []
        cl, ind = self.pcd.remove_statistical_outlier(neighbors, std_ratio)
        if len(ind) == 0:
            print("No inliers found. Skipping visualization.")
            return ind
        display_inlier_outlier(cl,ind)
        return ind

def display_inlier_outlier(cloud, ind):
    print('inlier')
    print(len(ind))
    inlier_cloud = cloud.select_by_index(ind)
    print('outlier')
    outlier_cloud = cloud.select_by_index(ind, invert=True)

    print("Showing outliers (red) and inliers (gray): ")
    outlier_cloud.paint_uniform_color([1, 0, 0])
    inlier_cloud.paint_uniform_color([0.8, 0.8, 0.8])
    print('visualize')
    o3d.visualization.draw([inlier_cloud, outlier_cloud])
    return
        
def main():
    pc_path = 'point_cloud_nm.csv'
    imu_path = 'imu_nm.csv'
    pc = pd.read_csv(pc_path)
    frame = pc[pc['z']<1.0]
    frame = frame[(frame['count'] ==1)]
    frame =  frame[frame['z']<1.0] # set ceiling bound    
    points = np.array(frame[['x', 'y', 'z']])
    print(points.shape)
    map_data = Mapping(points)
    map_data.preprocess()
    
if __name__ == "__main__":
    main()
