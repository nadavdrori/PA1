import time
from random import randint

from avl_template_new import AVLTreeList


def insert_to_list_n_times(lst, n, index_to_insert):
    for i in range(n):
        lst.insert(index_to_insert, str(i))

def insert_to_list_n_times_in_random(lst, n):
    for i in range(n):
        index = randint(0, i)
        lst.insert(index, str(i))

def measure_inserts_in_begining():
    lst = AVLTreeList()
    for i in range(0,10):
        print("index " + str(i + 1) + " rotations: ")
        amount = 1500 * (2 ** (i + 1))
        start = time.time()
        insert_to_list_n_times(lst, amount, 0)
        end = time.time()
        print((end - start)/amount)


def measure_inserts_in_end():
    lst = AVLTreeList()
    for i in range(0,10):
        print("index " + str(i + 1) + " rotations: ")
        amount = 1500 * (2 ** (i + 1))
        start = time.time()
        index_to_insert = lst.getSize()-1
        if index_to_insert == -1:
            index_to_insert = 0
        insert_to_list_n_times(lst, amount, index_to_insert)
        end = time.time()
        print((end - start)/amount)


def measure_inserts_in_random():
    lst = AVLTreeList()
    for i in range(0,10):
        print("index " + str(i + 1) + " rotations: ")
        amount = 1500 * (2 ** (i + 1))
        start = time.time()
        insert_to_list_n_times_in_random(lst, amount)
        end = time.time()
        print((end - start)/amount)
# measure_inserts_in_begining()
# measure_inserts_in_end()
measure_inserts_in_random()