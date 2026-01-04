# Uses python3
import sys

def get_fibonacci_last_digit(n):
    # The Pisano period for modulo 10 is 60
    n = n % 60
    if n <= 1:
        return n
    
    previous = 0
    current = 1
    
    for _ in range(n - 1):
        previous, current = current, (previous + current) % 10
        
    return current


def fibonacci_partial_sum_naive(m, n):
    # Sum(m, n) = F(n+2) - F(m+1)
    # We calculate the last digit of F(n+2) and F(m+1)
    f_n_plus_2 = get_fibonacci_last_digit(n + 2)
    f_m_plus_1 = get_fibonacci_last_digit(m + 1)
    
    # Add 10 to ensure the result isn't negative before modulo
    return (f_n_plus_2 - f_m_plus_1 + 10) % 10


if __name__ == '__main__':
    from_, to = map(int, input().split())
    print(fibonacci_partial_sum_naive(from_, to))
