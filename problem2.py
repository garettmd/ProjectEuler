#!/usr/bin/env python


def fibs():
    first = 1
    second = 2
    nex = 1
    total = 2
    while first <= 4000000:
        nex = first+second
        if nex % 2 == 0:
            total = total + nex
        first = second
        second = nex
    return total


def main():
    print(fibs())
        

main()
