def compute_operations(n):
    # min_ops[i] will store the minimum number of operations to reach i from 1
    # We initialize a list of size n+1 with zeros
    min_ops = [0] * (n + 1)

    # 1. Fill the DP table (Bottom-Up approach)
    for i in range(2, n + 1):
        # Default strategy: Come from the previous number (i - 1) by adding 1
        min_ops[i] = min_ops[i - 1] + 1
        
        # Check if coming from (i / 2) via multiplication is faster
        if i % 2 == 0:
            min_ops[i] = min(min_ops[i], min_ops[i // 2] + 1)
            
        # Check if coming from (i / 3) via multiplication is faster
        if i % 3 == 0:
            min_ops[i] = min(min_ops[i], min_ops[i // 3] + 1)

    # 2. Backtrack to find the actual sequence of numbers
    sequence = []
    current_value = n
    while current_value >= 1:
        sequence.append(current_value)
        # Determine which operation was used to reach the current_value optimally
        if current_value % 3 == 0 and min_ops[current_value] == min_ops[current_value // 3] + 1:
            current_value //= 3
        elif current_value % 2 == 0 and min_ops[current_value] == min_ops[current_value // 2] + 1:
            current_value //= 2
        else:
            current_value -= 1
            
    # Since we backtracked from n to 1, we must reverse the list
    sequence.reverse()
    
    # Return both the count of operations (k) and the sequence list
    return len(sequence) - 1, sequence


if __name__ == '__main__':
    input_n = int(input())
    output_sequence = compute_operations(input_n)
    print(len(output_sequence) - 1)
    print(*output_sequence)
