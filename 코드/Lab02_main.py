from Lab02 import *

#def testSS():
#    lab2 = lab02()
#    S = [10,34, 22, 25, 90, 10, 63, 67]
#    x = 90
#    loc=lab2.ssearch(S, x)
#    if loc == -1:
#        print("Element fount at", loc)
#    else:
#        print("Element not fount")
        
def testlab02():
    lab2=lab02()
    A=[32, 14, 5, 17, 23, 9, 11, 14, 26, 29]
    B=[13, 6, 8, 7, 12, 25]
    #C=[[1,2,3,4], [5,6,7,8]]
    print("2-1. A :", A, lab2.unique_elements(A))
    print("2-1. B :", B, lab2.unique_elements(B))
    #print("2-2. 시간 효율적인 알고리즘 찾기 : ", C, lab2.GE(C))
    print("2-3. n^2 : ", lab2.power2(4), "/ 2^n 재귀적 : ", lab2.power2b(4))
    print("2-4. 계단 오르는 방법의 수 : ", lab2.ways(4))
    print("2-5. common division(interative) : ", lab2.gcd_inter(60, 6))
    print("2-6. common division(recursive) : ", lab2.gcd_rec(60, 6))
    
    
    
def main():
    testlab02()

if __name__=='__main__':
    main()