l=['aakash','abhi','ram','ankit']
t=sorted(l,key=lambda x:len(x),reverse=True)
print(t)
print(l)


class student:
    def __init__(s,name,ages,marks):
        s.name=name
        s.ages=ages
        s.marks=marks

l=[student('aakash',20,90),student('abhi',21,80),student('ram',19,95),student('ankit',22,85)]
top=sorted(l,key=lambda x:x.marks,reverse=True)
for i in top:
    print(i.name,i.ages,i.marks)