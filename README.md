# Algorithms and Data Structures Insights

This file includes the insights from algorithm and data structure code.



## Algorithmic Warm-up: Fibonacci and Number Theory

### 1. Fibonacci Number Problem
 Naive recursion results in exponential time $O(2^n)$. By using **Iterative Dynamic Programming**, we build the solution from the ground up in $O(n)$ time. To optimize space to $O(1)$, we only track the two most recent values (`previous` and `current`) instead of an entire array.


### 2. Last Digit of Fibonacci Number Problem
The last digit of any Fibonacci number $F_n$ is determined solely by the last digits of the two preceding numbers $F_{n-1}$ and $F_{n-2}$. By applying **Modular Arithmetic** ($mod \ 10$) at each addition step, we avoid handling astronomical numbers that would cause integer overflow or slow down the computation, keeping the space complexity at $O(1)$.


### 3. Greatest Common Divisor (GCD) Problem
The **Euclidean Algorithm** is the most efficient method for finding the GCD. It relies on the recursive property: $GCD(a, b) = GCD(b, a \pmod b)$. This approach reduces the problem size logarithmically, ensuring a highly efficient $O(\log(\min(a, b)))$ time complexity. This makes it extremely fast even for very large numbers, as the values of `a` and `b` decrease rapidly in each iteration.


### 4. Least Common Multiple (LCM) Problem
Calculating the LCM directly by checking multiples is inefficient for large numbers. Instead, we use the fundamental mathematical relationship: $LCM(a, b) = \frac{|a \times b|}{GCD(a, b)}$. By leveraging the efficient Euclidean algorithm to find the GCD first, we can compute the LCM in $O(\log n)$ time. To prevent potential integer overflow in various programming environments, it is a best practice to perform the division by the GCD before the multiplication.


### 5. Huge Fibonacci Number 
The Fibonacci sequence modulo $m$ is periodic, a phenomenon known as the **Pisano Period**. This period always starts with the sequence `0, 1`. By discovering the length of this period ($P$), we can dramatically reduce a massive index $n$ to a manageable size using $n \pmod P$. This reduction allows us to compute results for $n$ as large as $10^{18}$ almost instantaneously, transforming what would be an impossible calculation into a fast iterative process.


### 6. Last Digit of the Sum of Fibonacci Numbers Problem
Calculating the sum directly for a large $n$ is computationally expensive. Instead, we apply the **Fibonacci Sum Identity**: $\sum_{i=0}^{n} F_i = F_{n+2} - 1$. Since we only need the last digit, we find $F_{n+2} \pmod{10}$. Knowing that the **Pisano Period** for $m=10$ is exactly 60, we simplify the index $(n+2)$ to $(n+2) \pmod{60}$. This allows us to compute the last digit of the sum in constant time $O(60)$ regardless of how large $n$ is.

### 7. Last Digit of the Partial Sum of Fibonacci Numbers Problem
To compute the last digit of the partial sum $F_m + F_{m+1} + \dots + F_n$, we apply the Fibonacci Partial Sum Identity: $\sum_{i=m}^{n} F_i = F_{n+2} - F_{m+1}$. Instead of iterating through the range, we focus on the last digits of only two Fibonacci numbers. By leveraging the Pisano Period for $m=10$ (which is 60), we simplify the indices to $(n+2) \pmod{60}$ and $(m+1) \pmod{60}$. To ensure the result is non-negative before the final modulo operation, we use the formula $(F_{n+2} - F_{m+1} + 10) \pmod{10}$. This approach reduces the computation to constant time $O(60)$, making it highly efficient for inputs up to $10^{18}$.

### 9. Last Digit of the Sum of Squares of Fibonacci Numbers Problem
To find the last digit of the sum of squares $F_0^2 + F_1^2 + \dots + F_n^2$, we use the Fibonacci Square Sum Identity: $\sum_{i=0}^{n} F_i^2 = F_n \times F_{n+1}$. This identity can be visualized geometrically as the area of a rectangle composed of squares with sides equal to Fibonacci numbers. To handle large $n$, we calculate the last digits of $F_n$ and $F_{n+1}$ separately by reducing the index $n$ using the Pisano Period for $m=10$ (which is 60). The final result is simply $(F_{n \pmod{60}} \times F_{(n+1) \pmod{60}}) \pmod{10}$. This reduces the calculation to constant time $O(60)$, providing an immediate result even for $n$ up to $10^{18}$.

### Money Change
The goal is to calculate the minimum number of coins needed to change a specific value into denominations of 1, 5, and 10. It is a fundamental optimization problem that tests the ability to reach a target sum using the fewest possible moves by prioritizing the highest-value units available.

Core Idea: The Division and Modulo Pattern This problem is solved using a Greedy strategy because the coin system (1, 5, 10) is canonical, ensuring that picking the largest coin first is always optimal. To implement this efficiently, we use the Division and Modulo Pattern: integer division (//) instantly determines the maximum number of the largest coins that fit, while the modulo operator (%) captures the remaining balance to be processed by the next denomination. This replaces iterative loops with direct arithmetic, making the solution