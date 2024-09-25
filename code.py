num = input().split()

m = int(num[0])
n = int(num[1])

total_sum = 0
for i in range(1, m +1):
    
    mat_input = list(map(int,input().split()))
    
    if i > 1 and i < m:
        sum_of = mat_input[0] + mat_input[-1]
        total_sum += sum_of
    else:
        sum_of = sum(mat_input)
        total_sum += sum_of

print(total_sum)        
