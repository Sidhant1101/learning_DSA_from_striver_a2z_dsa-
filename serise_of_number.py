# to print the series of numbers from 1 to n using recursion.

#forward recursion

def void(i,n):
   
    if i==n:
        return
    print(i,end=" ")
    void(i+1,n)
    
def main():
    void(1,5)
    
main()

# backward recursion back tracking

def void(i,n):
   
    if i==n:
        return
  
    void(i+1,n)
    print(i,end=" ")
def main():
    void(1,5)
    
main()

# fractional method to find the sum of first n numbers using recursion

def sum_of_n_fractions(n):
    if n == 0:
        return 0
    else:
        return n + sum_of_n_fractions(n - 1)
    
def main():
    n=5
    result = sum_of_n_fractions(n)
    print(f"Sum of first {n} numbers is: {result}")
    
main()
