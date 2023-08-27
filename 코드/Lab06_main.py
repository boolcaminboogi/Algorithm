#from Lab06_1_Karatsuba import*
#from Lab06_2_Strassen import*
#from Lab06_3_ClosestPair import*
#from Lab06_4_ConvexHull import*
from Lab06_5_Tromino import*


#1
def testKaratsuba():
    lab06_1 = Karatsuba()
    x=lab06_2.karatsubaMultiplication(2925, 6872)
    print("1-1. karatsubaMultiplication : ", x)
    y=lab06_2.gradeSchoolMultiplication(2925, 6872)
    print("1-2. gradeSchoolMultiplication : ", y)
    
#2
def testStrassen():
    lab06_2 = Strassen()
    A=np.array([[2,3],[4,1]])
    B=np.array([[5,7],[6,8]])
    C=np.zeros((2,2))
    x=lab06_2.strassen(A, B)
    print("2-1. strassen : ", x)
    y=lab06_2.multiply(A, B, C)
    print("2-2. multiply : ", y)
    
#3
def testClosestPair():
    lab06_3 = ClosestPair()
    p1=Point(1,1)
    p2=Point(4,5)
    a=lab06_3.distance(p1,p2)
    print("3_1.Distance : ",a)
    
    strip = [Point(1, 1), Point(2, 3), Point(4, 6), Point(6, 7), Point(9, 12)]
    dist = 3
    b=lab06_3.stripClosest(strip,dist)
    print("3_2.StripClosest : ",b)
    
    P = [Point(1, 1), Point(2, 3), Point(4, 6), Point(6, 7), Point(9, 12)]
    c=lab06_3.closest_pair_dc(P,P,len(P))
    print("3_3.Closest_Pair_DC : ", c)
    
#4
def testConvexHull():
    lab06_4 = ConvexHull()
    n=20
    points = ConvexHull().getPoints(n)
    ch = ConvexHull()
    dc_hull = ch.convex_hull_dc(points)
    ch.display(points, dc_hull)
    
#5
def testTromino():
    lab06_5 = Tromino()
    tp = Tromino(n=3, tileX=2, tileY=2)
    tp.printMap()
        


def main():
    #testKaratsuba()
    #testStrassen()
    #testClosestPair()
    #testConvexHull()
    testTromino() 


if __name__ == '__main__':
    main()
