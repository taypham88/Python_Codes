A = (7, 8, 5, 7, 7, 3, 2, 8)
n = len(A)
current = 1 
length = 1 
count = 1
for i in range(1, n):
    print(A[i - 1])
    print(A[i])
    if A[i - 1] < A[i]:
        current = current + 1
    else:
        current = 1
    if current == length:
        count = count + 1
    elif current > length:
        length = current
        count = 1
print(count)
