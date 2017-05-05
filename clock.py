# A script to check when the clock would be in a position with its hands apart by a ratio of 1:2:3.
# Yes, I know it's stupid but, Fuck You Sir.

# How are you going to implement a clock with code
# We can have three variables that keep track of the time
# Each variable will record only the info that is relavant to itself

import math

n = 60 * 60 * 12

def sort_sec(s,m,h):
    a = s
    b = m
    c = h
    if a > b:
        s = a
        b = a
        a = s
    if a > c:
        s = a
        c = a
        a = s
    if b > c:
        s = b
        c = b
        b = s

    return a,b,c



def check_ratio(s,m,h):
    a,b,c = sort_sec(s,m,h)
    print("%d %d %d" %(a,b,c))
    d = b - a
    e = c - b
    f = 360 - c + a
    print("%d %d %d" %(d,e,f))
    if ( d > 55 and d < 65 ):
        if ( e < 125 and e > 115):
            return 1
        if ( f < 125 and f > 115):
            return 1
    if ( e > 55 and e < 65):
        if ( d < 125 and d > 115):
            return 1
        if (f < 125 and f > 115):
            return 1
    if (f > 55 and f < 65):
        if (e < 125 and e > 115):
            return 1
        if ( d < 125 and d > 115):
            return 1
    return 0
    

for i in range(n):
    s = float(i/60/60/n*360)
    m = float(i/60/n*360)
    h = float(i/n*360)
    print("%f %f %f" %(s,m,h))
    if ( i%1000 == 0):
        print("thousand mark")
    if(check_ratio(s,m,h)):
        print("The ratio has made it's appearence.")


