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
# Given a graph G that is a balanced binary tree, preprocess the graph to
# create such labels for each node.  Note that the size of the list in
# each label should not be larger than log n for a graph of size n.
#

#
# create_labels takes in a balanced binary tree and the root element
# and returns a dictionary, mapping each node to its label
#
# a label is a dictionary mapping another node and the distance to
# that node
#

def create_labels(binarytreeG, root=None, labels=None):
    if root is None:
        root = binarytreeG.keys()[0]
    if labels is None:
        labels = { root: { root: 0 } }
    if len(labels) == len(binarytreeG):
        return labels
    for child in binarytreeG[root]:
        if child not in labels:
            labels[child] = { child: 0 }
            for hub in labels[root].keys():
                labels[child][hub] = labels[root][hub] + binarytreeG[root][child]
            create_labels(binarytreeG, child, labels)
    return labels


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
             (4, 8), (4, 9), (5, 10), (5, 11), (6, 12), (6, 13),
             (7, 14), (7, 15), (8, 16), (8, 17), (9, 18), (9, 19),
             (10, 20), (10, 21), (11, 22), (11, 23), (12, 24), (12, 25),
             (13, 26), (13, 27), (14, 28), (14, 29), (15, 30), (15, 31)]
    tree = {}
    for n1, n2 in edges:
        make_link(tree, n1, n2)
    labels = create_labels(tree, 1)
    for (k, v) in labels.items():
        for (n, d) in v.items():
            print k, '=>', n, '=', d
        print
    distances = get_distances(tree, labels)
    assert distances[1][2] == 1
    assert distances[1][4] == 2
    assert distances[8][13] == 6
    assert distances[9][1] == 3
    assert distances[10][6] == 5
    assert distances[16][23] == 6
    assert distances[18][15] == 7
    assert distances[20][24] == 8
    print 'distances[20][21]:', distances[20][21]
    print 'distances[20][22]:', distances[20][22]
    print 'distances[20][18]:', distances[20][18]
    print 'distances[20][16]:', distances[20][16]
    print 'distances[20][3]:', distances[20][3]
    print 'distances[20][7]:', distances[20][7]
    print 'distances[20][12]:', distances[20][12]
    print 'distances[20][14]:', distances[20][14]
    print 'distances[20][31]:', distances[20][31]


test()
