from itertools import permutations


def largest_number_naive(numbers):
    numbers = list(map(str, numbers))
    longest_int = max([len(number) for number in numbers])
    numbers_updated = sorted([[number * longest_int, number] for number in numbers], 
                             reverse= True)
    
    return int("".join([number[1] for number in  numbers_updated]))


if __name__ == '__main__':
    _ = int(input())
    input_numbers = input().split()
    print(largest_number_naive(input_numbers))
