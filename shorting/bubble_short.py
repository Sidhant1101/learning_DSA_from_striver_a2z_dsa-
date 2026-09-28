# Bubble Sort is a simple sorting algorithm that repeatedly compares adjacent elements in a list and swaps them if they are in the wrong order.
# How Bubble Sort Works
# 1 The algorithm steps through the list item by item.
# 2 It compares each pair of adjacent elements.
# 3 If the first element is greater than the second,it swaps them.
# 4 Large values "bubble up" to the end of the list with each complete pass.
# 5 The process repeats until a full pass goes by without any swaps, meaning the list is fully sorted

def bubble_short(array):
    for i in range(len(array)-1,0,-1):
        didswap = 0 
        for j in range(i):
            if array[j]>array[j+1]:
                array[j+1],array[j]=array[j],array[j+1]
                didswap =1
        if didswap == 0:
            break
    return array


def main():
    array = [1,10,20]
    bubble_short(array)
    print(array)
    
main()

# Average: O(n²)
# Worst:   O(n²)