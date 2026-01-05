def change(money):
    if money == 0:
        return 0
    return money//10 + (money%10)//5 + money%5


if __name__ == '__main__':
    m = int(input())
    print(change(m))
