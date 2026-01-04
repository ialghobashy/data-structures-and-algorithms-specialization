def fibonacci_number(n):
    fib = [0, 1]
    for i in range(2, n+1):
        fib.append(fib[i-1]+fib[i-2])
    return fib[n]
def fibonacci_last_digit(n):
    fib = [0, 1]
    for i in range(2, n+1):
        fib.append((fib[i-1]+fib[i-2])%10)
    return fib[n]


for i in range(25):
    print(fibonacci_number(i), fibonacci_last_digit(i))