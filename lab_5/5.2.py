def subset(set1, set2):
    if set1 == set2:
        return False
    else:
        return set1.issubset(set2)

print(subset({1, 2, 3},{1, 4, 5}))
print(subset({1, 2, 3, 4, 5, 6, 7},{10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0}))
print(subset({1, 10, 223, 413, 2},{1, 10, 223, 413, 2}))