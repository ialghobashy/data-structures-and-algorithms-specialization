def fibonacci_number(n):
    if n <= 1:
        return n
    
    # previous = F(i-1), current = F(i)
    previous, current = 0, 1
    for _ in range(n - 1):
        # Update values iteratively to save memory
        previous, current = current, previous + current
        
    return current


if __name__ == '__main__':
    input_n = int(input())
    print(fibonacci_number(input_n))

