import open3d as o3d
import numpy as np
import pandas as pd

class Mapping:
    def __init__(self,points):
        self.pcd = o3d.geometry.PointCloud()
        self.pcd.points = o3d.utility.Vector3dVector(points)

    def preprocess(self):
        # Extract outliers
        print('here')
        cl, ind = self.pcd.remove_statistical_outlier(nb_neighbors=20, std_ratio=2.0)
        print(type(cl.points))
        display_inlier_outlier(cl,ind)
        return ind

def display_inlier_outlier(cloud, ind):
    print('here23')
    inlier_cloud = cloud.select_by_index(ind)
    outlier_cloud = cloud.select_by_index(ind, invert=True)

    print("Showing outliers (red) and inliers (gray): ")
    outlier_cloud.paint_uniform_color([1, 0, 0])
    inlier_cloud.paint_uniform_color([0.8, 0.8, 0.8])
    o3d.visualization.draw_geometries([inlier_cloud, outlier_cloud])
    
def main():
    pc_path = 'point_cloud_nm.csv'
    imu_path = 'imu_nm.csv'

    pc = pd.read_csv(pc_path)
    frame = pc[pc['z']<1.0]
    frame = frame[(frame['count'] >= 1) & (frame['count'] <= 5)]
    points = np.array(frame[['x', 'y', 'z']])

    map_data = Mapping(points)
    map_data.preprocess()
    
if __name__ == "__main__":
    main()
