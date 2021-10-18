import math
w=float(input("PLEASE ENTER THE WEIGHT OF BLOCK A : "))
f1=float(input("PLEASE ENTER THE FRICTION BETWEEN BLOCK A AND SLOPE : "))
f2=float(input("PLEASE ENTER THE FRICTION BETWEEN BLOCK B AND SLOPE : "))
a=float(input("PLEASE ENTER THE ANGLE WHICH THE SLOPE MAKES : "))
cv=math.cos(a*0.0174533)
sv=math.sin(a*0.0174533)
na=w*cv
print("NORMAL ON THE BLOCK A : ",round(na,1))
t=(w*sv)-(na*f1)
print("TENSION IN THE STRING : ",round(t,1))
nb=t/f2
print("NORMAL ON THE BLOCK B : ",round(nb,1))
mb=nb/9.8
print("MASS OF THE BLOCK B : ",round(mb,1))

