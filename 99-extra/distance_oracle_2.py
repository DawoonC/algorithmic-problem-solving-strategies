#  
# This is the same problem as "Distance Oracle I" except that instead of
# only having to deal with binary trees, the assignment asks you to
# create labels for all tree graphs.
#
# In the shortest-path oracle described in Andrew Goldberg's
# interview, each node has a label, which is a list of some other
# nodes in the network and their distance to these nodes.  These lists
# have the property that
#
#  (1) for any pair of nodes (x,y) in the network, their lists will
#  have at least one node z in common
#
#  (2) the shortest path from x to y will go through z.
# 
# Given a graph G that is a tree, preprocess the graph to
# create such labels for each node.  Note that the size of the list in
# each label should not be larger than log n for a graph of size n.
#

#
# create_labels takes in a tree and returns a dictionary, mapping each
# node to its label
#
# a label is a dictionary mapping another node and the distance to
# that node
#
import math


def create_labels(treeG):
    treeG_copy = treeG.copy()
    labels = create_logn_labels(treeG_copy)
    return labels


def create_logn_labels(treeG):
    """ returns log n sized labels """
    labels = get_min_labels(treeG)
    if get_label_size(labels) <= math.ceil(math.log(len(treeG), 2)+1):
        return labels
    
    sub_labels = {}
    center = None
    leaves = []
    leaf_tracker = get_label_size(labels)-1
    for l in labels:
        if len(labels[l]) == 1:
            center = l
        if len(labels[l]) >= leaf_tracker:
            leaves.append(l)
            
    for e in treeG.keys():
        if e not in sub_labels:
            sub_labels[e] = {}
        sub_labels[e].update({center: labels[e][center]})
            
    for leaf in leaves:
        sub_tree = split_graph(treeG, leaf, center)
        sub_sub_labels = create_logn_labels(sub_tree)
        for j in sub_labels.keys():
            if j in sub_sub_labels:
                sub_labels[j].update(sub_sub_labels[j])
    return sub_labels


def split_graph(treeG, leaf, root):
    """ split the graph into half and returns new half graph """
    treeG_copy = treeG.copy()
    g = {}
    open_list = [leaf]
    while open_list:
        for neighbor in treeG[open_list[0]]:
            if neighbor not in g:
                if neighbor != root:
                    if neighbor in treeG_copy:
                        g[neighbor] = treeG_copy.pop(neighbor)
                        open_list.append(neighbor)
            treeG_copy = treeG.copy()
        del open_list[0]
    return g


def get_min_labels(treeG):
    """ 
    returns labels with minimum labels size from current graph size
    this method does not guarantee log n size labels
    labels could be log n size if the graph is balanced binary tree graph
    """
    f_labels = {}
    min_label = float('inf')
    for node in treeG:
        labels = {node: {node: 0}}
        find_child(treeG, labels, node)
        if get_label_size(labels) < min_label:
            min_label = get_label_size(labels)
            f_labels = labels.copy()
    return f_labels


def find_child(treeG, labels, parent):
    """ recursive method for finding child hubs from the root """
    if len(labels) == len(treeG):
        return labels
    for child in treeG[parent]:
        if child in treeG:
            if child not in labels:
                labels[child] = {child: 0}
                for hub in labels[parent].keys():
                    labels[child][hub] = labels[parent][hub] + treeG[parent][child]
                find_child(treeG, labels, child)


def get_label_size(labels):
    """ returns current max size of the labels """
    return max(len(labels[u]) for u in labels)


#######
# Testing
#


def get_distances(G, labels):
    # labels = {a:{b: distance from a to b,
    #              c: distance from a to c}}
    # create a mapping of all distances for
    # all nodes
    distances = {}
    for start in G:
        # get all the labels for my starting node
        label_node = labels[start]
        s_distances = {}
        for destination in G:
            shortest = float('inf')
            # get all the labels for the destination node
            label_dest = labels[destination]
            # and then merge them together, saving the
            # shortest distance
            for intermediate_node, dist in label_node.iteritems():
                # see if intermediate_node is our destination
                # if it is we can stop - we know that is
                # the shortest path
                if intermediate_node == destination:
                    shortest = dist
                    break
                other_dist = label_dest.get(intermediate_node)
                if other_dist is None:
                    continue
                if other_dist + dist < shortest:
                    shortest = other_dist + dist
            s_distances[destination] = shortest
        distances[start] = s_distances
    return distances


def make_link(G, node1, node2, weight=1):
    if node1 not in G:
        G[node1] = {}
    (G[node1])[node2] = weight
    if node2 not in G:
        G[node2] = {}
    (G[node2])[node1] = weight
    return G


def test():
    edges = [(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (3, 7),
             (4, 8), (4, 9), (5, 10), (5, 11), (6, 12), (6, 13)]
    tree = {}
    for n1, n2 in edges:
        make_link(tree, n1, n2)
    labels = create_labels(tree)
    distances = get_distances(tree, labels)
    assert distances[1][2] == 1
    assert distances[1][4] == 2
    
    
test()


def test2():
    edges = [(1, 2), (2, 3), (3, 4), (4, 5), (1, 6), (6, 7), 
             (7, 8), (8, 9), (1, 10), (10, 11), (11, 12), (12, 13)]    
    tree = {}
    for n1, n2 in edges:
        make_link(tree, n1, n2)
    labels = create_labels(tree)
    distances = get_distances(tree, labels)
    #for e in labels:
     #   print e, labels[e]
    for i in distances:
        print i, distances[i]
    print "Max Label Size: ", get_label_size(labels)


test2()
