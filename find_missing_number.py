# elements is sorted and not repeated
a=[1,2,3,5,6,7]

def find_missing_number_sorted(arr):
    n = len(arr) + 1
    total = n * (n + 1) // 2
    return total - sum(arr)







# method 2   element is unsorted and not repeated
def find_missing_number_unsorted(arr):
    n = len(arr) + 1
    total = n * (n + 1) // 2
    return total - sum(arr)








def find_missing_number_unsorted_repeat(arr):
   s=set(arr)
#    print(len(s))
   n= len(s)+1      #   o(n)  max(s)+1
   for i in range(1,n+1):
       if(i in s):
           continue
       else:
           return i

print(find_missing_number_unsorted_repeat([1,3,5,6,3,2,3,8,7,3,2]))




def find_missing_number_unsorted_repeat_with_arr(arr):
   n = max(arr) + 1
   l=[0]*n
   for i in arr:
       l[i-1]=1


   return l.index(0)+1