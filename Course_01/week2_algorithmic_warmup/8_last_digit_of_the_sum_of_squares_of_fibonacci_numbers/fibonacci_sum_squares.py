def get_fibonacci_last_digit(n):
    """Calculates the last digit of the n-th Fibonacci number."""
    # The Pisano period for modulo 10 is 60
    n = n % 60
    if n <= 1:
        return n
    
    previous, current = 0, 1
    for _ in range(n - 1):
        previous, current = current, (previous + current) % 10
        
    return current

def fibonacci_sum_squares(n):
    """Calculates the last digit of (F0^2 + F1^2 + ... + Fn^2)."""
    # Identity: Sum of squares up to Fn = Fn * F(n+1)
    # We need the last digit of Fn and the last digit of F(n+1)
    last_digit_fn = get_fibonacci_last_digit(n)
    last_digit_fn_plus_1 = get_fibonacci_last_digit(n + 1)
    
    # The last digit of the product is (last_digit_a * last_digit_b) % 10
    return (last_digit_fn * last_digit_fn_plus_1) % 10



if __name__ == '__main__':
    n = int(input())
    print(fibonacci_sum_squares(n))
