calculations = int(input())
count = 0 

for _ in range(calculations):
    calculation = input()
    if '++' in calculation:
        count +=1 
    else:
        count -=1 
print(count)