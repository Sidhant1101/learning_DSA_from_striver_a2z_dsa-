# swaping the array
arr = [1,2,3,4,5]
def reverse_array(l,r):
    if l>=r:
        return
    arr[l],arr[r] = arr[r],arr[l]
    reverse_array(l+1,r-1)
    
  
def main():
    global arr
    arr = [1,2,3,4,5]
    reverse_array(0,len(arr)-1)
    print(arr)
main()
    
# swaping by single pointer

def reverse_array_single_pointer(i):
    if i>=len(arr)//2:
        return
    arr[i],arr[len(arr)-1-i] = arr[len(arr)-1-i],arr[i]
    reverse_array_single_pointer(i+1)
    
def main():
    global arr
    arr = [1,2,3,4,5,6]
    reverse_array_single_pointer(0)
    print(arr)
main()