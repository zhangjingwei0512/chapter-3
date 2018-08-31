diming=['New York','Vancouver','Stockholm','Buenos Aires','Perth']
import numpy
a=numpy.pi/180
weidu=[-40.7166*a,-49.23*a,-59.33*a,34.33*a,31.8667*a]
jingdu=[-74*a,-123.1*a,18.05*a,-58.5*a,115.8667*a]
import math
def haversin(x):
    return (1-math.cos(x))/2
for i in range(0,5):
    m=haversin(weidu[i]-(-22.2)*a)+math.cos(weidu[i])*math.cos((-22.2)*a)*haversin((jingdu[i])-114.1*a)
    n=1-2*m
    d=math.acos(n)*6371
    print('the distance between HONGKONG and %s is:'%(diming[i]),d,'km')