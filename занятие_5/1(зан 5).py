#!/usr/bin/python3
# -- coding: utf-8 --
n = int(input('Введите N: '))
def main(n):
    for i in range(n):
        if i**2 <= n:
            print(i**2)
main(n)
