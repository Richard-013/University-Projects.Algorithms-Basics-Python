def linearSearch(target, data):
    '''Linear search that returns the item desired'''
    for item in data:
        if item == target:
            return item

    return None

def linearSearchBool(target, data):
    '''Linear search that returns true or false depending on
       if the item is present in the list or not'''
    for item in data:
        if item == target:
            return True

    return False

def binarySearch(target, data):
    '''Iterative binary search to find item in sorted list and
       return its value'''
    start = 0
    end = len(data) - 1

    while start <= end:
        #Calculates midpoint within the list
        midpoint = start + ((end - start) // 2)
        if data[midpoint] == target:
            return data[midpoint]
        elif data[midpoint] < target:
            start = midpoint + 1
        else:
            end = midpoint - 1

    return None
    

inputData = [43, 67, 12, 34, 76, 4, 19, 7, 200, 38]

#Linear Search Test
#Standard
print(linearSearch(43, inputData))
print(linearSearch(19, inputData))
print(linearSearch(569, inputData))

print("-------")
#Bool
print(linearSearchBool(38, inputData))
print(linearSearchBool(12, inputData))
print(linearSearchBool(8, inputData))
