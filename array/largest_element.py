
def largest_element(array):
    
    # for i in range(len(array)-1):
        
        max = 0
        for j in range(0,len(array)):
            if array[max] < array[j]:
                max = j
        array[max],array[0] = array[0],array[max]
        
        return array

def main():
    array = [13,42,2,56,9,20,0,1]
    largest_element(array)
    print(array[0])
    
main()