# Time=O(nlog(n)) && space = O(nlog(n))
def merge_sort(array):

    # Base-case of len(array) == 1
    if len(array) == 1:
        return(array)

    # Middle Index of array
    middleIndex = len(array) // 2 

    # Splitting up the array
    leftHalf = array[:middleIndex]
    rightHalf = array[middleIndex:]

    # We have to further divide these arrays and call merge_sort() on them ( and we also have to merge these later)
    return merge_sorted_array(merge_sort(leftHalf), merge_sort(rightHalf))

# Function to merge (sorted) arrays
def merge_sorted_array(leftHalf, rightHalf):

    # Creating a array with all 0's, which'll be filled later 
    sortedArray = [0] * (len(leftHalf) + len(rightHalf))

    k = i = j = 0

    # Comparing each element of leftHalf with that of rightHalf
    while i < len(leftHalf) and j < len(rightHalf):
        # Compare ith index of leftHalf with that of jth in rightHalf
        if leftHalf[i] <= rightHalf[j]:
            sortedArray[k] = leftHalf[i]
            i += 1
        else:
            sortedArray[k] = rightHalf[j]
            j += 1
        k += 1

    # If we still have number's in the left half ( usually there is a uneven split)
    while i < len(leftHalf):
        sortedArray[k] = leftHalf[i]
        i += 1
        k +=1 

    # If there are element's in the right half 
    while j < len(rightHalf):
        sortedArray[k] = rightHalf[j]
        j += 1
        k += 1               

    return(sortedArray)
        
# Typically when we sort a array, we mutate them

# Optimization for merge sort; Time=O(nlog(n)) && space = O(n)
def merge_sort2(array):
    if len(array) <= 1:
        return(array)

    auxillaryArray = array[:]
    mergeSortHelper(array, 0, len(array)-1, auxillaryArray)

    # Since we are sorting `in-place`
    return(array)


def mergeSortHelper(mainArray, startIndex, endIndex, auxillaryArray):
    if startIndex == endIndex:
        return

    middleIndex = (startIndex + endIndex) // 2

    mergeSortHelper(auxillaryArray, startIndex, middleIndex, mainArray)

    mergeSortHelper(auxillaryArray, middleIndex+1, endIndex, mainArray)    

    doMerge(mainArray, startIndex, middleIndex, endIndex, auxillaryArray)

def doMerge(mainArray, startIndex, middleIndex, endIndex, auxillaryArray):
    # We are merging 2 arrays: 1 starts at startIndex and ends at middleIndex and other starts at middleIndex and ends at endIndex
    k = startIndex
    i = startIndex  
    j = middleIndex+1

    while i <= middleIndex and j <= endIndex:
        if auxillaryArray[i] <= auxillaryArray[j]:
            mainArray[k] = auxillaryArray[i]
            i += 1
        else:
            mainArray[k] = auxillaryArray[j]
            j += 1
        k += 1

    # If elements are still there in left half
    while i <= middleIndex:
        mainArray[k] = auxillaryArray[i]
        i += 1
        k += 1

    while j <= endIndex:
        mainArray[k] = auxillaryArray[j]
        j += 1
        k += 1        




















