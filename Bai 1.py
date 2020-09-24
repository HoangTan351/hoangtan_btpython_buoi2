# bai 1 bt vn
print("Nhap a: ",end="")
a=int(input())
print("Nhap b: ",end="")
b=int(input())
print("Nhap c: ",end="")
c=int(input())

import math
if(a!=0):
    delta=pow(b,2)-4*a*c
    print("Ket Qua Delta= ",end="")
    print(int(delta))
    if(delta==0):
        kq1=-b/2*a
    elif delta > 0:
        kq1=(-b + math.sqrt(delta))/2*a
        kq2=(-b - math.sqrt(delta))/2*a
    else: 
        kq1="phuong trinh vo nghiem"

    if kq1 == "phuong trinh vo nghiem":
        print(kq1)
    else: 
        print(kq1,kq2)
else:
    kq1= -c/b
    print(kq1)