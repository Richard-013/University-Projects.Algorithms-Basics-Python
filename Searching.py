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

