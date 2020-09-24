# Bai 4
print("nhap canh a: ",end="")
a = int(input())
print("nhap canh b: ",end="")
b = int(input())
print("nhap canh c: ",end="")
c = int(input())


if (a<b+c or b<a+c or c<a+b):
   if(a*a==b*b+c*c or b*b==a*a+c*c or c*c==a*a+b*b):
        print("Đây Là Tam Giác Vuông",end="")
   else:
        print("Không phải tam giác vuông")
else:
     print("Đây Không Phải Là Tam Giác",end="")