def reverse(D, i, k):
    if k < 2: # base case
        return
    x2 = D.delete_at(i + k - 1) # swap items i and i + k - 1
    x1 = D.delete_at(i)
    D.insert_at(i, x2)
    D.insert_at(i + k - 1, x1)
    reverse(D, i + 1, k - 2) # recurse on remainder