import numpy as np
import sympy as syp
import math

def f(a,b,c,d,e=1):
    for i in range(e):
        a, b, c, d = a+b, b+c, c+d, d+a
    return a,b,c,d

def f1(a, b):
    for i in range(len(str(a*b))):
        a += math.cos(b)
        b += math.cos(a)

def f2(a,b,c):
    a = str(a)
    for i in range(c):
        a+=a+' '+str(i)
        for j in range(b):
            a += (str(i+j))*j
        if b > 1:
            b -= 1
        else:
            break
    
    return a

def main():
    print(f2("",0,0))

if __name__ == "__main__":
    main()