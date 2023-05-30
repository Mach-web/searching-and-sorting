"""You're going to write a binary search function.
You should use an iterative approach - meaning
using loops.
Your function should take two inputs:
a Python list to search through, and the value
you're searching for.
Assume the list only has distinct elements,
meaning there are no repeated values, and
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list."""

def binary_search(input_array, value):
    """Your code goes here."""
    """ def find_factor(arr):
        if len(arr) % 2 == 1:
            return odd
        else:
            return even
    if find_factor(input_array) == odd:
        mid_value = len(input_array) // 2
        if value < mid_value:
            new_arr = input_array[:mid_value] 
        """


    index = None
    for i in range(0, len(input_array)):
        if value == input_array[i]:
            index = i
            return index
            break
    if index is None:
        return -1
test_list = [1,3,9,11,15,19,29]
test_val1 = 25
test_val2 = 15
print(binary_search(test_list, test_val1))
print(binary_search(test_list, test_val2))