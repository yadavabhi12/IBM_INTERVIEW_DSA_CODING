s=input("Enter A String")
print(s[::-1])   # reverse string method 1
print(s[::])


# method 2
def reverse_string(s):
    r="" 
    for c in s:
        r=c+r
    return r
print("method 2 used extra space and time complexity is O(n)")
print(reverse_string(s))