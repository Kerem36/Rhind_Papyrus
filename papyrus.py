def GCD(a, b):
    for i in range(min(a, b), 0, -1):
        if a%i == 0 and b%i == 0:
            return i
    return 1


def main():
    a = int(input())
    b = int(input())
    n = 2
    results = []
    while a > 1:
        if 1/n < a/b:
            new_a = a*n - b
            new_b = n*b
            results.append("1/%d"%n)
            d = GCD(new_a, new_b)
            a = new_a//d
            b = new_b//d
            n = int(b/a) # runs much faster with this command 
            
        n += 1

    results.append("1/%d"%b)
    
    print(*results, sep="\n")


if __name__ == '__main__':
    main()
