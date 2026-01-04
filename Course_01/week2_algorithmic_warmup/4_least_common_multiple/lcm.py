def lcm(a, b):
    def gcd(a, b):
        if a%b == 0:
            return b
        return gcd(b, a%b)
    if a%b==0:
        return a
    return int(a * b / gcd(a,b))

if __name__ == '__main__':
    a, b = map(int, input().split())
    print(lcm(a, b))

