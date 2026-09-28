# Quick Sort is a highly efficient, divide-and-conquer sorting algorithm. 
# It works by selecting a pivot element from the array and partitioning the remaining elements into two sub-arrays: those less than the pivot and those greater than the pivot.
# The process is then applied recursively to the sub-arrays.
# How Quick Sort Works (Step-by-Step)
# 1 Choose a Pivot: Pick an element (e.g., the last element, first element, or a random element).
# 2 Partition: Rearrange the array so that all elements smaller than the pivot go to the left, and all larger elements go to the right. The pivot is now in its final sorted position.
# 3 Recurse: Apply the same logic to the left and right sub-arrays until the entire array is sorted.

def quick_sort(array, low, high):

    if low >= high:
        return

    pivot_index = partition(array, low, high)

    quick_sort(array, low, pivot_index - 1)
    quick_sort(array, pivot_index + 1, high)


def partition(array, low, high):

    pivot = array[low]

    left = low + 1
    right = high

    while left <= right:

        while left <= high and array[left] <= pivot:
            left += 1

        while right >= low and array[right] > pivot:
            right -= 1

        if left < right:
            array[left], array[right] = array[right], array[left]

    array[low], array[right] = array[right], array[low]

    return right


def main():

    array = [13, 51, 0, 10, 1, 3, 65, 23, 7, 90, 4]

    quick_sort(array, 0, len(array) - 1)

    print(array)


main()