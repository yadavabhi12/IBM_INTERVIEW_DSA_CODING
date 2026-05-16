l=[7,3,5,1,3,-11]
def insertion_sort(l):
    n=len(l)
    for i in range(1, n):
        key = l[i]
        j = i - 1
        while j >= 0 and l[j] > key:
            l[j + 1] = l[j]
            j -= 1
        l[j + 1] = key
    return l
print(insertion_sort(l))
