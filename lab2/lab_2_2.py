def heap_max(arr):
    return arr[0]


heap_size = 0
tree_array_size = 20
INF = 100000


# function to get right child of a node of a tree
def get_right_child(A, index):
    if (((2 * index) + 1) < len(A)) and (index >= 1):
        return (2 * index) + 1
    return -1


# function to get left child of a node of a tree
def get_left_child(A, index):
    if (((2 * index) < len(A)) and (index >= 1)):
        return 2 * index
    return -1


# function to get the parent of a node of a tree
def get_parent(A, index):
    if ((index > 1) and (index < len(A))):
        return index // 2
    return -1


def max_heapify(A, index):
    left_child_index = get_left_child(A, index)
    right_child_index = get_right_child(A, index)

    # finding largest among index, left child and right child
    largest = index

    if ((left_child_index <= heap_size) and (left_child_index > 0)):
        if (A[left_child_index] > A[largest]):
            largest = left_child_index

    if ((right_child_index <= heap_size and (right_child_index > 0))):
        if (A[right_child_index] > A[largest]):
            largest = right_child_index

    # largest is not the node, node is not a heap
    if (largest != index):
        A[index], A[largest] = A[largest], A[index]
        max_heapify(A, largest)


def heap_sort(arr):
    n = len(arr)
    # maxheap
    for i in range(n, -1, -1):
        max_heapify(arr, i)
    # element extraction
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        max_heapify(arr, i)


def heap_extract_max(arr):
    temp_var = len(arr)
    if temp_var < 1:
        return print("queue is empty")
    maximum = arr[0]
    arr[0] = arr[temp_var - 1]
    temp_var -= 1
    max_heapify(arr, 1)
    return maximum


def increase_key(arr, index, key):
    arr[index - 1] = key
    while (index - 1 > 1) and (arr[get_parent(arr, index - 1)] < arr[index - 1]):
        arr[index - 1], arr[get_parent(arr, index - 1)] = arr[get_parent(arr, index - 1)], arr[index - 1]
        index = get_parent(arr, index - 1)


def decrease_key(A, index, key):
    A[index - 1] = key
    max_heapify(A, index)


def insert(arr, key):
    lol = len(arr)

    # arr[lol-1]=INF
    arr.append(key)
    lol += 1

    increase_key(arr, lol - 1, key)


A = [7]

insert(A, 15)
insert(A, 8)
insert(A, 10)
insert(A, 5)
insert(A, 7)
insert(A, 6)
insert(A, 2)
insert(A, 9)
insert(A, 56)
heap_sort(A)
print(A)
