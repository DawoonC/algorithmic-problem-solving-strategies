def dijkstra(g, start, end):
    dist = {start: 0}
    path = {start: (start,)}
    queue = [start]
    while queue:
        v = queue.pop(0)
        for w in g[v].keys():
            if w not in dist or dist[v]+g[v][w] < dist[w]:
                dist[w] = dist[v]+g[v][w]
                path[w] = path[v]+(w,)
                queue.append(w)
    return (dist[end], path[end])
