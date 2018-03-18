# 왜 안 풀리는지 고민해야 겠다 2018.03.18
def isRight(n):
    for i in range(1,101):
        if i ** 2 == n: return i
    return -1

M, N = [int(x) for x in input().split()]
l = [x for x in range(M,N+1) if isRight(x) != -1]

if len(l) == 0: print(-1)
else: print(sum(l),min(l),sep="\n")

"""
def isRight(n):
    for i in range(1,101):
        if i ** 2 == n: return i
    return -1

M, N = [int(x) for x in input().split()]
l = []
x = M
while x <= N:
	if isRight(x) != -1: l.append(x)
	x += 1
if len(l) == 0: print(-1)
else: print(sum(l),min(l),sep="\n")
"""