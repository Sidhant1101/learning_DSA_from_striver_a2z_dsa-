# subsecquence is set of elements (sub set ) but in the same order of array

# A subsequence is a sequence derived from another sequence or string by deleting some or no elements while keeping the relative order of the remaining elements intact.

array = [1, 4, 2]

def subsequence_array(i, sub_array):
    # Base case: if we've considered all elements
    if i >= len(array):
        print(sub_array)   # print the current subsequence
        return
    
    # Include array[i]
    sub_array.append(array[i])
    subsequence_array(i + 1, sub_array)
    
    # Backtrack: remove array[i] and explore without it
    sub_array.pop()
    subsequence_array(i + 1, sub_array)

def main():
    subsequence_array(0, [])
    
main()
