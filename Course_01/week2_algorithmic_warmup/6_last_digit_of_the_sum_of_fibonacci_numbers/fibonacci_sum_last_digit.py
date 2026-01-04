def fibonacci_sum(n):
    # Using the identity: Sum(F_0 to F_n) = F(n+2) - 1
    # The last digit of Fibonacci sequence repeats every 60 numbers (Pisano Period for m=10)
    # We reduce the index (n + 2) modulo 60
    n = (n + 2) % 60
    
    if n <= 1:
        fib_n_plus_2 = n
    else:
        # Calculate Fn+2 % 10 iteratively
        previous, current = 0, 1
        for _ in range(n - 1):
            previous, current = current, (previous + current) % 10
        fib_n_plus_2 = current

    # Result: (F_n+2 - 1) % 10
    # Modulo 10 ensures that if F_n+2 ends in 0, the sum last digit becomes 9
    return (fib_n_plus_2 - 1) % 10

if __name__ == '__main__':
    n = int(input())
    print(fibonacci_sum(n))
