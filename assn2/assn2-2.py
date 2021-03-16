import sys

FLOOR_INT = -2147483648

def max_sum(array, left, right):
    if left == right:
        maxsum = max(array[left], array[right])
        return maxsum
    
    center = int((left+right) / 2)
    max_left = max_sum(array, left, center)
    max_right = max_sum(array, center+1, right)
    
    max_both_left_sum = FLOOR_INT 
    both_left_sum = 0
    max_both_right_sum = FLOOR_INT
    both_right_sum = 0

    for i in range(center, left - 1, -1):
        both_left_sum += array[i]
        max_both_left_sum = max(max_both_left_sum, both_left_sum)

    for i in range(center+1, right+1):
        both_right_sum += array[i]
        max_both_right_sum = max(max_both_right_sum, both_right_sum)

    return max(max_left, max_right, max_both_left_sum+max_both_right_sum)


T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    array = list(map(int, sys.stdin.readline().split()))
    answer = max_sum(array, 0, N-1)
    print(answer)
        


