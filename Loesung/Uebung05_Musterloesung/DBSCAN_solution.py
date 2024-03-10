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

        # If point was visited already, continue
        if not (labels[p] is None):
            continue

        # Find all neighboring points
        nbs = regionQuery(ds, p, eps)

        # Set to noise, if number of neighbors is below min_pts
        if len(nbs) < min_pts:
            labels[p] = 0

        # Otherwise, point is a seed for a new cluster
        else:
            c += 1 # Next cluster id
            expandCluster(ds, labels, p, nbs, c, eps, min_pts)

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

    labels[p] = c

    i = 0
    while i < len(nbs):

        next_p = nbs[i]

        # If next_p is labeled 0 (noise) earlier, it is not a branch point
        if labels[next_p] == 0:
            labels[next_p] = c

        # Otherwise, if next_p isn't already assigned, add it to cluster c
        elif labels[next_p] == None:
            labels[next_p] = c

            # Find all the neighbors of next_p
            next_p_nbs = regionQuery(ds, next_p, eps)

            # If next_p has at least min_pts neighbors, it's a branch point
            # Add all of its neighbors to the list of neighbors.
            if len(next_p_nbs) >= min_pts:
                nbs += next_p_nbs

        # Otherwise, next_p doesn't have enough neighbors, it's a leaf point
        i += 1


def regionQuery(ds, q, eps):
    """
    Finds all points in dataset `ds` within distance `eps` of point `q`.
    :param ds: dataset
    :param q: index of point
    :param eps: threshold distance
    :return: points which are within threshold distance `eps`
    """

    nbs = []

    for p in range(0, len(ds)):
        if np.linalg.norm(ds[q] - ds[p]) < eps:
            nbs += [ p ]

    return nbs
