n= int(input("Enter the number of elements in the array: "))
arr=[]
for i in range(n):
    arr.append(int(input('')))
target = int(input("Enter the target sum: "))






# method  1
def two_sum(arr,target):
    for i in range(n):
        for j in range(i+1):
          if arr[i]+arr[j]==target:
             return [i,j]; 





# method 2

def two_sum_dict(arr,target):
   dict={}
   for i in range(n):
      t=target-arr[i]
      if(t in dict):
         return [dict[t],i]
      dict[arr[i]]=i
   return None

print(two_sum(arr,target))
print(two_sum_dict(arr,target))