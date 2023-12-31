import random
import time

# Naive Search: simply scanning every single element and ask if equal to the target search
#  if Yes, return index
#  if No, return -1

def naive_search(list, target):
    # example list = [1, 3, 10, 12]
    for i in range(len(list)):
        if list[i] == target:
            return i
    return -1

# Binary Search is an algorithm that search an unordered list faster than Naive search
# return the index of wanted item in the list
# our list will be SORTED
# (parameters: low and high are indices)


def binary_search(list, target, low=None, high=None):
    if low is None:
        low = 0
    if high is None:
        high = len(list) - 1

    if high < low:
        return -1

    # midpoint = len(list) // 2  # index 2
    midpoint = (low + high) // 2

    if list[midpoint] == target:
        return midpoint
    elif target < list[midpoint]:
        # recurse binary search for the lower half if target belongs there
        return binary_search(list, target, low, midpoint-1)
    else:
        # target > l[midpoint]
        return binary_search(list, target, midpoint+1, high)


if __name__=="__main__":
    # list = [1, 3, 5, 10, 12]
    # target = 10
    # print(naive_search(list, target))
    # print(binary_search(list, target))

    length = 10000
    # build a sorted list of length 10000
    sorted_list = set()
    while len(sorted_list) < length:
        sorted_list.add(random.randint(-3*length, 3*length))
    sorted_list = sorted(list(sorted_list))

    # run Naive Search
    start = time.time()
    for target in sorted_list:
        naive_search(sorted_list, target)
    end = time.time()
    print("Naive search time: ", (end - start)/length, "seconds")

    # run Binary Search
    start = time.time()
    for target in sorted_list:
        binary_search(sorted_list, target)
    end = time.time()
    print("Binary search time: ", (end - start)/length, "seconds")