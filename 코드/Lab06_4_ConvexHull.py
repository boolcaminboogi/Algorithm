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
    
#4-Divide and Conquer Algorithm for Convex-Hull
class ConvexHull:  
    _points = []
    _hull_points = []
    
    def getPoints(self, n):
        points=[]
        for _ in range(n):
            point=Point(random.randint(-200, 200), random.randint(-200, 200))
            points.append(point)
        return points

    def __init__(self):
        pass

    def add(self, point):
        self._points.append(point)
        
    def _det(self,a, b, c): 
        det = (a.x * b.y + b.x * c.y + c.x * a.y) - (a.y * b.x + b.y * c.x + c.y * a.x)
        return det   

    def convex_hull_bf(self, points):
        points.sort(key = lambda point: point.x)
        n = len(points)
        convex_set = set()
        for i in range(n - 1):
            for j in range(i + 1, n):
                points_left_of_ij = points_right_of_ij = False
                ij_part_of_convex_hull = True
                for k in range(n):
                    if k != i and k != j:
                        det_k = self._det(points[i], points[j], points[k])

                        if det_k > 0:
                            points_left_of_ij = True
                        elif det_k < 0:
                            points_right_of_ij = True
                        else:
                            if points[k] < points[i] or points[k] > points[j]:
                                ij_part_of_convex_hull = False
                            break

                    if points_left_of_ij and points_right_of_ij:
                        ij_part_of_convex_hull = False
                        break

                if ij_part_of_convex_hull:
                    convex_set.update([points[i], points[j]])

        return list(convex_set)
    
    def convex_hull_dc(self,points):
        points.sort(key = lambda point: point.x)
        n = len(points)
        left_most_point = points[0]
        right_most_point = points[n - 1]
        
        convex_set = {left_most_point, right_most_point}
        upper_hull = []
        lower_hull = []
        for i in range(1, n - 1):
            det = self._det(left_most_point, right_most_point, points[i])

            if det > 0:
                upper_hull.append(points[i])
            elif det < 0:
                lower_hull.append(points[i])
        self._construct_hull(upper_hull, left_most_point, right_most_point, convex_set)
        self._construct_hull(lower_hull, right_most_point, left_most_point, convex_set)
        return convex_set

    def _construct_hull(self, points, left, right, convex_set):
        if points:
            extreme_point = None
            extreme_point_distance = float("-inf")
            candidate_points = []

            for p in points:
                det = self._det(left, right, p)

                if det > 0:
                    candidate_points.append(p)

                    if det > extreme_point_distance:
                        extreme_point_distance = det
                        extreme_point = p

        if extreme_point:
            self._construct_hull(candidate_points, left, extreme_point, convex_set)
            convex_set.add(extreme_point)
            self._construct_hull(candidate_points, extreme_point, right, convex_set)
        

    def display(self, points, S):
        
        fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(10, 3))
        x = [p.x for p in points]
        y = [p.y for p in points]
        ax1.plot(x, y, '.', color='k')
        ax1.set_title('Given points')
        
        hx = [p.x for p in S]
        hy = [p.y for p in S]
        ax2.plot(hx, hy, 'o', color='r')
        ax2.set_title('Points in Convex hull')
        plt.show()


