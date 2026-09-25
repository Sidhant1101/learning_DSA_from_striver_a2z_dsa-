#Check if a number is a palindrome using string conversion in Python. A palindrome is a number that reads the same backward as forward. Here is an example of how to check if a number is a palindrome:
def is_palindrome(num):
    # Convert the number to a string
    num_str = str(num)
    # Get the reversed string
    reversed_str = num_str[::-1]
    # Check if the original and reversed strings are equal
    return num_str == reversed_str

# Test the function
print(is_palindrome(12321))  # prints True
print(is_palindrome(12345))  # prints False



#checking if a number is a palindrome without converting it to a string can be done using mathematical operations. Here is an example of how to check if a number is a palindrome using integer division and modulus:

def is_palindrome_math(num):
    # Store the original number
    original_num = num
    reversed_num = 0
    while num > 0:
        digit = num % 10  # get the last digit
        reversed_num = reversed_num * 10 + digit  # append it to the reversed number
        num = num // 10  # remove the last digit
    # Check if the original and reversed numbers are equal
    return original_num == reversed_num

# Test the function
print(is_palindrome_math(12321))  # prints True
print(is_palindrome_math(12345))  # prints False