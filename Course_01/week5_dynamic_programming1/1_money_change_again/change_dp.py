def change(money):
    min_number = [0, 1, 2, 1, 1]
    for i in range(5, money+1):
        min_number.append(1 + min(min_number[i-1], min_number[i-3], min_number[i-4]))

    return min_number[money]


if __name__ == '__main__':
    m = int(input())
    print(change(m))
