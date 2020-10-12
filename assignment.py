#! python3

import math

def tempConversion(degrees, unit="C"):
    deg1=(degrees*1.8)+32
    if unit=="F":
        deg1=((degrees-32)*(5/9))
    deg1=round(deg1,1)
    return deg1


def factorPair(num, fact):
    li1=[]
    fact2=num/fact
    li1=[int(fact),int(fact2)]
    li1.sort()
    return li1







def toRadians(angle):
    import math
    rad=angle*(math.pi/180)
    return rad

def quadratic(a,b,c):
    li1=[]
    print(a)
    print(b)
    print(c)
    x1 = (-b + (math.sqrt((b**2) - (4 * a * c))) / (2*a))
    x2 = (-b - (math.sqrt((b**2) - (4 * a * c))) / (2*a))
    li1.append(x1)
    li1.append(x2)
    li1.sort()
    return li1


    
def solution(lis):
    x2=lis[1]
    return x2

def cosineLaw(a , b , angle , oppositeSide=True):
    import math
    c2=0
    c2=a**2 + b**2 -(2 * a * b * (math.cos(toRadians(angle))))
    c2=math.sqrt(c2)
    if oppositeSide==False:
        q1=1
        q2=-(2*a*math.cos(toRadians(angle)))
        q3=(a**2 - b**2)
        c1=quadratic(q1,q2,q3)
        c2=solution(c1)
    return c2