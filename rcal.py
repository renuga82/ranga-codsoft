
a=int(input("enter the 1st number"))
b=int(input("enter the 2nd number"))
c=int(input("enter the 3rd number"))
ch=int(input("enter ur choice:"))
print("1.addition")
print("2.subtraction")
print("3.multiplication")
print("4.division")
print("5.modulous")
if ch==1:
    result=a+b+c
elif ch==2:
    result=a-b
elif ch==3:
    result=a*b*c
elif ch==4:
    result=a/b
    
elif ch==5:
    result=a%b
else:
    print("invalid choice")
print("result:",result)

