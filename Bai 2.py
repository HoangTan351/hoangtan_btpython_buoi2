# bai 2
import math
print("nhap x: ",end="")
x=float(input())
print("nhap n: ",end="")
n=int(input())

s1=s2=s3=0.0

print("S1 = 1 + x + x^2 + x^3 + ... + x^n=",end="")
for i in range(n+1):
    s1+= pow(x,i)
    i+=1
print(s1)

print("S2 = 1 - x + x^2 - x^3 +...+(-1)^n*x^n=",end="")
for i in range(n+1):
    if i%2==0:
        s2+= pow(x,i)
    else:
        s2+= (-1)*pow(x,i)
    i+=1
print(s2)

print("S3 = 1 + x/(1!) + x^2/(2!) + x^3/(3!) +...+x^n/(n!)=",end="")
for i in range(n+1):
    s3+=(pow(x,i)/math.factorial(i))
    i+=1
print(s3)