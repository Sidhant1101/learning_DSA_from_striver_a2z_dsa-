count = 0


def void():
    global count
    if count == 5:
        return
    count += 1
    print(1)
    void()


def main():
    void()
    


print(main())