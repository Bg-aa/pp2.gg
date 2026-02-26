import math

R = float(input())
x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())

def length(p1, p2):
    return math.hypot(p1[0]-p2[0], p1[1]-p2[1])

A = (x1, y1)
B = (x2, y2)

dx, dy = B[0]-A[0], B[1]-A[1]

dist = abs(dx*A[1] - dy*A[0]) / math.hypot(dx, dy)

if dist >= R:

    print(f"{length(A,B):.10f}")
else:

    def tangent_length(P):
        return math.sqrt(P[0]**2 + P[1]**2 - R**2)
    
    tA = tangent_length(A)
    tB = tangent_length(B)

    angleA = math.atan2(A[1], A[0])
    angleB = math.atan2(B[1], B[0])

    alphaA = math.asin(R / math.hypot(A[0], A[1]))
    alphaB = math.asin(R / math.hypot(B[0], B[1]))
    
    theta = abs((angleB - alphaB) - (angleA + alphaA))
    theta = (theta + 2*math.pi) % (2*math.pi)  
    
    L = tA + tB + R*theta
    print(f"{L:.10f}")