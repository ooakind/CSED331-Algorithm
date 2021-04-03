import sys
from collections import deque
from collections import defaultdict
from copy import deepcopy
import math

def dist_update(dist):
    return dist - 1 if dist < 0 else dist + 1

def sign(dist):
    return -1 if dist < 0 else 1

def reagent(ini_state):
    q = deque()
    final_state_cnt = [0] * 3
    final_state = [""] * 3
    dist = defaultdict(int)

    for s in ini_state:
        final_state_cnt[0] += s.count("1")
        final_state_cnt[1] += s.count("2")
        final_state_cnt[2] += s.count("3")

    final_state[0] = "1" * final_state_cnt[0]
    final_state[1] = "2" * final_state_cnt[1]
    final_state[2] = "3" * final_state_cnt[2]

    q.append(ini_state)
    q.append(final_state)

    dist[tuple(ini_state)] = 1
    dist[tuple(final_state)] = -1

    while q:
        state = q.popleft()
        for i in range(len(state)):
            if len(state[i]) == 0: continue
            for j in range(len(state)):
                if j == i: continue

                new_state = deepcopy(state)
                new_state[i] = new_state[i][:-1]
                new_state[j] = new_state[j] + state[i][-1]

                t_new_state = tuple(new_state) 
                t_state = tuple(state)

                if dist[t_new_state] == 0:
                    dist[t_new_state] = dist_update(dist[t_state])
                    q.append(new_state)
                elif sign(dist[t_new_state]) != sign(dist[t_state]):
                    return abs(dist[t_new_state]) + abs(dist[t_state]) - 1
                
    return 0
                        
    
T = int(sys.stdin.readline())
for _ in range(T):
    n_first, n_second, n_third = map(int, sys.stdin.readline().split())
    ini_state = []
    for _ in range(3):
        ini_state.append(str(sys.stdin.readline())[:-1])
    answer = reagent(ini_state)
    print(answer)
        


