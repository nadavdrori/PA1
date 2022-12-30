# username - nadavdrori
# id1      - 208935882
# name1    - Nadav Drori
# id2      - 318900883
# name2    - Omer Talmi


"""A class represnting a node in an AVL tree"""
from random import randint


class AVLNode(object):
    """Constructor, you are allowed to add more fields.

    @type value: str
    @param value: data of your node
    """

    def __init__(self, value, parent=None):
        if value is not None:
            self.value = value
            self.left = AVLNode(None, self)
            self.right = AVLNode(None, self)
            self.parent = None
            self.height = 0
            self.size = 1
        else:
            self.value = None
            self.left = None
            self.right = None
            self.parent = parent
            self.height = -1
            self.size = 0

    """returns the left child
    @rtype: AVLNode
    @returns: the left child of self, None if there is no left child
    """

    def getLeft(self):
        return self.left

    """returns the right child

    @rtype: AVLNode
    @returns: the right child of self, None if there is no right child
    """

    def getRight(self):
        return self.right

    """returns the parent 

    @rtype: AVLNode
    @returns: the parent of self, None if there is no parent
    """

    def getParent(self):
        return self.parent

    """return the value

    @rtype: str
    @returns: the value of self, None if the node is virtual
    """

    def getValue(self):
        return self.value

    """returns the height

    @rtype: int
    @returns: the height of self, -1 if the node is virtual
    """

    def getHeight(self):
        return self.height

    """returns the size

        @rtype: int
        @returns: the size of self, 0 if the node is virtual
        """

    def getSize(self):
        return self.size

    """sets left child

    @type node: AVLNode
    @param node: a node
    """

    def setLeft(self, node):
        self.left = node

    """sets right child

    @type node: AVLNode
    @param node: a node
    """

    def setRight(self, node):
        self.right = node

    """sets parent

    @type node: AVLNode
    @param node: a node
    """

    def setParent(self, node):
        self.parent = node

    """sets value

    @type value: str
    @param value: data
    """

    def setValue(self, value):
        self.value = value

    """sets the balance factor of the node

    @type h: int
    @param h: the height
    """

    def setHeight(self, h):
        self.height = h

    """sets the size of the subtree of the node (inclusive)

       @type size: int
       @param size: the size
       """

    def setSize(self, size):
        self.size = size

    """returns whether self is not a virtual node 

    @rtype: bool
    @returns: False if self is a virtual node, True otherwise.
    """

    def isRealNode(self):
        return self.value is not None and self.getLeft() is not None and self.getRight() is not None


"""
A class implementing the ADT list, using an AVL tree.
"""


