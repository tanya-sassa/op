#!/usr/bin/python3
# -- coding: utf-8 --
def main():
    i = 1
    n = 0
    list = []
    while i != 0:
        i = int(input('Введите число последовательности: '))
        n += 1
        list.append(i)
    return (sum(list)/(n-1))
print(main())
