# sum of first n number using different methods in recrusion

# parametrized way

def sum_of_n(n, total=0):
    if n == 0:
        return total
    else:
        return sum_of_n(n - 1, total + n)
    
def main():
    n=5
    result = sum_of_n(n)
    print(f"Sum of first {n} numbers is: {result}")
    
main()