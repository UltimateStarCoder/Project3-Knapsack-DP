def fib(n):
    first = 0
    second = 1

    for _ in range(2, n):
        temp = first + second
        first = second
        second = temp
    return first + second

print(fib(7))

def fib_recursion(n):
    if n < 2:
        return n
    return fib_recursion(n - 1) + fib_recursion(n - 2)

print(fib_recursion(7))