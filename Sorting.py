def bubbleSort(data):
    '''Sorts a list of elements using the bubble sort algorithm'''
    for i in range(len(data), -1, -1): #Loop controlling the point to compare up to
        for j in range(i - 1): #Loop comparing values in the list
            print("COMP:", j, end=' ')
            if data[j] > data[j+1]:
                temp = data[j+1]
                data[j+1] = data[j]
                data[j] = temp
                print("SWAPPED")
            else:
                print("NOT SWAPPED")
                continue
        print(data)

    return data

def mergeSort(data):
    '''Sorts a list of elements using merge sort algorithm'''
    if len(data) > 1:
        #Splits list into two halves at the midpoint
        midpoint = len(data) // 2
        leftList = data[:midpoint]
        rightList = data[midpoint:]

        mergeSort(leftList)
        mergeSort(rightList)

        leftIndex = 0
        rightIndex = 0
        mergeIndex = 0

        #Compares and merges both lists
        while(leftIndex < len(leftList) and rightIndex < len(rightList)):
            if leftList[leftIndex] < rightList[rightIndex]:
                data[mergeIndex] = leftList[leftIndex]
                leftIndex += 1
            else:
                data[mergeIndex] = rightList[rightIndex]
                rightIndex += 1

            mergeIndex += 1

        #Adds in remaining elements from the left list
        while leftIndex < len(leftList):
            data[mergeIndex] = leftList[leftIndex]
            leftIndex += 1
            mergeIndex += 1

        #Adds in remaining elements from the right list
        while rightIndex < len(rightList):
            data[mergeIndex] = rightList[rightIndex]
            rightIndex += 1
            mergeIndex += 1

        print(data)
        return data
        

def quickSort():
    pass

inputData = [3, 8, 42, 9, 31, 12, 25]
print(inputData)
#print(bubbleSort(inputData))
print(mergeSort(inputData))

