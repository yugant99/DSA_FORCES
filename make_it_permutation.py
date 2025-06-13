def solve():
    n = int(input())
    operations  = []
    for i in range(2,n+1):
        k = i-1
        if k > 0 and k<n:
            operations.append(f"{i} 1 {k}")
            if n-k+1 < n :
                operations.append(f"{i} {n-k+1} {n}")

    print(len(operations))
    for op in operations:
        print(op)


        

