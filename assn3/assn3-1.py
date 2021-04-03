import sys
from sys import maxsize as INT_MAX
from collections import deque


def shortest_cycles(N, M, edges):
    answer = INT_MAX
    graph = [[] for _ in range(N)]

    for e in edges:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])

    for i in range(N):
        prev = [-1] * N
        dist = [INT_MAX] * N

        q = deque()
        q.append(i)

        dist[i] = 0

        while q:
            v = q.popleft()
            for e in graph[v]:
                if dist[e] == INT_MAX:
                    dist[e] = dist[v] + 1
                    prev[e] = v
                    q.append(e)
                elif prev[e] != v and prev[v] != e:
                    answer = min(answer, dist[v] + dist[e] + 1)
            
    if answer == INT_MAX:
        return -1
    else:
        return answer

T = int(sys.stdin.readline())
for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())
    edges = []
    for _ in range(M):
        edges.append(tuple(map(int, sys.stdin.readline().split())))
    answer = shortest_cycles(N, M, edges)
    print(answer)
        


