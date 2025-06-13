def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    def count_bits(x):
        return bin(x).count('1')
    if k == 0 :
        return sum(count_bits(x) for x in a)
    max_beauty = 0
    for i in range(n):
        temp_array = a[:]
        temp_array[i] += k 
        beauty = sum(count_bits(x) for x in temp_array)
        max_beauty = max(max_beauty,beauty)
    return max_beauty

t = int(input())
for _ in range(t):
    solve()