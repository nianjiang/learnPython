#!/usr/bin/python3

import src.Hello.Hello as Hello

def main():
    # hello()
    packageHello()


def hello():
    print("Hello, World!")


def packageHello():
    Hello.hello()
    # Hello.printTime()



main()