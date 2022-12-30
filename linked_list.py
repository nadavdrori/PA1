class Node:
    def __init__(self, val):
        self.value = val
        self.next = None

    def __repr__(self):
        return str(self.value)



class Linked_list:
    def __init__(self, seq=None):
        self.head = None
        self.size = 0
        if seq != None:
            for x in seq[::-1]:
                self.add_at_start(x)


    def __repr__(self):
        out = ""
        p = self.head
        while p != None:
            out += p.__repr__() + ", "  
            p = p.next
        return "[" + out[:-2] + "]"  # discard the extra ", " at the end


    def add_at_start(self, val):
        ''' add node with value val at the list head '''
        tmp = self.head
        self.head = Node(val)
        self.head.next = tmp
        self.size += 1


    def __len__(self):
        ''' called when using Python's len() '''
        return self.size


    def index(self, val):
        ''' find index of (first) node with value val in list
            return None of not found '''
        p = self.head
        i = 0     # we want to return the location
        while p != None:
            if p.value == val:
                return i
            else:
                p = p.next
                i += 1   
        return None # in case val not found


    def __getitem__(self, i):
        ''' called when reading L[i] 
            return value of node at index 0<=i<len '''
        assert 0 <= i < len(self)
        p = self.head
        for j in range(0, i):
            p = p.next
        return p.value


    def __setitem__(self, i, val):
        ''' called when using L[i]=val (indexing for writing)
            assigns val to node at index 0<=i<len '''
        assert 0 <= i < len(self)
        p = self.head
        for j in range(0, i):
            p = p.next
        p.value = val
        return None


    def insert(self, i, val):
        ''' add new node with value val before index 0<=i<=len '''
        assert 0 <= i <= len(self)
        if i == 0:
            self.add_at_start(val) #makes changes to self.head
        else:
            p = self.head
            for j in range(0, i-1): # get to position i-1
                p = p.next
            # now add new element 
            tmp = p.next
            p.next = Node(val)
            p.next.next = tmp
            self.size += 1


    def append(self, val):
        self.insert(self.size, val)

        
    def pop(self, i):
        ''' delete element at index 0<=i<len '''
        assert 0 <= i < len(self)
        if i == 0:
            self.head = self.head.next # bypass first element
        else: # i >= 1
            p = self.head
            for j in range(0, i-1):
                p = p.next

            # now p is the element BEFORE index i
            p.next = p.next.next # bypass element at index i

        self.size -= 1


 
def test():
    lst = Linked_list()  #empty linked list
    lst.insert(0,3) #insert 3 at position 0
    lst.insert(0,5)
    lst.insert(1,4)
    lst.insert(2,7)
    print(len(lst))
    print(lst)
    print(lst[2])
    print(lst.index(7))    
    lst.pop(0) #remove element at position 0
    lst[1] = 999
    print(lst)

       