class AVLTreeList(object):
    """
    Constructor, you are allowed to add more fields.

    """

    def __init__(self):
        self.size = 0
        self.root = None
        self.first_node = None
        self.last_node = None

    # add your fields here

    def setSize(self, size):
        self.size = size

    def getSize(self):
        return self.size

    """returns whether the list is empty

    @rtype: bool
    @returns: True if the list is empty, False otherwise
    """

    def empty(self):
        return self.getRoot() is None or self.getRoot().isRealNode() is False

    """retrieves the value of the i'th item in the list

    @type i: int
    @pre: 0 <= i < self.length()
    @param i: index in the list
    @rtype: str
    @returns: the value of the i'th item in the list
    """

    def retrieve(self, i):
        if self.empty():
            return None
        return self.retrieve_node(i).getValue()

        """retrieves the i'th item in the list

        @type i: int
        @pre: 0 <= i < self.length()
        @param i: index in the list
        @rtype: AVLNode
        @returns: the i'th item in the list
        """

    def retrieve_node(self, i):
        if self.empty():
            return None
        if i < 0 or i >= self.length():
            return None
        return self.select(self.getRoot(), i + 1)

    """ return the node with rank of i in the tree
    @type i: int
    @pre: 0 <= i < self.length()
    @param i: rank in the tree
    @rtype: AVLNode
    @returns: the node with rank of i in the tree
    """

    def select(self, node, i):
        left_node_size = 1
        if node.getLeft() is not None and node.getLeft().isRealNode():
            left_node_size = node.getLeft().getSize() + 1
        if left_node_size == i:
            return node
        elif left_node_size > i:
            return self.select(node.getLeft(), i)
        elif node.getRight() is not None and node.getRight().isRealNode():
            return self.select(node.getRight(), i - left_node_size)
        else:
            return None

    """inserts val at position i in the list

    complexity - O(logn)
    @type i: int
    @pre: 0 <= i <= self.length()
    @param i: The intended index in the list to which we insert val
    @type val: str
    @param val: the value we inserts
    @rtype: list
    @returns: the number of rebalancing operation due to AVL rebalancing
    """

    def insert(self, i, val):
        if self.empty():
            self.setRoot(AVLNode(val))
            inserted_node = self.getRoot()
            self.last_node = inserted_node
            self.first_node = inserted_node
        else:
            if i == self.length():
                inserted_node = self.insertLast(val)
                self.last_node = inserted_node
            elif i < self.length():
                inserted_node = self.insert_in_middle(i, val)
        self.setSize(self.getSize() + 1)
        return self.rebalancing_tree(inserted_node)

    """inserts val at middle position in the list

    @type val: str
    @param val: the value we inserts
    @rtype: AVLNode
    @returns: the inserted node
    """

    def insert_in_middle(self, i, val):
        curr_node = self.retrieve_node(i)
        if curr_node.getLeft().getValue() is None:
            curr_node.setLeft(AVLNode(val))
            curr_node.getLeft().setParent(curr_node)
            if curr_node is self.first_node:
                self.first_node = curr_node.getLeft()
            return curr_node.getLeft()
        else:
            pred = self.predecessor(curr_node)
            pred.setRight(AVLNode(val))
            pred.getRight().setParent(pred)
            return pred.getRight()

    """inserts val at last position in the list

        @type val: str
        @param val: the value we inserts
        @rtype: AVLNode
        @returns: the inserted node
        """

    def insertLast(self, val):
        curr_node = self.getRoot()
        curr_node = self.get_max_node_in_sub_of(curr_node)
        curr_node.setRight(AVLNode(val))
        curr_node.getRight().setParent(curr_node)
        return curr_node.getRight()

    """ return the max node in the sub tree
        @type node: AVLNode
        @param curr_node: the node we start from
        @rtype: AVLNode
        @returns: the max node in the sub tree
    """

    def get_max_node_in_sub_of(self, curr_node):
        if self.empty():
            return None
        while curr_node.getRight().isRealNode():
            curr_node = curr_node.getRight()
        return curr_node

    """ return the min node in the sub tree
            @type node: AVLNode
            @param curr_node: the node we start from
            @rtype: AVLNode
            @returns: the min node in the sub tree
    """

    def get_min_node_in_sub_of(self, curr_node):
        if self.empty():
            return None
        while curr_node.getLeft().isRealNode():
            curr_node = curr_node.getLeft()
        return curr_node

    """ make the tree balanced and update the node's fields
    @type node: AVLNode
    @param node: the node we start from
    @rtype: int
    @returns: the number of rotations operations due to AVL rebalancing
    """

    def rebalancing_tree(self, node):
        rotates_amount = 0
        while node is not None:
            self.update_height_and_size(node)
            if abs(node.getLeft().getHeight() - node.getRight().getHeight()) > 1:
                rotates_amount += self.rotate(node)
            node = node.parent
        return rotates_amount

    """ make rotation on node
    @type node: AVLNode
    @param node: the node we operate on
    """

    def rotate(self, node):
        if node.getLeft().getHeight() > node.getRight().getHeight():
            if node.getLeft().getLeft().getHeight() > node.getLeft().getRight().getHeight():
                return self.right_rotation(node)
            else:
                return self.left_right_rotation(node)
        else:
            if node.getRight().getRight().getHeight() > node.getRight().getLeft().getHeight():
                return self.left_rotation(node)
            else:
                return self.right_left_rotation(node)

    """ make right rotation on node
    @type node: AVLNode
    @param node: the node we operate on
    """

    def right_rotation(self, node):
        left_child = node.getLeft()
        left_child.setParent(node.parent)
        if node.getParent() is not None:
            if node.getParent().getLeft() == node:
                node.getParent().setLeft(left_child)
            else:
                node.getParent().setRight(left_child)
        node.setLeft(left_child.getRight())
        node.getLeft().setParent(node)
        left_child.setRight(node)
        left_child.getRight().setParent(left_child)
        self.update_height_and_size(node)
        self.update_height_and_size(left_child)
        if self.getRoot() == node:
            self.setRoot(left_child)
        return 1

    """ make left rotation on node
        @type node: AVLNode
        @param node: the node we operate on
        """

    def left_rotation(self, node):
        right_child = node.getRight()
        right_child.setParent(node.getParent())
        if node.getParent() is not None:
            if node.getParent().getRight() == node:
                node.getParent().setRight(right_child)
            else:
                node.getParent().setLeft(right_child)
        node.setRight(right_child.getLeft())
        node.getRight().setParent(node)
        right_child.setLeft(node)
        right_child.getLeft().setParent(right_child)
        self.update_height_and_size(node)
        self.update_height_and_size(right_child)
        if self.getRoot() == node:
            self.setRoot(right_child)
        return 1

    """ make left right rotation on node
        @type node: AVLNode
        @param node: the node we operate on
    """

    def left_right_rotation(self, node):
        return self.left_rotation(node.getLeft()) + self.right_rotation(node)

    """ make right left rotation on node
        @type node: AVLNode
        @param node: the node we operate on
    """

    def right_left_rotation(self, node):
        return self.right_rotation(node.getRight()) + self.left_rotation(node)

    """ update the height and size of the node
        @type node: AVLNode
        @param node: the node we operate on
    """

    def update_height_and_size(self, node):
        node.setHeight(max(node.getLeft().getHeight(), node.getRight().getHeight()) + 1)
        node.setSize(node.getLeft().getSize() + node.getRight().getSize() + 1)

    """deletes the i'th item in the list

    @type i: int
    @pre: 0 <= i < self.length()
    @param i: The intended index in the list to be deleted
    @rtype: int
    @returns: the number of rebalancing operation due to AVL rebalancing
    """

    def delete(self, i):
        if self.getRoot().getSize() != self.getSize():
            # TODO: Remove this line after debugging
            self.update_height_and_size(self.getRoot())
        if self.empty():
            return 0
        node = self.retrieve_node(i)
        rotations_count = self.delete_node(node)
        self.setSize(self.getRoot().getSize())
        if not self.getRoot().isRealNode():
            self.setRoot(None)
        return rotations_count

    """deletes the node in the list
    @type node: AVLNode
    @param node: The intended node in the list to be deleted
    @rtype: int
    @returns: the deleted node
    """

    def delete_node(self, node):
        if node is None or not node.isRealNode():
            return 0
        parent = node.getParent()
        if node.getLeft().isRealNode() and node.getRight().isRealNode():
            parent = self.delete_node_with_two_sons(node)
        elif node.getLeft().isRealNode() or node.getRight().isRealNode():
            self.delete_node_with_single_son(node)
        else:
            self.delete_leaf(node)
        rotations_count = self.rebalancing_tree(parent)
        return rotations_count

    """deletes node which have single son
        @type node: AVLNode
        @param node: The intended node in the list to be deleted with single son
    """

    def delete_node_with_single_son(self, node):
        if node is self.first_node:
            self.first_node = self.successor(node)
        if node is self.last_node:
            self.last_node = self.predecessor(node)

        if node.getLeft().isRealNode():
            node_to_connect = node.getLeft()
        else:
            node_to_connect = node.getRight()
        node_to_connect.setParent(node.getParent())
        if node.getParent() is not None:
            if node.getParent().getLeft() == node:
                node.getParent().setLeft(node_to_connect)
            else:
                node.getParent().setRight(node_to_connect)
        else:
            self.setRoot(node_to_connect)

    def delete_leaf(self, node):
        if node is self.first_node:
            self.first_node = self.successor(node)
        if node is self.last_node:
            self.last_node = self.predecessor(node)

        if node.getParent() is not None:
            if node.getParent().getLeft() == node:
                node.getParent().setLeft(AVLNode(None, node.getParent()))
            else:
                node.getParent().setRight(AVLNode(None, node.getParent()))
        else:
            self.setRoot(AVLNode(None))

    """deletes node which have two sons
        @type node: AVLNode
        @param node: The intended node in the list to be deleted with two sons
        @rtype: AVLNode
        @returns: the node which is the parent of the actual deleted node
    """

    def delete_node_with_two_sons(self, node):
        successor = self.successor(node)
        if node.getRight() == successor:
            parentOfSuccessor = node.getParent()
        else:
            parentOfSuccessor = successor.getParent()

        self.replace_and_delete(node, successor)
        curr_node = parentOfSuccessor
        while curr_node is not None:
            self.update_height_and_size(curr_node)
            curr_node = curr_node.parent
        return parentOfSuccessor

    def replace_and_delete(self, node, successor):
        if successor.getLeft().isRealNode() or successor.getRight().isRealNode():
            self.delete_node_with_single_son(successor)
        else:
            self.delete_leaf(successor)

        successor.setParent(node.getParent())
        successor.setLeft(node.getLeft())
        successor.setRight(node.getRight())
        successor.setHeight(node.getHeight())
        successor.setSize(node.getSize())

        if node.getParent() is None:
            self.setRoot(successor)
        else:
            if node.getParent().getLeft() == node:
                node.getParent().setLeft(successor)
            else:
                node.getParent().setRight(successor)

        node.getRight().setParent(successor)
        node.getLeft().setParent(successor)

        node.setLeft(AVLNode(None, node))
        node.setRight(AVLNode(None, node))
        node.setParent(None)
        node.setValue(None)
        node.setHeight(0)
        node.setSize(0)

    """ get the successor of the node
        @type node: AVLNode
        @param node: The intended node in the list to get its successor
        @rtype: AVLNode
        @returns: the successor of the node
    """

    def successor(self, node):
        if node.getRight().getValue() is not None:
            return self.get_min_node_in_sub_of(node.getRight())
        else:
            while node.getParent() is not None and node == node.getParent().getRight():
                node = node.getParent()
            return node.getParent()

    """ get the predecessor of the node
            @type node: AVLNode
            @param node: The intended node in the list to get its predecessor
            @rtype: AVLNode
            @returns: the predecessor of the node
        """

    def predecessor(self, node):
        if node.getLeft().getValue() is not None:
            return self.get_max_node_in_sub_of(node.getLeft())
        else:
            while node.getParent() is not None and node == node.getParent().getLeft():
                node = node.getParent()
            return node.getParent()

    """returns the value of the first item in the list

    @rtype: str
    @returns: the value of the first item, None if the list is empty
    """

    def first(self):
        if self.empty():
            return None
        return self.first_node.getValue()

    """returns the value of the last item in the list

    @rtype: str
    @returns: the value of the last item, None if the list is empty
    """

    def last(self):
        if self.empty():
            return None
        return self.last_node.getValue()

    """returns an array representing list 
    complexity: O(n)
    @rtype: list
    @returns: a list of strings representing the data structure
    """

    def listToArray(self):
        lst = []
        return self.listToArray_rec(self.getRoot(), lst)

    """insert the tree nodes to the given list
    complexity: O(n)
    @type lst: list
    @param lst: the list to insert the tree nodes to
    @type node: AVLNode
    @param node: the current node to insert to the list
    @rtype: list
    @returns: the list of strings representing the data structure
        """

    def listToArray_rec(self, node, lst):
        if not node.isRealNode():
            return lst
        self.listToArray_rec(node.getLeft(), lst)
        lst.append(node.getValue())
        self.listToArray_rec(node.getRight(), lst)
        return lst

    """returns the size of the list 

    @rtype: int
    @returns: the size of the list
    """

    def length(self):
        return self.size

    """sort the info values of the list
    complexity: O(nlogn)
    @rtype: list
    @returns: an AVLTreeList where the values are sorted by the info of the original list.
    """

    def sort(self):
        sorted_tree = AVLTreeList()
        lst = self.listToArray()
        self.mergeSort(lst, 0, len(lst) - 1)
        sorted_tree.create_tree_from_sorted_lst(lst)
        return sorted_tree

    """sort the given list
    complexity: O(nlogn)    
    @type lst: list
    @param lst: the list to sort
    @type start: int
    @param start: the start index of the list
    @type end: int
    @param end: the end index of the list
    """

    def mergeSort(self, lst, left_index, right_index):
        if left_index < right_index:
            middle_index = left_index + (right_index - left_index) // 2

            # Sort first and second halves
            self.mergeSort(lst, left_index, middle_index)
            self.mergeSort(lst, middle_index + 1, right_index)
            self.merge(lst, left_index, middle_index, right_index)

    """merge the two sorted lists
    @type lst: list
    @param lst: the list to sort
    @type left_index: int
    @param left_index: the start index of the list
    @type middle_index: int
    @param middle_index: the middle index of the list
    @type right_index: int
    @param right_index: the end index of the list
    """

    def merge(self, lst, left_index, middle_index, right_index):
        n1 = middle_index - left_index + 1
        n2 = right_index - middle_index

        # create temp arrays
        left_lst = [0] * (n1)
        right_lst = [0] * (n2)

        # Copy data to temp arrays left_lst[] and right_lst[]
        for i in range(0, n1):
            left_lst[i] = lst[left_index + i]

        for j in range(0, n2):
            right_lst[j] = lst[middle_index + 1 + j]

        # Merge the temp arrays back into lst[left_index..right_index]
        i = 0  # Initial index of first subarray
        j = 0  # Initial index of second subarray
        k = left_index  # Initial index of merged subarray

        while i < n1 and j < n2:
            if left_lst[i] <= right_lst[j]:
                lst[k] = left_lst[i]
                i += 1
            else:
                lst[k] = right_lst[j]
                j += 1
            k += 1

        # Copy the remaining elements of left_lst[], if there
        # are any
        while i < n1:
            lst[k] = left_lst[i]
            i += 1
            k += 1

        # Copy the remaining elements of right_lst[], if there
        # are any
        while j < n2:
            lst[k] = right_lst[j]
            j += 1
            k += 1

    """create a tree from a sorted list    
    @type lst: list
    @param lst: the list to create the tree from
    """

    def create_tree_from_sorted_lst(self, sorted_lst: list):
        self.setRoot(self.create_tree_from_sorted_lst_rec(sorted_lst, 0, len(sorted_lst) - 1))

    def create_tree_from_sorted_lst_rec(self, sorted_lst, first, last):
        if last == first:
            return AVLNode(sorted_lst[first])
        else:
            middle = (last + first) // 2
            root_node = AVLNode(sorted_lst[middle])

            root_node.setLeft(self.create_tree_from_sorted_lst_rec(sorted_lst, first, middle))
            root_node.getLeft().setParent(root_node)

            root_node.setRight(self.create_tree_from_sorted_lst_rec(sorted_lst, middle + 1, last))
            root_node.getRight().setParent(root_node)
            return root_node

    """permute the info values of the list 
    complexity: O(n)
    @rtype: list
    @returns: an AVLTreeList where the values are permuted randomly by the info of the original list. ##Use Randomness
    """

    def permutation(self):
        shuffled_tree = AVLTreeList()
        lst = self.listToArray()
        self.shuffle_list(lst)
        shuffled_tree.create_tree_from_sorted_lst(lst)
        return shuffled_tree

    """shuffle the given list
    complexity: O(n)
    @type lst: list
    @param lst: the list to shuffle
    """

    def shuffle_list(self, lst):
        # Start from the last element and swap one by one. We don't
        lst_size = len(lst)
        for index in range(lst_size - 1, 0, -1):
            index_to_replace = randint(0, index)
            lst[index], lst[index_to_replace] = lst[index_to_replace], lst[index]

        return lst

    """concatenates lst to self

    @type lst: AVLTreeList
    @param lst: a list to be concatenated after self
    @rtype: int
    @returns: the absolute value of the difference between the height of the AVL trees joined
    """

    def concat(self, lst):
        if self.empty() and lst.empty():
            return 0
        if self.empty():
            self.setRoot(lst.getRoot())
            self.setSize(lst.length())
            self.first_node = lst.first_node
            self.last_node = lst.last_node
            return lst.getRoot().getHeight() + 1
        if lst.empty():
            return self.getRoot().getHeight() + 1

        height = self.getRoot().getHeight() - lst.getRoot().getHeight()
        if height >= 0:
            tall_tree_connect_node = self.getRoot()
            low_tree_root = lst.getRoot()
            x = self.last_node
            self.delete_node(x)
            x.setParent(None)
            self.update_big_tree(low_tree_root, tall_tree_connect_node, x)
        else:
            low_tree_root = self.getRoot()
            tall_tree_connect_node = lst.getRoot()
            x = self.last_node
            self.delete_node(x)
            x.setParent(None)
            self.update_small_tree(low_tree_root, tall_tree_connect_node, x)
        # TODO: THE TEST test_compare_concatinated_treelists_and_list_small fails here
        self.rebalancing_tree(x)
        self.update_root(x)
        self.setSize(self.getRoot().getSize())
        height = abs(height)
        self.first_node = self.get_min_node_in_sub_of(self.getRoot())
        self.last_node = self.get_max_node_in_sub_of(self.getRoot())
        return height

    """ update pointer while concat in case of big tree
    @type lower_tree_root: AVLNode
    @param lower_tree_root: the root of the lower tree
    @type taller_tree_connect_node: AVLNode
    @param taller_tree_connect_node: the root of the taller tree
    @type x: AVLNode
    @param x: the node to connect between the trees
    """

    def update_big_tree(self, lower_tree_root, taller_tree_connect_node, x):
        while taller_tree_connect_node.getHeight() > lower_tree_root.getHeight() and taller_tree_connect_node.getRight().isRealNode():
            taller_tree_connect_node = taller_tree_connect_node.getRight()
        b = taller_tree_connect_node
        a = lower_tree_root
        x.setLeft(b)
        x.setRight(a)
        if b.getParent() != None:
            x.setParent(b.getParent())
            b.getParent().setRight(x)
        else:
            self.setRoot(x)
            self.getRoot().setSize(self.getSize())
        a.setParent(x)
        b.setParent(x)
        self.rebalancing_tree(x)

    """ update pointer while concat in case of small tree
    @type lower_tree_root: AVLNode
    @param lower_tree_root: the root of the lower tree
    @type taller_tree_connect_node: AVLNode
    @param taller_tree_connect_node: the root of the taller tree
    @type x: AVLNode
    @param x: the node to connect between the trees
    """

    def update_small_tree(self, low_tree_root, tall_tree_connect_node, x):
        while tall_tree_connect_node.getHeight() > low_tree_root.getHeight() and tall_tree_connect_node.getLeft().isRealNode():
            tall_tree_connect_node = tall_tree_connect_node.getLeft()
        a = low_tree_root
        b = tall_tree_connect_node
        c = b.getParent()
        a.setParent(x)
        x.setLeft(a)
        x.setRight(b)
        b.setParent(x)
        c.setLeft(x)
        x.setParent(c)
        self.rebalancing_tree(x)

    """set the root of the tree to be the given node
    @type node: AVLNode
    @param node: the node to be the root of the tree
    """

    def update_root(self, node):
        while node.getParent() is not None:
            node = node.getParent()
        self.setRoot(node)

    """searches for a *value* in the list

    @type val: str
    @param val: a value to be searched
    @rtype: int
    @returns: the first index that contains val, -1 if not found.
    """

    def search(self, val):
        if self.getSize() == 0:
            return -1
        lst = self.listToArray()
        for i in range(len(lst)):
            if val == lst[i]:
                return i
        return -1

    """returns the root of the tree representing the list

    @rtype: AVLNode
    @returns: the root, None if the list is empty
    """

    def getRoot(self) -> AVLNode:
        return self.root

    def setRoot(self, new_root):
        self.root = new_root
