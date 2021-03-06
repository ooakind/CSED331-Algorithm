import sys

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    seq = list(map(int, sys.stdin.readline().split()))
    
    is_odd = N % 2
    middle =int(N/2) 
    if is_odd:
        best = seq[middle]
    else:
        best = (seq[middle] + seq[middle-1]) / 2

    dist = int(sum(list(map(lambda x : abs(x - best), seq))))
    print(dist)
