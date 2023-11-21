import numpy as np


def DBSCAN(ds, eps, min_pts):
    """
    Cluster a dataset using DBSCAN.

    :param ds: dataset, list of points
    :param eps: threshold distance
    :param min_pts: minimum number of points per cluster
    :cluster: group of object, all teh element in this group have the same characteristic
    :return: list of cluster labels (0 to n), where 0 corresponds to noise
    """
    # Set all points to `unvisited`
    labels = [None] * len(ds)
    # First cluster id (i.e. noise)
    c = 0 
    for p in range(len(ds)):
        # Put your code here
        if labels[p] is not None: #skip if this point already visited
            continue
        nbs = regionQuery(ds, p, eps) #find all the neighrbour point inside distance eps
        
        if len(nbs) >= min_pts:
            print(f"Check: {nbs}")
            c+=1
            expandCluster(ds, labels, p, nbs, c, eps, min_pts)
        else:
            labels[p] = 'noise'
        
    print(labels)    
    return labels


def expandCluster(ds, labels, p, nbs, c, eps, min_pts):
    """
    Grows a new cluster with label `c` from seed point `p`,
    i.e. finds all points that belong to this new cluster.

    :param ds: dataset, list of points
    :param labels: list for cluster labels of dataset points
    :param p: index of seed point for new cluster
    :param nbs: neighbors of p
    :param c: label for the new cluster
    :param eps: threshold distance
    :param min_pts: minimum number of neighbors
    """
    # Put your code here
    labels[p] = c #labels the point with cluster c

    i = 0
    while i < len(nbs):
        #print(f"Check nbs: {nbs}")
        point_index  = nbs[i]
        if(point_index==-1):
            print(f"Error: This point doesn't exist") 
            continue
        
        elif labels[point_index] is None  :
            
            labels[point_index] = c
            point_nbs = regionQuery(ds, point_index, eps)
            if len(point_nbs) >= min_pts:
                nbs += point_nbs
        elif labels[point_index] == 'noise':
            labels[point_index] = c
        i+=1
            
            
    


def regionQuery(ds, q, eps):
    """
    Finds all points in dataset `ds` within distance `eps` of point `q`.
    :param nbs: neighbors of p
    :param ds: dataset
    :param q: index of point
    :param eps: threshold distance
    :return: points which are within threshold distance `eps`
    """
    nbs = []
    # Put your code here
    for i in range(len(ds)):
        if i==q:
            continue
        if np.linalg.norm(np.array(ds[q]) - np.array(ds[i])) <= eps: #if the distance between point q and i <= eps
            nbs.append(i)
    
    return(nbs)

def find_index(ds,target):
    # Find the index 
    index = next((i for i, point in enumerate(ds) if np.array_equal(point, target)), -1)
    # Print the result
    print(f"The index of {target} in ds is: {index}")
    return index
    
if __name__ == "__main__":
    #ds = [np.array([1, 2]), np.array([3, 4]), np.array([5, 6]), np.array([10,11])]
    # create ds with 10 random points
    import matplotlib.pyplot as plt

    ds = [  np.array([1, 2]), 
        np.array([3, 4]), 
        np.array([5, 6]), 
        np.array([10,11]),
        np.array([11,12]),
        np.array([10,12]),
        np.array([1, 3]),
        np.array([2, 4]),
        np.array([3, 5]),
        np.array([4, 6]),
        np.array([5, 7]),
        np.array([6, 8]),
        np.array([10,1])]

    #find_index(ds,np.array([10,11]))
    #print(regionQuery(ds,2,2))
    labels = DBSCAN(ds, 2, 2) 
    
    
   
    # Extract x and y coordinates from the data points
    x = [point[0] for point in ds]
    y = [point[1] for point in ds]

    # Find the unique cluster labels
    unique_labels = set(labels)

    # Generate a random color for each cluster
    colors = {label: np.random.rand(3,) for label in unique_labels} #RGB=3 colors

    # Plot the data points, colored by cluster
    for label in unique_labels:
        # Points in the current cluster
        cluster_points = [(x[i], y[i]) for i in range(len(labels)) if labels[i] == label]

        # Separate x and y coordinates
        cluster_x = [point[0] for point in cluster_points]
        cluster_y = [point[1] for point in cluster_points]

        # Plot the cluster points
        plt.scatter(cluster_x, cluster_y, color=colors[label], label=f'Cluster {label}')

    # Add annotations, labels, and title
    for i in range(len(ds)):
        plt.text(x[i], y[i], f'({x[i]}, {y[i]}), \nCluster:{labels[i]}', fontsize=9, ha='right')

    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Data Points by Cluster')
    plt.legend()
    plt.show()
    
       
    
