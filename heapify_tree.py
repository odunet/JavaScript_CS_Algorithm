"""
Algo
This should be and while true loop
1) At start of loop, initiate an exit variable iter_E_1 as 0
2) initialize a sub exit variable as iter_E_2 = 0
3) Calculate lenght of the dictionary of the binary
4) Make a for loop to loop through each node in the binary tree starting from the last_index
    if(last_index is the first index, break loop)
    iter_E_1 = iter_E_1 + iter_E_2
5) plan to loop through the current node using sub_last_index with and range(ceil(length(node)/2))
    (check for every iteration if they are at least two additional items to be compared)
    if yes:
        temp1 = min(tree["Node"+str(i)][index*2], tree["Node"+str(i)][index*2+1], \
                tree["Node"+str(i-1)][index])
        if temp1 == tree["Node"+str(i-1)][index]:
            continue;
        else:
            y = tree["Node"+str(i-1)].index(temp1)
            tree["Node"+str(i-1)][index], tree["Node"+str(i)][y] = tree["Node"+str(i)][y]\
            , tree["Node"+str(i-1)][index]
            iter_E_2 += 1
    if no:
        temp1 = min(tree["Node"+str(i)][index*2], tree["Node"+str(i)][index])
        if temp1 == tree["Node"+str(i-1)][index]:
            continue;
        else:
            tree["Node"+str(i-1)][index], tree["Node"+str(i)][index*2] = tree["Node"+str(i)][index*2]\
            , tree["Node"+str(i-1)][index]
            iter_E_2 += 1

6) Check if iter_E_1 == 0 (This means no swap occured)
    if yes, break from endless loop
"""
import math
from binary_tree import binaryT

def heap(tree, lst=[]):
    iter_E_1 = 0
    iter_E_2 = 0
    dict_len = len(tree)
    for i in range(dict_len-1):
        iter_E_1 = iter_E_1 + iter_E_2
        dict_item_len = len(tree["Node"+str(dict_len-1-i)])
        temp_iter = math.ceil(dict_item_len/2)
        for index in range(temp_iter):
            if dict_item_len < ((temp_iter*2)):
                temp1 = min(tree["Node"+str(dict_len-1-i)][index*2], tree["Node"+str(dict_len-1-i-1)][index])
                if temp1 == tree["Node"+str(dict_len-1-i-1)][index]:
                    continue
                else:
                    tree["Node"+str(dict_len-1-i)][index*2], tree["Node"+str(dict_len-1-i-1)][index] = tree["Node"+str(dict_len-1-i-1)][index]\
                    , tree["Node"+str(dict_len-1-i)][index*2]
                    iter_E_2 += 1       
            else:
                temp1 = min(tree["Node"+str(dict_len-1-i)][index*2], tree["Node"+str(dict_len-1-i-1)][index], tree["Node"+str(dict_len-1-i)][index*2+1])
                if temp1 == tree["Node"+str(dict_len-1-i-1)][index]:
                    continue
                else:
                    y = tree["Node"+str(dict_len-1-i)].index(temp1)
                    tree["Node"+str(dict_len-1-i-1)][index], tree["Node"+str(dict_len-1-i)][y] = tree["Node"+str(dict_len-1-i)][y]\
                    , tree["Node"+str(dict_len-1-i-1)][index]
                    iter_E_2 += 1         
    
    #store lowest value in new list and pop last rightmost number inm last node
    print(tree)
    tree["Node0"][0], tree["Node"+str(dict_len-1)][-1] = tree["Node"+str(dict_len-1)][-1]\
    , tree["Node0"][0]
    lst.append(tree["Node"+str(dict_len-1)][-1])
    tree["Node"+str(dict_len-1)].pop(-1)
    if not tree["Node"+str(dict_len-1)]: del tree["Node"+str(dict_len-1)]
    if len(tree) == 1:
        lst.append(tree["Node0"][0])
        return lst
    else:
        return heap(tree,lst)

if __name__ == "__main__":
    #Initialize test list
    s = [2,4,6,8,4,6,7,8,9,10,4,8,56,34,5,2,6,9,5,3,7,9,5,7,4,7,1,12,23,41,16,8]
    #Call the function to make a Binary Tree
    tree1 = binaryT(s)
    print("The un-ordered Binary Tree is: {}".format(tree1))
    #Call the function to Heapify the Binary Tree
    HeapifiedTree = heap(tree1)  
    print("The ordered Binary Tree is: {}".format(HeapifiedTree))