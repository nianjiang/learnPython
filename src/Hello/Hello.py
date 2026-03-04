#!/usr/bin/python3

import time


def hello():
    print("Hello, World!\t " + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))



def printTime():
    # 格式化成2016-03-20 11:45:39形式
    print (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

