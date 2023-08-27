from collections import namedtuple  
import matplotlib.pyplot as plt  
import random
import math
import copy

class Point():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def __repr__(self):
        return "({},{})".format(self.x, self.y)
    
    def __eq__(self, other):    
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):    
        return not self == other

    def __gt__(self, other): 
        if self.x > other.x:
            return True
        elif self.x == other.x:
            return self.y > other.y
        return False

    def __lt__(self, other):
        return not self > other

    def __ge__(self, other):
        if self.x > other.x:
            return True
        elif self.x == other.x:
            return self.y >= other.y
        return False

    def __le__(self, other):
        if self.x < other.x:
            return True
        elif self.x == other.x:
            return self.y <= other.y
        return False
    def __hash__(self):
        return hash(self.x)
    
#3-Divide and Conquer Algorithm for Closest-Pair Problem
class ClosestPair:
    def getPoints(self, n):
        points=[]
        for _ in range(n):

            point=Point(random.randint(1, 200), random.randint(1, 200))
            if point not in points:
                points.append(point)
        return points
    
    
    def closest_pair_bf(self, P):
        n = len(P) 
        cp=[]             			
        mindist = float("inf")  			
        for i in range(n-1):
            for j in range(i+1, n):
                dist = self.distance(P[i], P[j])	
                if dist < mindist:
                    mindist = dist
                    cp=(P[i],P[j])
        return mindist,cp
    
    def distance(self,p1, p2):
        return math.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2) 

    def stripClosest(self, strip,  d):
        size=len(strip)
        min_val = d 
        for i in range(size):
            j = i + 1
            while j < size and (strip[j].y -strip[i].y) < min_val:
                min_val = self.distance(strip[i], strip[j])
                j += 1
        return min_val

    def closest_pair_dc(self,P, Q, n):
        if n <= 3: 
            mindist,cp=self.closest_pair_bf(P)
            return mindist 

        mid = n // 2
        midPoint = P[mid]

        dl = self.closest_pair_dc(P[:mid], Q, mid)
        dr = self.closest_pair_dc(P[mid:], Q, n - mid) 
        d = min(dl, dr)
        strip = [] 
        for i in range(n): 
            if abs(Q[i].x - midPoint.x) < d: 
                strip.append(Q[i])
        return min(d, self.stripClosest(strip, d))

    def closest_dc(self,P):
        n=len(P)
        Q = copy.deepcopy(P)
        P.sort(key = lambda point: point.x)
        Q.sort(key = lambda point: point.y)    
        return self.closest_pair_dc(P, Q, n)
    
    def display(self, P, cp):
        # all points
        x = [p.x for p in P]
        y = [p.y for p in P]
        plt.plot(x, y, marker='o', linestyle='None')

                # closest points
        cx = [p.x for p in cp]
        cy = [p.y for p in cp]
        plt.plot(cx, cy)
        
        plt.title('closest pair')
        plt.show()
