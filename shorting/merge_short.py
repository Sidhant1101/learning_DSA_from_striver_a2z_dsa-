# Merge sort is an efficient, comparison-based, and stable sorting algorithm that operates on the divide-and-conquer principle.
# Invented by John von Neumann in 1945, it continuously splits an array into halves until single-element subarrays remain, then merges those subarrays back together in sorted order.
# How Merge Sort Works (Step-by-Step)
# 1 Divide: Split the unsorted list into two roughly equal halves.
# 2 Conquer: Recursively sort both halves by continuing to divide them until they each contain only a single element (a list with one element is inherently sorted).
# 3 Merge: Combine the two smaller sorted lists into a single, larger sorted list by comparing elements sequentially.
def merge_sort(array):

    def divide(array, low, high):

        if low >= high:
            return

        mid = (low + high) // 2

        divide(array, low, mid)
        divide(array, mid + 1, high)

        combine(array, low, mid, high)


    def combine(array, low, mid, high):

        left = low
        right = mid + 1

        new_array = []

        while left <= mid and right <= high:

            if array[left] <= array[right]:
                new_array.append(array[left])
                left += 1
            else:
                new_array.append(array[right])
                right += 1

        while left <= mid:
            new_array.append(array[left])
            left += 1

        while right <= high:
            new_array.append(array[right])
            right += 1

        for i in range(low, high + 1):
            array[i] = new_array[i - low]


    divide(array, 0, len(array) - 1)

    return array


def main():

    array = [13, 51,0,10, 1,3,65,23,7,90,4]

    print(merge_sort(array))


main()