import math


def merge(arr1, arr2):
    arr1Lenght = len(arr1)
    arr2Lenght = len(arr2)
    arr1Iter, arr2Iter = [0, 0]
    newArray = []

    while (arr1Iter < arr1Lenght) and (arr2Iter < arr2Lenght):

        if arr1[arr1Iter] < arr2[arr2Iter]:
            newArray.append(arr1[arr1Iter])
            arr1Iter += 1
        else:
            newArray.append(arr2[arr2Iter])
            arr2Iter += 1

    while arr1Iter <= arr1Lenght-1:
        newArray.append(arr1[arr1Iter])
        arr1Iter += 1

    while arr2Iter <= arr2Lenght-1:
        newArray.append(arr2[arr2Iter])
        arr2Iter += 1

    return newArray


def mergeSort(array):
    arrayLenght = len(array)

    if arrayLenght == 1:
        return array

    midPoint = math.floor(arrayLenght/2)
    array1 = array[:midPoint]
    array2 = array[midPoint:]

    return merge(mergeSort(array1), mergeSort(array2))


print(mergeSort([9, 1, 3, 5, 2, 4, 6, 1]))
