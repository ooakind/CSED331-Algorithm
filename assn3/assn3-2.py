import sys
from collections import deque

sys.setrecursionlimit(40000)

time = 0
INT_MAX = 2147483648

def find_bridge(u, visited, disc, earliest_visit, graph, prev, bridge):
    global time
    visited[u] = True
    disc[u] = time
    earliest_visit[u] = time
    time += 1

    for v, w in graph[u]:
        if not visited[v]:
            prev[v] = u
            find_bridge(v, visited, disc, earliest_visit, graph, prev, bridge)

            earliest_visit[u] = min(earliest_visit[u], earliest_visit[v])
            if earliest_visit[v] > disc[u] and sum(map(lambda x : x[0] == v, graph[u])) == 1:
                bridge.append(w)
        elif v != prev[u]:
            earliest_visit[u] = min(earliest_visit[u], disc[v])

def retreat(N, M, edges):
    visited = [False] * N
    disc = [INT_MAX] * N
    earliest_visit = [INT_MAX] * N
    graph = [[] for _ in range(N)] # 0: connected vertex, 1: weight of the edge
    prev = [-1] * N
    bridge = []

    for e in edges:
        graph[e[0]].append([e[1], e[2]])
        graph[e[1]].append([e[0], e[2]])

    for i in range(N):
        if not visited[i]:
            find_bridge(i, visited, disc, earliest_visit, graph, prev, bridge)
    
    if len(bridge) == 0:
        return -1
    else:
        return min(bridge)

    
T = int(sys.stdin.readline())
for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())
    edges = []
    for _ in range(M):
        edges.append(tuple(map(int, sys.stdin.readline().split())))
    answer = retreat(N, M, edges)
    print(answer)
        


