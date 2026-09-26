# printing all the subsecquence whoes sum is k
array = [3,5,7,9,1,2,4,6,3,9,4]
k= 8
def subsecquence_sum(i,sub_array):
  
    if i>=len(array):
        if sum(sub_array)==k:
            print(sub_array)
        
        return
    sub_array.append(array[i])
    subsecquence_sum(i+1,sub_array)
    
    sub_array.pop()
    subsecquence_sum(i+1,sub_array)
    
def main():
    subsecquence_sum(0,[])
    
main()



# diff method without using sum function

array = [1,2,3,4,5]
k= 3
s=0
def subsecquence_sum(i,sub_array,s):
  
    if i>=len(array):
        if s==k:
            print(sub_array)
        
        return
    sub_array.append(array[i])
    s = s+array[i]
    subsecquence_sum(i+1,sub_array,s)
    
    sub_array.pop()
    s = s-array[i]
    subsecquence_sum(i+1,sub_array,s)
    
def main():
    subsecquence_sum(0,[],s)
    
main()

# subsecquence giving first sum 

array = [1,2,3,4,5]
k= 3
s=0
def subsecquence_sum(i,sub_array,s):
  
    if i>=len(array):
        if s==k:
            print(sub_array)
            return True
        return False
    sub_array.append(array[i])
    s = s+array[i]
    if subsecquence_sum(i+1,sub_array,s):
        return True
    
    sub_array.pop()  
    s = s-array[i]
    if subsecquence_sum(i+1,sub_array,s):
        return True
    return False
def main():
    subsecquence_sum(0,[],s)
    
main()

# #give me the count of subsecquence which has sum is equals to k


array = [1,2,3,46]
k= 3
s=0
def subsecquence_sum(i,sub_array,s):
  
    if i>=len(array):
        if s==k:
           return 1
        return 0
    
    s = s+array[i]
    r =subsecquence_sum(i+1,sub_array,s)
        
   
    s = s-array[i]
    l = subsecquence_sum(i+1,sub_array,s)
        
    return l + r
def main():
    count= subsecquence_sum(0,[],s)
    print(count)
main()