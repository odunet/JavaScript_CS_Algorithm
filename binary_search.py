#Implementation of binary search
"""
SUDO
1) Divide the loop into two, check if required number is equal to middle number, if yes found return the missing number and exit, else
2) Check if required number is less than or greater than the middle number and return the appropraite half
3) Call the function recursively with the newly halved list until the required number is found, return  missing number
"""
import math

def binary_search(a,b):
    #Get the midpoint
    mid_index = math.floor( len(a)/2 )
    #If the list has been reduced to 2 elements, check if missing value is there.
    if len(a)/2 == 1:
        if b == a[0]:
            return "The number {} is found".format(a[0])
        elif b == a[1]:
            return "The number {} is found".format(a[1])
        else:
            return 'The number is not in the List'
    #Check if missing number is the mid element
    if b == a[mid_index]:
        return b
    #Check if missing number is larger than index, then run fucntion recursively on new list
    elif b > a[mid_index]:
        return binary_search(a[mid_index:],b)
    else:
    #Check if missing number is smaller than index, then run fucntion recursively on new list
        return binary_search(a[:mid_index],b)
    
#Call function
if __name__ == "__main__":
    #Initialize variable
    lst = [3,2,1,4,5,6,7,10,11,14,16,17,19,20,23,25,28,30]
    missing_num = 19    

    #Call function
    print( binary_search(lst,missing_num) )

