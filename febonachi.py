# generating the cod for the fibonacci series using multiple recurtion method

def febonachi(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
   
    return  febonachi(n-1)+febonachi(n-2)
        
def main():
    print(febonachi(10))
main()