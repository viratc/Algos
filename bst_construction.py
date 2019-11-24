class BST:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # To insert the value into the BST
    def insert(self, value):
        
        ## `self` is the root node
        currentNode = self

        # Running the loop indefinitely
        while True:
            if value < currentNode.value:
                # Left child node is NULL                
                if currentNode.left is None:
                    # Insert the new node
                    currentNode.left = BST(value)
                    break

                # If left child node exists, move to the next node     
                else:
                    currentNode = currentNode.left

            else:
                # Right child node is NULL                
                if currentNode.right is None:
                    # Insert the new node
                    currentNode.right = BST(value)
                    break

                # If right child node exists, move to the next node     
                else:
                    currentNode = currentNode.right

    def contains(self, value):

        currentNode = self

        while currentNode is not None:
            if value < currentNode.value:
                currentNode = currentNode.left
            elif value > currentNode.value:
                currentNode = currentNode.right
            else:
                return True
        return False            

    def getMinValue(self):
        # Method to find minimum value
        currentNode = self

        while currentNode.left is not None:                
            currentNode = currentNode.left

        return currentNode.value               

    def remove(self, value, parentNode=None):
        
        currentNode = self

        while currentNode is not None:

            if value < currentNode.value:
                # Update parentNode & currentNode till we find the node, that's to be removed
                parentNode = currentNode
                currentNode = currentNode.left

            elif value > currentNode.value:
                # Update parentNode & currentNode till we find the node, that's to be removed
                parentNode  = currentNode
                currentNode = currentNode.right

            else:
                # Found the node that's to be removed; now we remove it and arrange the BST
                
                # Case where both the children are present
                if currentNode.left is not None and currentNode.right is not None:
                    #   2   We have to remove 4 i.e parentNode = 2, currentNode = 4
                    #  / \   
                    # 1   4
                    #    / \
                    #   3   5

                    # Find the node thats to be removed => currentNode = 4, currentNode.value = 5
                    currentNode.value = currentNode.right.getMinValue()

                    # currentNode.value = 5 (value), currentNode = 4 (parentNode)
                    currentNode.right.remove(currentNode.value, currentNode)

                # `Root` node case
                elif parentNode is None:

                    #      4              4            
                    #     /                \
                    #    2                  6
                    #   / \                / \
                    #  1   3              5   7
 
                    # currentNode has only 1 child node, and if that child is the `left` node
                    # Deleting 4 (currentNode=4 and parentNode=None)
                    if currentNode.left is not None:
                        # Replacing all the values of our left & right nodes, with left node's value
                        # Order is important
                        currentNode.value = currentNode.left.value
                        currentNode.right = currentNode.left.right
                        currentNode.left = currentNode.left.left

                    elif currentNode.right is not None:
                        currentNode.value = currentNode.right.value
                        currentNode.left = currentNode.right.left
                        currentNode.right = currentNode.right.right

                    else:
                        # Case where only root node is present in the entire BST
                        currentNode.value = None    

                # When we are `not` dealing with `root` node ( & doesn't have 2 children)
                # i.e there is only 1 child node or None, then we check if our current node
                # is a `left` child or `right` child

                #           4                3                3
                #          / \              / \                \
                #         2   5            2   4                6
                #        / \              /   / \              / \
                #       1   3            1  4.5  5            5   8
                #                                            /   /
                #                                           4   7

                # If it's a `left` child (Eg: 2 i.e currentNode=2 & parentNode=4)
                elif parentNode.left == currentNode:
                    parentNode.left = currentNode.left if currentNode.left is not None else currentNode.right

                # If it's a `right` child (Eg: 4 i.e currentNode=4 & parentNode=3)
                elif parentNode.right == currentNode:
                    parentNode.right = currentNode.left if currentNode.left is not None else currentNode.right 

                # Want to break when we have found our value
                break       
                    


                            
                    




