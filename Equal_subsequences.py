t = int(input())
for _ in range(t):
    n,k = list(map(int,input().split()))
    bits = '1' * k + '0' * (n-k)
    print(bits)
