n=int(input('Enter the number of elements in the array: '))
arr=[]
for i in range(n):
    element=int(input('Enter element {}: '.format(i+1)))
    arr.append(element)
def Single_Number(arr):
    t=0
    for i in arr:
        t^=i
    return t

print(Single_Number(arr))