from avl_template_new import AVLTreeList


def given_list_when_retrieve_element_then_return_element():
    lst = AVLTreeList()
    lst.insert(0, "a")
    print(lst.retrieve(0) is "a")


given_list_when_retrieve_element_then_return_element()
