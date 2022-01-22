import time
import random as ra
def seperateNumbers(string):
    a = []
    b = ''
    for i in range(len(string)):
        try:
            int(string[i])
            b += string[i]
            if len(string)-1 == i:
                a.append(int(b))
                b = ''
        except ValueError:
            if b != '':
                a.append(int(b))
                b = ''
    return tuple(a)

class Quaternion:
    def __init__(self,string):
        if type(string) == str:
            self.r, self.i, self.j, self.k = seperateNumbers(string)
        else:
            self.r = eval(str(string[0]))
            self.i = eval(str(string[1]))
            self.j = eval(str(string[2]))
            self.k = eval(str(string[3]))

    
    def __add__(self,other):
        return Quaternion([self.r+other.r,self.i+other.i,self.j+other.j,self.k+other.k])
    
    def __sub__(self,other):
        return Quaternion([self.r-other.r,self.i-other.i,self.j-other.j,self.k-other.k])
    
    def __mul__(self,other):
        return Quaternion([self.r*other.r - self.i*other.i - self.j*other.j-self.k*other.k,  self.r*other.i+self.i*other.r+self.j*other.k-self.k*other.j,  self.r*other.j+self.j*other.r+self.k*other.i-self.i*other.k, self.r*other.k+self.k*other.r+self.i*other.j-self.j*other.i])
    
    def __str__(self):
        return str(self.r)+' + '+str(self.i)+'i + '+str(self.j)+'j + '+str(self.k)+'k'

def randomQuaternionInt(r0,r1,i0,i1,j0,j1,k0,k1):
    return Quaternion([ra.randint(r0,r1),ra.randint(i0,i1),ra.randint(j0,j1),ra.randint(k0,k1)])

if __name__ == "__main__":
    a = Quaternion(input("Type a Quaternion : "))
    b = Quaternion(input("Type another Quaternion : "))
    c = a*b
    print("(",a,") * (",b,") = (",c,')')
