import sys
import collections
from collections import deque
import copy

def stacking_blocks(blk_size, blk_quantity, box_size):
    box_seg_remained = deque([box_size])
    blk_num = [0 for _ in range(len(blk_size))]
    # Repeat until there's no remained box segments.
    while box_seg_remained:
        box_seg = box_seg_remained.popleft()
        i_min_box_edge = min(range(len(box_seg)), key=box_seg.__getitem__)
        i_max_blk = -1
        # Find max size block available to fill the segment.
        for i in range(len(blk_size) - 1, -1, -1):
            if box_seg[i_min_box_edge] >= blk_size[i]:
                i_max_blk = i
                break
        # If there is no block available, return -1.
        if i_max_blk == -1:
            return [-1]

        available_blk_num = 1
        new_segs = list()
        # Calculate the number of block to fill the segment.
        # After this, there remain at most 3 segments that can be filled with smaller blocks.
        for i in range(len(box_seg)):
            blk_num_per_edge = int(box_seg[i]/blk_size[i_max_blk])
            available_blk_num *= blk_num_per_edge
            new_seg = copy.deepcopy(box_seg)
            new_seg[i] -= blk_num_per_edge * blk_size[i_max_blk]
            if new_seg[i] != 0: # If one of the segment edge is 0, don't append this to new segments.
                new_segs.append(new_seg)

        # Remove overlapping areas and append the segments to remained box segments.
        blk_num[i_max_blk] += available_blk_num
        new_segs.sort(key=lambda x:-min(x))
        for i in range(len(new_segs)):
            if i == 0:
                box_seg_remained.append(copy.deepcopy(new_segs[i]))
            elif i == 1:
                min_index = min(range(len(new_segs[i-1])), key=new_segs[i-1].__getitem__)
                c_new_seg = copy.deepcopy(new_segs[i])
                c_new_seg[min_index] -= new_segs[i-1][min_index]
                box_seg_remained.append(c_new_seg)
            elif i == 2:
                min_index1 = min(range(len(new_segs[i-1])), key=new_segs[i-1].__getitem__) 
                min_index2 = min(range(len(new_segs[i-2])), key=new_segs[i-2].__getitem__) 
                c_new_seg = copy.deepcopy(new_segs[i])
                c_new_seg[min_index1] -= new_segs[i-1][min_index1]
                c_new_seg[min_index2] -= new_segs[i-2][min_index2]
                box_seg_remained.append(c_new_seg)

    # Comparing the calculated block num with block quantity, determine whether the box can be filled with given blocks.
    # If bigger blocks are not enough, replace the excess with smaller ones. 
    for i in range(len(blk_num) - 1, 0, -1):
        if blk_num[i] > blk_quantity[i]:
            diff = blk_num[i] - blk_quantity[i]
            blk_num[i] -= diff
            blk_num[i-1] += diff * 8
            
    if blk_num[0] > blk_quantity[0]:
        return [-1]

    return blk_num


T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    blk_size = list(map(int, sys.stdin.readline().split()))
    blk_quantity = list(map(int, sys.stdin.readline().split()))
    box_size = list(map(int, sys.stdin.readline().split())) 

    answer = stacking_blocks(blk_size, blk_quantity, box_size)
    print(*answer)
