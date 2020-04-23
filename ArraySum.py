import sys

def sumArr (inp):
    sum = 0
    for i in inp:
       sum += i

n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))

tot = sumArr()
