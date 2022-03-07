import time

#Recursion-----------------
def Recursion(n):
    if n <= 1:
        return n
    return n + Recursion(n-1)

print(Recursion(998))

#Iteration-----------------

def Iteration(n):
    first = 1
    second = 2
    nextnum = first + second
    if n == 1:
        return first
    if n == 2:
        return nextnum
    for i in range(n-2):
        second = second +1
        nextnum = nextnum + second
    return nextnum

start = time.time()
print(Iteration(5000000))
end = time.time()

print(end - start)

#Formula-----------------

def Formula(n):
    return int((n *(n+1))/2)

start = time.time()
print(Formula(5000000))
end = time.time()

print(end - start)