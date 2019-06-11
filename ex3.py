c=list(raw_input())
d=[]
a=len(c)
for  i  in range(0,a):
    d.append(c[a-1-i])
if(d==c):
    print("yes")
else:
    print("no")
