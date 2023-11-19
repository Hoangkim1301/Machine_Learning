import numpy as np


def DBSCAN(ds, eps, min_pts):
    """
    Cluster a dataset using DBSCAN.

    :param ds: dataset, list of points
    :param eps: threshold distance
    :param min_pts: minimum number of points per cluster
    :return: list of cluster labels (0 to n), where 0 corresponds to noise
    """

    # Set all points to `unvisited`
    labels = [None] * len(ds)

    # First cluster id (i.e. noise)
    c = 0

    for p in range(0, len(ds)):

        # Put your code here

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


def regionQuery(ds, q, eps):
    """
    Finds all points in dataset `ds` within distance `eps` of point `q`.
    :param ds: dataset
    :param q: index of point
    :param eps: threshold distance
    :return: points which are within threshold distance `eps`
    """

    nbs = []
    
    # Put your code here

    return nbs
