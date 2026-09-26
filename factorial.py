def factorial(n):
    # 1. Base Case: stops the infinite loop
    if n == 1 or n == 0:
        return 1
    
    # 2. Recursive Case: function calls itself
    else:
        return n * factorial(n - 1)

# Test the function
print(factorial(5))  # Output: 120
