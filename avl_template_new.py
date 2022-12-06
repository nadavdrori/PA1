# username - nadavdrori
# id1      - 208935882
# name1    - Nadav Drori
# id2      - 318900883
# name2    - Omer Talmi


"""A class represnting a node in an AVL tree"""


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
        return self.value is not None


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

    # add your fields here

    """returns whether the list is empty

    @rtype: bool
    @returns: True if the list is empty, False otherwise
    """

    def empty(self):
        return self.getRoot() is None

    """retrieves the value of the i'th item in the list

    @type i: int
    @pre: 0 <= i < self.length()
    @param i: index in the list
    @rtype: str
    @returns: the the value of the i'th item in the list
    """

    def retrieve(self, i):
        return self.select(self.getRoot(), i + 1)

    def select(self, node, i):
        left_node_size = node.getLeft().getSize() + 1
        if left_node_size == i:
            return node
        elif left_node_size > i:
            return self.select(node.getLeft(), i)
        return self.select(node.getRight(), i - left_node_size)

    """inserts val at position i in the list

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
            self.root = AVLNode(val)
            inserted_node = self.root
        else:
            if i == self.length():
                inserted_node = self.insertLast(val)
            elif i < self.length():
                inserted_node = self.insert_in_middle(i, val)
        self.size += 1
        return self.rebalancing_tree(inserted_node)

    """inserts val at middle position in the list

            @type val: str
            @param val: the value we inserts
            @rtype: AVLNode
            @returns: the inserted node
            """

    def insert_in_middle(self, i, val):
        curr_node = self.retrieve(i)
        if curr_node.getLeft().getValue() is None:
            curr_node.setLeft(AVLNode(val))
            curr_node.getLeft().setParent(curr_node)
            return curr_node.getLeft()
        else:
            pred = self.retrieve(i - 1)  # TODO - compare complexity retrieve\predecessor function
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
        while curr_node.getRight().getValue() is not None:
            curr_node = curr_node.getRight()
        curr_node.setRight(AVLNode(val))
        curr_node.getRight().setParent(curr_node)
        return curr_node.getRight()

    def rebalancing_tree(self, node):
        rebalancing_count = 0
        while node is not None:
            self.update_height_and_size(node)
            if abs(node.getLeft().getHeight() - node.getRight().getHeight()) > 1:
                rebalancing_count += 1
                self.rebalance(node)
            node = node.parent
        return rebalancing_count

    def rebalance(self, node):
        if node.getLeft().getHeight() > node.getRight().getHeight():
            if node.getLeft().getLeft().getHeight() > node.getLeft().getRight().getHeight():
                self.right_rotation(node)
            else:
                self.left_right_rotation(node)
        else:
            if node.getRight().getRight().getHeight() > node.getRight().getLeft().getHeight():
                self.left_rotation(node)
            else:
                self.right_left_rotation(node)

    def right_rotation(self, node):
        left_child = node.getLeft()
        left_child.setParent(node.parent)
        if node.getParent() is not None:
            if node.getParent().getLeft() == node:
                node.getParent().setLeft(left_child)
            else:
                node.getParent().setRight(left_child)
        node.setLeft(left_child.getRight())
        left_child.setRight(node)
        self.update_height_and_size(node)
        self.update_height_and_size(left_child)
        if self.root == node:
            self.root = left_child

    def left_right_rotation(self, node):
        self.left_rotation(node.getLeft())
        self.right_rotation(node)

    def right_left_rotation(self, node):
        self.right_rotation(node.getRight())
        self.left_rotation(node)

    def left_rotation(self, node):
        right_child = node.getRight()
        right_child.setParent(node.getParent())
        if node.getParent() is not None:
            if node.getParent().getRight() == node:
                node.getParent().setRight(right_child)
            else:
                node.getParent().setLeft(right_child)
        node.setRight(right_child.getLeft())
        right_child.setLeft(node)
        self.update_height_and_size(node)
        self.update_height_and_size(right_child)
        if self.root == node:
            self.root = right_child

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
        return -1

    """returns the value of the first item in the list

    @rtype: str
    @returns: the value of the first item, None if the list is empty
    """

    def first(self):
        return None

    """returns the value of the last item in the list

    @rtype: str
    @returns: the value of the last item, None if the list is empty
    """

    def last(self):
        return None

    """returns an array representing list 

    @rtype: list
    @returns: a list of strings representing the data structure
    """

    def listToArray(self):
        return None

    """returns the size of the list 

    @rtype: int
    @returns: the size of the list
    """

    def length(self):
        return self.size

    """sort the info values of the list

    @rtype: list
    @returns: an AVLTreeList where the values are sorted by the info of the original list.
    """

    def sort(self):
        return None

    """permute the info values of the list 

    @rtype: list
    @returns: an AVLTreeList where the values are permuted randomly by the info of the original list. ##Use Randomness
    """

    def permutation(self):
        return None

    """concatenates lst to self

    @type lst: AVLTreeList
    @param lst: a list to be concatenated after self
    @rtype: int
    @returns: the absolute value of the difference between the height of the AVL trees joined
    """

    def concat(self, lst):
        return None

    """searches for a *value* in the list

    @type val: str
    @param val: a value to be searched
    @rtype: int
    @returns: the first index that contains val, -1 if not found.
    """

    def search(self, val):
        return None

    """returns the root of the tree representing the list

    @rtype: AVLNode
    @returns: the root, None if the list is empty
    """

    def getRoot(self):
        return self.root
