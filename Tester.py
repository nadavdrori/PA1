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
    print(lst.getRoot().getValue() == "b")
    print(lst.getRoot().getRight().getValue() == "a")


def given_balanced_tree_when_delete_element_then_rotate():
    lst = AVLTreeList()
    lst.insert(0, "a")
    lst.insert(0, "b")
    lst.insert(0, "c")
    lst.delete(2)
    print(lst.getRoot().getValue() == "b")
    print(lst.getRoot().getLeft().getValue() == "c")


def given_balanced_tree_when_delete_one_son_element_then_rotate():
    lst = AVLTreeList()
    lst.insert(0, "a")
    lst.insert(1, "b")
    lst.insert(2, "c")
    lst.insert(3, "d")
    lst.delete(2)
    print(lst.getRoot().getValue() == "b")
    print(lst.getRoot().getRight().getValue() == "d")


def given_balanced_tree_when_delete_two_sons_element_then_delete():
    lst = AVLTreeList()
    lst.insert(0, "a")
    lst.insert(1, "b")
    lst.insert(2, "c")
    lst.insert(2, "d")
    lst.insert(4, "e")
    lst.delete(3)
    print(lst.getRoot().getValue() == "b")
    print(lst.getRoot().getRight().getValue() == "e")
    print(lst.getRoot().getRight().getLeft().getValue() == "d")


def given_balanced_tree_when_delete_two_sons_element_then_rotate():
    lst = AVLTreeList()
    lst.insert(0, "a")
    lst.insert(0, "b")
    lst.insert(2, "c")
    lst.insert(0, "d")
    lst.insert(2, "e")
    lst.insert(4, "f")
    lst.insert(6, "j")
    lst.insert(5, "t")
    lst.delete(3)
    print(lst.getRoot().getValue() == "f")
    print(lst.getRoot().getRight().getLeft().getValue() == "t")


def given_balanced_tree_when_get_first_then_return_right_value():
    lst = AVLTreeList()
    lst.insert(0, "a")
    lst.insert(0, "b")
    lst.insert(2, "c")
    lst.insert(0, "d")
    lst.insert(2, "e")
    lst.insert(4, "f")
    lst.insert(6, "j")
    lst.insert(5, "t")
    print(lst.first().getValue() == "d")
    lst.insert(1, "one")
    print(lst.first().getValue() == "d")
    lst.insert(0, "z")
    print(lst.first().getValue() == "z")


def given_balanced_tree_when_get_last_then_return_right_value():
    lst = AVLTreeList()
    lst.insert(0, "a")
    lst.insert(0, "b")
    lst.insert(2, "c")
    lst.insert(0, "d")
    lst.insert(2, "e")
    lst.insert(4, "f")
    lst.insert(6, "j")
    lst.insert(5, "t")
    print(lst.last().getValue() == "j")
    lst.insert(7, "s")
    print(lst.last().getValue() == "j")
    lst.insert(9, "n")
    print(lst.last().getValue() == "n")


def given_sorted_lst_when_create_tree_then_get_valid_tree():
    lst = [1, 2, 3, 4, 5, 6, 7]
    tree = AVLTreeList()
    tree.create_tree_from_sorted_lst(lst)
    print((tree.getRoot().getValue() == 4))


def given_tree_when_sort_then_get_sorted_tree():
    lst = AVLTreeList()
    lst.insert(0, "a")
    lst.insert(0, "b")
    lst.insert(2, "c")
    print(lst.sort().getRoot().getValue() == "b")
    print(lst.sort().getRoot().getLeft().getValue() == "a")
    print(lst.sort().getRoot().getRight().getValue() == "c")


def given_tree_when_convert_to_list_then_get_valid_list():
    lst = AVLTreeList()
    org_lst = []
    lst.insert(0, "a")
    lst.insert(0, "b")
    lst.insert(2, "c")
    lst.insert(0, "d")
    lst.insert(2, "e")
    lst.insert(4, "f")
    lst.insert(6, "j")
    lst.insert(5, "t")

    org_lst.insert(0, "a")
    org_lst.insert(0, "b")
    org_lst.insert(2, "c")
    org_lst.insert(0, "d")
    org_lst.insert(2, "e")
    org_lst.insert(4, "f")
    org_lst.insert(6, "j")
    org_lst.insert(5, "t")
    print(lst.listToArray() == org_lst)


def test_concat():
    lst1 = AVLTreeList()
    lst2 = AVLTreeList()
    lst1.insert(0, "a")
    lst1.insert(0, "b")
    lst1.insert(2, "c")
    lst1.insert(0, "d")
    lst1.insert(2, "e")
    lst1.insert(4, "f")
    lst1.insert(5, "t")
    lst1.insert(5, "h")
    lst1.insert(7, "j")
    lst1.insert(3, "i")
    lst1.insert(3, "o")

    lst2.insert(0, "z")
    lst2.insert(0, "w")
    lst2.insert(2, "n")
    lst2.insert(0, "m")
    lst2.insert(2, "k")
    lst2.insert(4, "l")
    lst2.insert(6, "s")

    return lst1.concat(lst2)

def search_test():
    lst1 = AVLTreeList()
    print(lst1.search("a"))
    print(lst1.search("h"))
    print(lst1.search("k"))
    print(lst1.search("l"))
    print(lst1.search("j"))
    print(lst1.search("o"))
    print(lst1.search('a'))


def given_tree_need_left_right_rotation_when_insert_then_get_valid_rotation_amount():
    lst = AVLTreeList()
    lst.insert(0, "a")
    lst.insert(0, "b")
    print(lst.insert(1, "c") == 2)

    lst = AVLTreeList()
    lst.insert(0, "a")
    lst.insert(0, "b")
    print(lst.insert(0, "c") == 1)

def test_shuffle():
    lst = AVLTreeList()
    lst.insert(0, "a")
    lst.insert(0, "b")
    lst.insert(2, "c")
    print(lst.permutation().getRoot().getValue())
#
# given_balanced_tree_when_delete_element_then_rotate()
# given_list_when_retrieve_element_then_return_element()
# given_balanced_tree_when_insert_element_then_rotate()
# given_balanced_tree_when_delete_two_sons_element_then_rotate()
# given_balanced_tree_when_delete_two_sons_element_then_delete()
# given_balanced_tree_when_delete_one_son_element_then_rotate()
#
# given_balanced_tree_when_get_first_then_return_right_value()
# given_balanced_tree_when_get_last_then_return_right_value()
# given_sorted_lst_when_create_tree_then_get_valid_tree()
# given_tree_when_convert_to_list_then_get_valid_list()
# given_tree_when_sort_then_get_sorted_tree()

print(test_concat())
# search_test()


# given_tree_need_left_right_rotation_when_insert_then_get_valid_rotation_amount()
test_shuffle()
