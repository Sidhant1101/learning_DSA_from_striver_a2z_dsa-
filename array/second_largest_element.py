def largest_element(array,n,):
    
    for i in range(n-1):
        
        max = 0
        for j in range(0,len(array)):
            if array[max] < array[j]:
                max = j
        array[max],array[0] = array[0],array[max]
        
        return array

def main_():
    array = [13,42,2,56,9,20,0,1]
    n = 2
    largest_element(array,n)
    print(array[n-1])
    
main_()

# another better way for finding the second largest element in an array is to use a single pass through the array while keeping track of the largest and second largest elements. Here's how you can implement it:


def second_largest_element(array):
    
    
        
        largest = array[0]
        second_largest = -1
        
        for i in range(1,len(array)):
            if array[i] > largest:
               largest ,second_largest =array[i] , largest
              
            elif array[i] > second_largest and array[i]!=largest:
                second_largest = array[i]  
      
        return second_largest

def main():
    array = [13,42,2,45,56,9,20,0,1]
    print(second_largest_element(array))
    # print(array)
    
main()
