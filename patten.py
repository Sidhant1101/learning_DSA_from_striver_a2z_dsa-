def print_pattern_1(n):
    for i in range(n):
        for j in range(0,n-i-1):
            print(" ", end=" ")
        for j in range(0,i*2+1):
            print("*", end=" ")
        for j in range(0,n-i-1):
            print(" ", end=" ")
        print()
def print_pattern_2(n):
    for i in range(n):
        for j in range(0,i+1):
            print("*", end=" ")
        print()
def print_pattern_3(n):
    for i in range(n):
        for j in range(i):
            print(" ", end=" ")
        for j in range(2*n-1-i*2):
            print("*", end=" ")
        for j in range(i):
            print(" ", end=" ")
        print()

def print_pattern_4(n):
    for i in range(n):
        for j in range(0,n-i-1):
            print(" ", end=" ")
        for j in range(0,i*2+1):
            print("*", end=" ")
        for j in range(0,n-i-1):
            print(" ", end=" ")
        print()
    for i in range(n-2,-1,-1):
        for j in range(0,n-i-1):
            print(" ", end=" ")
        for j in range(0,i*2+1):
            print("*", end=" ")
        for j in range(0,n-i-1):
            print(" ", end=" ")
        print()


def print_pattern_5(n):
    for i in range(n):
        for j in range(i+1):
            print(i, end=" ")
        print()

def print_pattern_6(n):
    for i in range(1, n+1):
        for j in range( i):
            print(i, end=" ")
        for j in range(n-i):
            print(" "*2, end="  ")
        for j in range(i):
            print(i, end=" ")
        print()
print_pattern_6(5)