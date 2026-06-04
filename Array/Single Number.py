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
# arr=[2,3,3,2,4,4,5]    output  5    but ager [1,3,3,3,2,2]   output   3^3  =0,2^2 = 0   ,  3^1=2
print(Single_Number(arr))





# if list me repeat elements frequency two element ki odd frq hai to ans wrong ho sakta hai  but agar ek element ki odd frequency hai to ans sahi hoga







from collections import Counter

nums = [1, 3, 3, 3, 2, 2]

freq = Counter(nums)

for num, count in freq.items():
    if count == 1:
        print(num)






# output  5    but ager [1,3,3,3,2,2]   output   3^3  =0,2^2 = 0   ,  3^1=2





n = int(input("Enter the number of elements in the array: "))
arr = []

for i in range(n):
    arr.append(int(input(f"Enter element {i+1}: ")))

freq = {}

for num in arr:
    freq[num] = freq.get(num, 0) + 1      #frq count kar rahai hai element ki

for num, count in freq.items():
    if count == 1:
        print("Single Number:", num)
        break
