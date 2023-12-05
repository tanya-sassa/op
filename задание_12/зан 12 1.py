def modulo(a, b):
    if a < b:
        return a
    else:
        return modulo(a - b, b)
a=int(input())
b=int(input())
result = modulo(a, b)
print(result)
