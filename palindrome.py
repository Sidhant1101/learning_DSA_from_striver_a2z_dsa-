# check wather the string is palindrome or not

def is_palindrome(s):
    # base case
    if len(s) <= 1:
        return True
    # check first and last character
    if s[0] != s[-1]:
        return False
    # recursive call with the substring excluding first and last character
    return is_palindrome(s[1:-1])

def main():
    s = "racecar"
    if is_palindrome(s):
        print(f"{s} is a palindrome")
    else:
        print(f"{s} is not a palindrome")

if __name__ == "__main__":
    main()