# Algorithms and Data Structures Insights

This file includes the insights from algorithm and data structure code.



## Algorithmic Warm-up: Fibonacci and Number Theory

### 1. Fibonacci Number Problem
**Core Insight:** Naive recursion results in exponential time $O(2^n)$. By using **Iterative Dynamic Programming**, we build the solution from the ground up in $O(n)$ time. To optimize space to $O(1)$, we only track the two most recent values (`previous` and `current`) instead of an entire array.

```python
def get_fibonacci(n):
    if n <= 1:
        return n
    
    # previous = F(i-1), current = F(i)
    previous, current = 0, 1
    for _ in range(n - 1):
        # Update values iteratively to save memory
        previous, current = current, previous + current
        
    return current
```

### 2. Last Digit of Fibonacci Number Problem
**Problem:** Compute the last digit of the n-th Fibonacci number.
- **Input:** An integer `n`.
- **Output:** The last digit of $F_n$.

#### Core Insight
The last digit of any Fibonacci number $F_n$ is determined solely by the last digits of the two preceding numbers $F_{n-1}$ and $F_{n-2}$. By applying **Modular Arithmetic** ($mod \ 10$) at each addition step, we avoid handling astronomical numbers that would cause integer overflow or slow down the computation, keeping the space complexity at $O(1)$.



```python
def get_fibonacci_last_digit(n):
    if n <= 1:
        return n

    # Initialize previous and current Fibonacci last digits (F0 and F1)
    previous, current = 0, 1
    
    for _ in range(n - 1):
        # In modular arithmetic: (a + b) % m = ((a % m) + (b % m)) % m
        # We only keep the remainder to track the last digit
        previous, current = current, (previous + current) % 10
        
    return current
```
### 3. Greatest Common Divisor (GCD) Problem
**Problem:** Compute the greatest common divisor of two positive integers.
- **Input:** Two positive integers `a` and `b`.
- **Output:** The greatest common divisor of `a` and `b`.

#### Core Insight
The **Euclidean Algorithm** is the most efficient method for finding the GCD. It relies on the recursive property: $GCD(a, b) = GCD(b, a \pmod b)$. This approach reduces the problem size logarithmically, ensuring a highly efficient $O(\log(\min(a, b)))$ time complexity. This makes it extremely fast even for very large numbers, as the values of `a` and `b` decrease rapidly in each iteration.



```python
def gcd(a, b):
    # Iteratively replace (a, b) with (b, a % b) until b is 0
    while b:
        # Pythonic simultaneous assignment handles the swap and modulo operation
        # This prevents the need for a temporary 'temp' variable
        a, b = b, a % b
    return a
```
### 4. Least Common Multiple (LCM) Problem
**Problem:** Compute the least common multiple of two positive integers.
- **Input:** Two positive integers `a` and `b`.
- **Output:** The least common multiple of `a` and `b`.

#### Core Insight
Calculating the LCM directly by checking multiples is inefficient for large numbers. Instead, we use the fundamental mathematical relationship: $LCM(a, b) = \frac{|a \times b|}{GCD(a, b)}$. By leveraging the efficient Euclidean algorithm to find the GCD first, we can compute the LCM in $O(\log n)$ time. To prevent potential integer overflow in various programming environments, it is a best practice to perform the division by the GCD before the multiplication.



```python
def gcd(a, b):
    # Euclidean algorithm to find the GCD efficiently
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    # Base case: if either number is 0, the LCM is 0
    if a == 0 or b == 0:
        return 0
    
    # Using the identity: LCM(a, b) = (a * b) // GCD(a, b)
    # Division is done first to keep intermediate values smaller
    return (a * b) // gcd(a, b)
```
### 5. Huge Fibonacci Number Modulo m Problem
**Problem:** Compute the n-th Fibonacci number modulo $m$.
- **Input:** Integers $n$ (up to $10^{18}$) and $m$ (up to $10^5$).
- **Output:** $F_n \pmod m$.

#### Core Insight
The Fibonacci sequence modulo $m$ is periodic, a phenomenon known as the **Pisano Period**. This period always starts with the sequence `0, 1`. By discovering the length of this period ($P$), we can dramatically reduce a massive index $n$ to a manageable size using $n \pmod P$. This reduction allows us to compute results for $n$ as large as $10^{18}$ almost instantaneously, transforming what would be an impossible calculation into a fast iterative process.



```python
def get_pisano_period(m):
    # A Pisano period always starts with the sequence 0, 1
    previous, current = 0, 1
    # The maximum possible period length for m is m * m
    for i in range(0, m * m):
        previous, current = current, (previous + current) % m
        # The period resets when we find 0 followed by 1
        if previous == 0 and current == 1:
            return i + 1

def get_huge_fibonacci_modulo(n, m):
    # Use the Pisano Period to scale down the massive index n
    period = get_pisano_period(m)
    n = n % period
    
    if n <= 1:
        return n

    # Compute Fn % m for the reduced n using the iterative approach
    previous, current = 0, 1
    for _ in range(n - 1):
        previous, current = current, (previous + current) % m
        
    return current
```
### 6. Last Digit of the Sum of Fibonacci Numbers Problem
**Problem:** Compute the last digit of the sum $F_0 + F_1 + \dots + F_n$.
- **Input:** An integer `n`.
- **Output:** The last digit of the sum.

#### Core Insight
Calculating the sum directly for a large $n$ is computationally expensive. Instead, we apply the **Fibonacci Sum Identity**: $\sum_{i=0}^{n} F_i = F_{n+2} - 1$. Since we only need the last digit, we find $F_{n+2} \pmod{10}$. Knowing that the **Pisano Period** for $m=10$ is exactly 60, we simplify the index $(n+2)$ to $(n+2) \pmod{60}$. This allows us to compute the last digit of the sum in constant time $O(60)$ regardless of how large $n$ is.



```python
def get_fibonacci_sum_last_digit(n):
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
```
