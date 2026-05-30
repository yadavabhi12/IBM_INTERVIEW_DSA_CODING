l=[7,3,5,1,3,-11]
def selection_sort(l):
    n=len(l)
    for i in range(n):
        min=i
        for j in range(i+1,n):
            if l[j]<l[min] :
               min=j
        l[i],l[min]=l[min],l[i]

    return l
print(selection_sort(l))
