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


        




