import math
import os
import random
import re
import sys

def consecutive_ones(n):
    if not n:
        return 0
    binary = bin(n)[2:]
    
    return len(max(binary.replace('0',' ').split(), key = len))
        

if __name__ == '__main__':
    n = int(input("Enter Number: "))
    Consecutive_1s = consecutive_ones(n)
    print(Consecutive_1s)
