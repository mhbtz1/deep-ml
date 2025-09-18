import numpy as np

def k_means_clustering(points: list[tuple[float, float]], k: float, initial_centroids: list[tuple[float, float]], max_iterations: int) -> list[tuple[float, float]]:
    points = np.array(points, dtype=np.float32)
    centroids = np.array(initial_centroids, dtype=np.float32)

    for i in range(max_iterations):
        asgn_centroids = np.array([np.argmin(np.linalg.norm(points[j, :] - centroids, axis=1)) for j in range(points.shape[0])])
        for j in range(len(centroids)):
            subpoints = points[np.where(asgn_centroids == j)]
            new_centroid = np.mean(subpoints, axis=0)
            centroids[j] = new_centroid
    
    return centroids