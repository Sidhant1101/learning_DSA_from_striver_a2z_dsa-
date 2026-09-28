# Insertion sort is a straightforward, comparison-based sorting algorithm that builds a final sorted array one element at a time.
# It works similarly to the way you might sort a hand of playing cards:
# you pick up one card from an unsorted pile and slide it into its exact correct position within your already sorted hand.
# How the Algorithm Works
# 1 Assume the first element in the array is already sorted.
# 2 Move to the next element (the "key").
# 3 Compare the key with the elements to its left (the sorted portion).
# 4 Shift all elements that are greater than the key one position to the right to make space.
# 5 Insert the key into its correct relative position.
# 6 Repeat steps 2–5 until the entire array is sorted


def insertion_short(array):
    for i in range(len(array)-1):
        for j in range(i,0,-1):
             if array[j]>array[j+1]:
                array[j+1],array[j]=array[j],array[j+1]
                
    return array


def main():
    array = [1,10,20]
    insertion_short(array)
    print(array)
    
main()


# Time Complexity:
# Best Case: O(n) – Occurs when the array is already sorted.
# The inner loop never triggers because no elements need shifting.
# Average Case: O(n²) – Occurs when elements are randomly distributed.
# Worst Case: O(n²) – Occurs when the array is sorted in reverse order