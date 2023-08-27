from Lab03 import*
  
#lAB03_2
def testIntersection():
    lab03=Lab03()
    A=[1,3,5,7,9,11,13,15,17]
    B=[2,4,6,8,9,10,12,14,15,16]
    C=lab03.intersectionSet(A,B)
    print('Intersection Set= ', C)
     
def testPowerSet():
    lab03=Lab03()
    S1=[1,2,3]
    L1=lab03.powerSet(S1)
    print("Power Set = ", L1)
    
    S2=['A', 'B']
    L2=lab03.powerSet(S2)
    print("Power Set = ", L2)
    
def testBC():
    lab03=Lab03()
    print(lab03.binomialCoeffRec(15,5))
    print(lab03.binomialCoeffDP(15,5))
    

def testBC_1():
    lab03=Lab03()
    #print(lab03.binomialCoeffRec(5,5))
    B= lab03.binomialCoeffDP(8,3)
    for r in B:
        print(r)
        
def testLSZM():
    lab03=Lab03()
    matrix=[
        [9, 7, 16, 5],
        [1, -6, -7, -3],
        [1, 8, 7, -9],
        [7, -2, 0, 12]
        ]
    for r in matrix:
        print(r)
    Z=lab03.maxZeroSumSubmatrix(matrix)
    for r in Z:
        print(r)
        
def testSM():
    lab03=Lab03()
    txt = "AABAAVAADAABAAABAA"
    pat = "AABA"
    lab03.SM(txt, pat)

def testClosestPair():
    lab03=Lab03()
    pList=[(2,3), (12,30), (40,50), (5,1), (12, 10), (4,4), (3,3)]
    cp=lab03.closest_pair(pList)
    print('closest pair[{},{}] '.format(cp[0], cp[1]))
    print("Distance between closest pair = {: .2f} ".format(lab03.distance(cp[0])))



#lab03_1
def testSumSubArray():
    lab03=Lab03()
    ssa=lab03
    a=[3, -15, -4, 25, -3, 6, 5, 4, -2, 8]
    print("#1",ssa.maxSum4(a))
    print("#2",ssa.maxSum3(a, 0, len(a)-1))
    print("#3",ssa.maxSum2(a))
    print("#4",ssa.maxSum1(a))
    
def main():
    #testPowerSet()
    #testIntersection()
    #testBC()
    #testBC_1()
    #testLSZM()
    #testSM()
    #testClosestPair()
    testSumSubArray()
    
if __name__=='__main__':
    main()