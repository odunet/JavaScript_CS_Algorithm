#Implementation of bubble sort
"""
SUDO
1) Loop through list starting from element 2 multiple time while list is disordered
2) For every loop, use a for loop to check if any number is dis-ordered, if no dis-ordered number is found break out of all loops
3) You are here when all numbers previous are well arranged, continue loop
"""

def bubble_sort(a):
            #Lenght of list
    a_len = len(a)

    while True:
        #Initialize swithc variable to 0
        confirm_switch = 0
        #Loop throught the list
        for i in range(1,a_len):
            #If an un-ordered pair is found, switch the pair positions
            if a[i]<a[i-1]:
                a[i],a[i-1] = a[i-1],a[i]
                #Increase switch value by 1
                confirm_switch += 1
        #If switch value is 0, i.e. no un-ordered pair was found, break loop.
        if confirm_switch == 0:
            break
    return "The ordered list is: {}".format(a)

#Call function
if __name__ == "__main__":
    a = [3,2,1,5,4,6,7,10,11,17,16,15]
    print( bubble_sort(a) )
            
