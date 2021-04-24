"""
Algo
1) create an empty dict
2) calculate the number of items in each node using (2^index).
3) create an empty temp list
4) for the sub loop, we will loop through the expected items in each node i.e. (2^index)
    5) As long as the increamented index is less than the lenght of origina list,
        6) Append the item with the current index in the temp list
    7) continue to loop through to add other items, repeat 5,6.
8) Append the temp list to the dict as a new node
9) Check if increamented index is equal to the lenght of the original list, if yes, break loop,
if no continue with another iteration of the main for loop.
"""
if __name__ == "__main__":
    #Initialize increamental index, this will be incremented for each iteration of the minor for loop
    #this will ensure that each new iteration of the major for loop continues the minor for loop from where 
    #it last stopped
    index_switch = 0

    #Initialize test list
    a = [2,4,6,8,4,6,7,8,9,10,4,8,56,34,5,2,6,9,5,3,7,9,5,7,4,7,1,12,23,41,16,17]
    #Initialize empty dict
    tree = dict()   

    #Major for loop
    for i,j in enumerate(a):
        #The iterator is used by the minor for loop, it is the maximum number of items for each node (2^index).
        iterator = 2**i

        #Initialize empty list which will be fufilled for every iteration of the minor for loop. At the completion of the
        #minor for loop, the temporary list below will be saved as a new node in the tree dict.
        temp_list = []

        #Save a temporary index switch, this is used to alter the minor for loop such that it start from where the last minor loop ends,
        #and runs to the expected lenght
        index_switch_temp = index_switch

        #Minor loop
        for inner in range(index_switch_temp, iterator + index_switch_temp):
            #Catches error of list out of index by ensuring the index_switch is an index in the original list
            if ( len(a) ) != index_switch:
                temp_list.append( a[index_switch] )
                index_switch = index_switch + 1

        #Appends the temp list as a new node
        tree[ "".join(["Node",str(i)] )] = temp_list

        #Breaks the major for loop if the index equal to the lenght of the original list. This means the minor for loop
        #has looped through all items in original list, and thus it's value (sum of all minor iterations) is same as 
        #the lenght of original list
        if ( len(a) ) == index_switch:
            break

    print(tree)


def binaryT(a):
    #Initialize increamental index, this will be incremented for each iteration of the minor for loop
    #this will ensure that each new iteration of the major for loop continues the minor for loop from where 
    #it last stopped
    index_switch = 0

    #Initialize empty dict
    tree = dict()   

    #Major for loop
    for i,j in enumerate(a):
        #The iterator is used by the minor for loop, it is the maximum number of items for each node (2^index).
        iterator = 2**i

        #Initialize empty list which will be fufilled for every iteration of the minor for loop. At trhe completion of the
        #minor for loop, the temporary list below will be saved as a new node in the tree dict.
        temp_list = []

        #Save a temporary index switch, this is used to alter the minor for loop such that it start from where the last minor loop ends,
        #and runs to the expected lenght
        index_switch_temp = index_switch

        #Minor loop
        for inner in range(index_switch_temp, iterator+index_switch_temp):
            #Catches error of list out of index by ensuring the index_switch is an index in the original list
            if (len(a))!=index_switch:
                temp_list.append(a[index_switch])
                index_switch = index_switch + 1

        #Appends the temp list as a new node
        tree["".join(["Node",str(i)])] = temp_list

        #Breaks the major for loop if the index equal to the lenght of the original list. This means the minor for loop
        #has looped through all items in original list, and thus it's value (sum of all minor iterations) is same as 
        #the lenght of original list
        if (len(a))==index_switch:
            break

    return tree