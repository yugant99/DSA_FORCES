n,k = map(int,input().split())
score = list(map(int,input().split()))

count = 0 
if k > n or k <= 0:
    print(0)
else:
    for i in range(n):
        if score[i] >= score[k-1] and score[i] > 0:
            count += 1
    print(count)

