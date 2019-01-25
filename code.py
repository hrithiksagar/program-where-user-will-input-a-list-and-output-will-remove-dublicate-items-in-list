l=[]
s=int(input("please enter size of list")) 
for i in range(s):
    x=int(input("enter list items"))  
    l.append(x)
print("items you have entered",l)
q=set(l)
q= list(q)
print(q)