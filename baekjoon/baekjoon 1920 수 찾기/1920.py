import sys

N = int(sys.stdin.readline())
Nset = set(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
Mlist = list(map(int, sys.stdin.readline().split()))

for i in Mlist:
    if i in Nset:
        print(1)
    else:
        print(0)
