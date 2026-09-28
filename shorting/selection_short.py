
# Selection Sort is a straightforward, comparison-based sorting algorithm
# that works by repeatedly finding the minimum element from the unsorted portion of a list 
# and swapping it to its correct position at the fron
# How It Works
# 1 The algorithm conceptually splits the array into two halves:
# 2 A sorted section at the left (initially empty).
# 3 An unsorted section at the right (initially containing the entire list).

def slection_short(array):
    
    for i in range(len(array)-1):
        
        mini = i
        for j in range(i,len(array)):
            if array[i]>array[j]:
                mini = j
        array[mini],array[i] = array[i],array[mini]
                
    return array

def main():
    array = [13,42,2,56,9,20,1]
    slection_short(array)
    print(array)
    
main()


# here time complaxicity is n2 
# hence this algorithim is considred as the wost algorithim for shorting
# Selection Sort
# -------------------------
# Time Complexity:
# Best:    O(n²)
# Average: O(n²)
# Worst:   O(n²)

# Space Complexity:
# O(1)

# In-place: Yes
# Stable: Usually No