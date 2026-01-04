def fibonacci_last_digit(n):
    if n <= 1:
        return n

    # Initialize previous and current Fibonacci last digits (F0 and F1)
    previous, current = 0, 1
    
    for _ in range(n - 1):
        # In modular arithmetic: (a + b) % m = ((a % m) + (b % m)) % m
        # We only keep the remainder to track the last digit
        previous, current = current, (previous + current) % 10
        
    return current


if __name__ == '__main__':
    n = int(input())
    print(fibonacci_last_digit(n))
