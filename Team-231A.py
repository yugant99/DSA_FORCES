n = int(input())
count = 0 
for _ in range(n):
    friends = input().split()
    if friends.count('1') >=2:
        count += 1
print(count)