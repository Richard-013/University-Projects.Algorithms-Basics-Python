def bubbleSort(data):
    for i in range(len(data), -1, -1):
        for j in range(i - 1):
            print("COMP:", j, end=' ')
            if data[j] > data[j+1]:
                temp = data[j+1]
                data[j+1] = data[j]
                data[j] = temp
                print("SWAPPED")
            else:
                print("NOT SWAPPED")
                continue

    return data

def mergeSort():
    pass

def quickSort():
    pass

