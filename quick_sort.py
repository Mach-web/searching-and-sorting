"""Implement quick sort in Python.
Input a list.
Output a sorted list."""
'''
I implemented quick sort by use of a recursive function
'''
def quicksort(arr):
    # This would only be implemented if the left or right array has only one value remaining
    if len(arr) <= 1:
        return arr
    else:
        # by convention the pivot is the last element of array
        pivot = -1
        start_index = 0
        pivot_value = arr[pivot]
        bfr_pivot = pivot - 1
        '''Swap the values in case pivot is less than the start.
        Assign start as next index if pivot is greater'''
        while arr[start_index] < arr[pivot]:
            start_index += 1
        while arr[start_index] > arr[pivot]:
            start = arr[start_index]
            arr[start_index] = arr[bfr_pivot]
            arr[bfr_pivot] = arr[pivot]
            arr[pivot] = start
            pivot -= 1
            bfr_pivot = pivot - 1
            # after swapping assign the start as the next value in the array so that comparison is done with pivot
            while arr[start_index] < arr[pivot]:
                start_index += 1
        '''
        Get the index of pivot which has already been sorted then use it to separate the array into left and right arrays.
        Repeat the function until the condition in the first statement is met.
        '''
        new_pivot_index = arr.index(pivot_value)
        left_arr = arr[:new_pivot_index]
        right_arr = arr[new_pivot_index + 1:]
        return quicksort(left_arr) + [pivot_value] + quicksort(right_arr)

test2 = [5, 21, 6, 19, 3]
test = [23, 4, 1, 3, 9, 20, 25, 6, 21, 14]
# test3 = [12, 43, 76, 23, 56, 200, 100, 76]
print(quicksort(test))
print(quicksort(test2))
# print(quicksort(test3))