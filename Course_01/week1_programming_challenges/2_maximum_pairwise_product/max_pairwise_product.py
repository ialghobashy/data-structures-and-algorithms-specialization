def max_pairwise_product(numbers):
    n = len(numbers)
    index_1 = 0
    for i in range(1, n):
        if numbers[i] > numbers[index_1]:
            index_1 = i
            
    index_2 = n-1

    if index_1 == index_2:
        index_2 = 0

    for i in range(n):
        if i != index_1 and numbers[i] > numbers[index_2]: 
                index_2 = i

    return numbers[index_1] * numbers[index_2]


if __name__ == '__main__':
    _ = int(input())
    input_numbers = list(map(int, input().split()))
    print(max_pairwise_product(input_numbers))
