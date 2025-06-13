n = int(input())
for _ in range(n):
    h,m = map(int,input().split())
    print(abs(23-h)*60 + abs(60-m))