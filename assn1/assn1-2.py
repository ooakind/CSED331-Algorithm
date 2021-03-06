import sys


T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    points = []
    for _ in range(N):
       points.append(tuple(map(int, sys.stdin.readline().split()))) 
    points.sort(key=lambda x: (x[0], x[1]))
    max_s = -1  # abs((points[0][1] - points[1][1]) / (points[0][0] - points[1][0])) 
    max_points = []
    for i in range(len(points) - 1):
        steep = abs((points[i][1] - points[i+1][1]) / (points[i][0] - points[i+1][0])) 
        if max_s < steep:
            max_s = steep
            max_points.clear()
            max_points.append(points[i])
            max_points.append(points[i+1])
    
    print(max_points[0][0], max_points[0][1], max_points[1][0], max_points[1][1])    

        


