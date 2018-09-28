import heapq
inf = float('Inf')

def dijkstra(G, s):
    n = len(G)
    Q = [(0, s)]
    d = [inf for i in range(n)]
    d[s]=0
    while len(Q)!=0:
        (cost, u) = heapq.heappop(Q)
        for v in range(n):
            if d[v] > d[u] + G[u][v]:
                d[v] = d[u] + G[u][v]
                heapq.heappush(Q, (d[v], v))
    return d

G = [\
    [0.0, 2.0, 5.0, inf],\
    [2.0, 0.0, 2.0, 6.0],\
    [5.0, 2.0, 0.0, 3.0],\
    [inf, 6.0, 3.0, 0.0]]

d = dijkstra(G, 0)
print(d)
