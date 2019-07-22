def linearSearch(target, data):
    for item in data:
        if item == target:
            return item

    return None

def linearSearchBool(target, data):
    for item in data:
        if item == target:
            return True

    return False

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
