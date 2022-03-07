import time

# Recursion-----------------
def Recursion(n):
    try:
        if n <= 1:
            return n
        return n + Recursion(n - 1)
    except RecursionError as re:
        return 0


start = time.time()
print(f"Recursion: {Recursion(998)}") # 998 is the highest value recursion can reach
end = time.time()

print(end - start)

# Iteration-----------------


def Iteration(n):
    first = 1
    second = 2
    nextnum = first + second
    if n == 1:
        return first
    if n == 2:
        return nextnum
    for i in range(n - 2):
        second = second + 1
        nextnum = nextnum + second
    return nextnum


start = time.time()
print(f"\nIteration: {Iteration(10000000)}")
end = time.time()

print(end - start)

# Formula-----------------


def Formula(n):
    return int((n * (n + 1)) / 2)


start = time.time()
print(f"\nFormula: {Formula(10000000)}")
end = time.time()

print(end - start)