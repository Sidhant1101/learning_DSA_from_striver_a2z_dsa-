# visuvalising what actually hashing do 


def hashing(arr):
    key = []
    value = []

    for i in range(len(arr)):
        if arr[i] in key:
            index = key.index(arr[i])
            value[index] += 1
        else:
            key.append(arr[i])
            value.append(1)

    return dict(zip(key, value))


arr = [1,5,3,5,1,6,1,3,1,4,2,6,2,4,3,6]

def main():
    result = hashing(arr)
    print(result)

main()