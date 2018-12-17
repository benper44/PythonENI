
limite= input("Quel est la limite: ")


def fibonacci(n):
    a = 0
    b = 1
    for i in range(0, n):
        temp = a
        a = b
        b = temp + b
    return a


for c in range(0, 1000):
    if fibonacci(c) <= limite:
        print fibonacci(c)
    
