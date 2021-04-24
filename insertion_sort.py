#Implementation of insertion sort
"""
SUDO
1) Loop through list starting from element 2
2) If you find the current number is less than the previous, move to next loop
    (a)while a[i]>a[i-1]:
        a[i],a[i-1] = a[i-1],a[i]
        i-=1
        if (i-1)<0:
            break;
3) You are here when all numbers previous are well arranged, continue loop
"""

def insertion_sort(a):
    #Get lenght of list
    a_len = len(a)
    #Loop through the list
    for i in range(1,a_len):
        #Check if pair is un-ordered.
        if a[i]<a[i-1]:
            #Perform switch as un-ordered item moved down the list till it reached the right spot or position 1
            while a[i]<a[i-1]:
                a[i],a[i-1] = a[i-1],a[i]
                i-=1
                if (i-1)<0:
                    break
    return "The ordered list is: {}".format(a)

if __name__ == "__main__":
    a = [3,2,1,5,4,6,7,10,11,17,16,15]
    print( insertion_sort(a) )

