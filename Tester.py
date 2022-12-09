from avl_template_new import AVLTreeList


def given_list_when_retrieve_element_then_return_element():
    lst = AVLTreeList()
    lst.insert(0, "a")
    print(lst.retrieve(0).getValue() == "a")

def given_balanced_tree_when_insert_element_then_rotate():
    lst = AVLTreeList()
    lst.insert(0, "a")
    lst.insert(0, "b")
    lst.insert(0, "c")
    print(lst.getRoot().getValue()=="b")
    print(lst.getRoot().getRight().getValue()=="a")


def given_balanced_tree_when_delete_element_then_rotate():
    lst = AVLTreeList()
    lst.insert(0, "a")
    lst.insert(0, "b")
    lst.insert(0, "c")
    lst.delete(2)
    print(lst.getRoot().getValue()=="b")
    print(lst.getRoot().getLeft().getValue()=="c")

def given_balanced_tree_when_delete_one_son_element_then_rotate():
    lst = AVLTreeList()
    lst.insert(0, "a")
    lst.insert(1, "b")
    lst.insert(2, "c")
    lst.insert(3, "d")
    lst.delete(2)
    print(lst.getRoot().getValue()=="b")
    print(lst.getRoot().getRight().getValue()=="d")




#given_balanced_tree_when_delete_element_then_rotate()
# given_list_when_retrieve_element_then_return_element()
# given_balanced_tree_when_insert_element_then_rotate()
given_balanced_tree_when_delete_one_son_element_then_rotate()
