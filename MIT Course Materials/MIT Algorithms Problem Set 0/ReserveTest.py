def reverse(D, i, k):
    if k < 2: # base case
        return
    x2 = D.pop(i + k - 1) # swap items i and i + k - 1
    x1 = D.pop(i)
    D.insert(i, x2)
    D.insert(i + k - 1, x1)
    reverse(D, i + 1, k - 2) # recurse on remainder
A = [x for x in range(1,11)]
reverse(A,0,10)
print(A)

# need to define what delete at and insert at is