def recCount(x):
    if x == 0:
        print("BOOOOM!")
        return None
    else:
        print(x, ".......")
        recCount(x - 1)

def power(num, pwr):
    if pwr == 0:
        return 1
    else:
        return num * power(num, pwr - 1)

def factorial(num):
    if num == 1:
        return 1
    else:
        return num * factorial(num - 1)

print("3 to the power of 7 is:", power(3, 7))
print("7! is:", factorial(7))
