from avl_template_new import AVLTreeList


def given_list_when_retrieve_element_then_return_element(self):
    lst = AVLTreeList()
    lst.insert("a", "a")
    print(self.list.retrieve(0), "a")