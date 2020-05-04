def heapSort(array):
    """
    Performs sorting using heap sort
    """
    print("input:", array)

    # Build max-heap 
    buildMaxHeap(array)

    print("max heap:", array)

    # Traverse the array, swapping root node to the end of array and applying `siftDown`
    for i in range(len(array)):

        endIdx = len(array) - 1 - i
        
        # Moving root node(largest number) to end of array
        swap(0, endIdx, array)

        # Applying `siftDown` on entire array except last element
        siftDown(0, endIdx-1, array)

    print("sorted:", array)
    return array

def buildMaxHeap(array):
    """
    parent = (i-1)//2, childOne = 2*i+1, childTwo = 2*i+2
    """
    
    firstParentIdx = (len(array)-1) // 2

    for idx in range(firstParentIdx+1, -1, -1):
        siftDown(idx, len(array)-1, array)

    return array

def siftDown(currentIdx, endIdx, array):
    
    childOne = (2*currentIdx) + 1

    while childOne <= endIdx:
        # To handle the case childTwo may not exist
        childTwo = (2*currentIdx) + 2

        if childTwo <= endIdx:

            if array[childOne] > array[childTwo]:
                swapIdx = childOne
            else:
                swapIdx = childTwo

            # Comparing swapIdx with parent and swapping accordingly
            if array[swapIdx] > array[currentIdx]:
                # Swap
                swap(swapIdx, currentIdx, array)

                # Update parent and children
                currentIdx = swapIdx
                childOne = (2*currentIdx) + 1
                childTwo = (2*currentIdx) + 2
            else:
                # Max-heap property is already maintained
                return

        else:
            # Only childOne exists  
            if array[childOne] > array[currentIdx]:
                # Swap
                swap(childOne, currentIdx, array)

                # Update parent and children
                currentIdx = childOne
                childOne = (2*currentIdx) + 1
                childTwo = (2*currentIdx) + 2
            else:
                # Max-heap property is already maintained
                return

def swap(i, j, array):
    array[i], array[j] = array[j], array[i]

# Testing
l = [8, 5, 2, 9, 6, 5, 3]

heapSort(l)    