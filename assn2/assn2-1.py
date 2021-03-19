import sys
import math
import copy

def star_stacking(N, star_array):
    K = int(math.log2(int(N/3)))
    for p in range(1, K+1):
        left_array = copy.deepcopy(star_array)
        two_k = int(2**p)

        for i in range(0, len(left_array), 3):
            i_three_step = int(i/3)
            space_num = (int(len(left_array)/3) - 1 - i_three_step) * 6
            for j in range(3):
                left_array[i+j][-1] = " "
                left_array[i+j].append(" " * (space_num + j))
                new_array = left_array[i+j] + star_array[i+j]
                star_array.append(new_array)
 


T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    two_k = int(N / 3)
    star_array = [
        ["*", "*", "*", "*", "*", "\n"],
        [" ", "*", " ", "*", "\n"],
        [" ", " ", "*", "\n"]]
    star_stacking(N, star_array)
    line_num = N
    for i in range(0, N, 3):
        line_num = line_num - 3
        for j in range(3):
            print(" " * line_num, end="")
            for e in star_array[i + j]:
                print(e, end="")
