# bai 3
n=int(input("Nhap n: "))
Tong=0.0

while n>=1000:
    print("Nhap sai, moi nhap lai")
    n=int(input("Nhap n: "))

for i in range(0,n+1):
    Tong = Tong + i

print(Tong)