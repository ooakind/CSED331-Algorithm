import sys
import collections

T = int(sys.stdin.readline())
for _ in range(T):
    N, C = map(int, sys.stdin.readline().split())
    seq = list(map(str, sys.stdin.readline().split()))
    C_to_i_dict = collections.defaultdict(int)
    count_list = list()
    is_changed = 0
    index = 0

    for x in seq:
        # 'in' operator has O(1) for dict, set / O(N) for list
        if x not in C_to_i_dict.keys(): # In python3, dict.keys() has O(1). Converting to list has O(N).
            C_to_i_dict[x] = index
            index += 1
            count_list.append(0)
        
        count_list[C_to_i_dict[x]] += 1
        
        if C_to_i_dict[x] > 0 and count_list[C_to_i_dict[x] - 1] < count_list[C_to_i_dict[x]]:
            is_changed = 1
            break 

    if is_changed:
        print("YES")
    else:
        print("NO")          



