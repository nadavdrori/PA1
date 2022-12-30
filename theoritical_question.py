from random import randint

from avl_template_new import AVLTreeList


def insert_to_list_n_times(lst, n):
    rotations_count = 0
    for i in range(n):
        index = randint(0, i)
        rotations_count += lst.insert(index, str(i))
    return rotations_count


def measure_inserts():
    lst = AVLTreeList()
    for i in range(10):
        print("index " + str(i + 1) + " rotations: ")
        print(insert_to_list_n_times(lst, 1500 * (2 ** (i + 1))))


def measure_deletes():
    lst = AVLTreeList()
    for index in range(1, 3):
        n = 1500 * (2 ** index)
        insert_to_list_n_times(lst, n)
        print("index " + str(index) + " rotations: ")
        print(delete_from_list_n_times(lst, n))
        print("finish measure deletes")


def delete_from_list_n_times(lst, n):
    rotations_count = 0
    for i in reversed(range(0,n)):
        index = randint(0, i)
        rotations_count += lst.delete(index)
    return rotations_count

def measure_deletes_and_inserts():
    lst = AVLTreeList()
    for index in range(1, 11):
        count =0
        n = 1500 * (2 ** index)
        # n = 200
        count+=insert_to_list_n_times(lst, int(n/2))
        for i in reversed(range(0, int(n/4))):
            random = randint(0, i)
            count += lst.delete(random)
            random = randint(0, i)
            count += lst.delete(random)
        print("index " + str(index) + " rotations: ")
        print(count)

# measure_inserts()
# measure_deletes()
measure_deletes_and_inserts()