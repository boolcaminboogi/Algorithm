from Lab05 import*

#1-1,5
def ternarySearchTest():
    lab05 = Lab05()
    A = random.sample(range(1, 50), 30)
    A.sort()
    print(A)
    key = 19
    p = lab05.interpolationSearchRec(0, len(A) - 1, key, A)
    print("1-1. interpolationSearchRec: Index of", key, "is", p)
    p = lab05.interpolationSearchItr(A, key)
    print("1-1. interpolationSearchItr: Index of", key, "is", p)
    p = lab05.ternarySearchRec(0, len(A) - 1, key, A)
    print("1-5. ternarySearchRec: Index of", key, "is", p)
    p = lab05.ternarySearchItr(A, key)
    print("1-5. ternarySearchItr: Index of", key, "is", p)
    
    
#1-4    
def rankSelectionTest_1():
    lab05=Lab05()
    A = random.sample(range(1, 50), 30)
    print(A)
    medi=int(round((1+len(A))/2))
    largest= len(A)
    smallest=1
    print("element at rank {} is {} ".format(smallest,lab05.rankSelection(A, 0, len(A)-1, smallest)))
    print("element at rank {} is {} ".format(largest, lab05.rankSelection(A, 0, len(A) - 1, largest)))
    print("element at rank {} is {} ".format(medi, lab05.rankSelection(A, 0, len(A) - 1, medi)))
    A.sort()
    print(A)
    
#1-2,3    
def slTest():
    lab05=Lab05()
    A=random.sample(range(1,50),30)
    A.sort()
    print(A)
    #print("SL", lab05.findSL_large(A))
    #print("SL", lab05.findSL_small(A))
    print("SLPK_small", lab05.findSLPK_small(A))
    print("SLPK_large", lab05.findSLPK_large(A))

def minMaxTest():
    lab05 = Lab05()
    A = random.sample(range(1, 3000), 15)
    print(A)
    minmax = lab05.getMinMax1(A)
    print("Minimum element is", minmax.min)
    print("Maximum element is", minmax.max)
    
#1-4    
def rankSelectionTest():
    lab05=Lab05
    A=random.sample(range(1,50),30)
    print(A)
    medi=int(round((1+len(A))/2))
    largest=len(A)
    smallest=1
    print("element at rank {} is {}". format(smallest, lab05.rankSelection(A,0,len(A)-1,smallest)))
    print("element at rank {} is {}". format(largest, lab05.rankSelection(A,0,len(A)-1,largest)))
    print("element at rank {} is {}". format(medi, lab05.rankSelection(A,0,len(A)-1,medi)))
    A.sort()
    print(A)
    
    
#2-1
def POLTest():
    lab05 = Lab05()
    P = [(1, 1), (3, 5), (4, 6), (6, 6), (2, 3), (3, 5), (7, 3), (12, 3), (4, 14)]
    lab05.postOfficeLocation(P)

#2-2
def fakeCoinTest():
    fk = FakeCoin(20)
    print("Fake Coin with weight:", fk.fake_coin_DQ2())

#2-3
def bitflipstest():
    bf=BitFlips()
    res = bf.minBitFlips(3, 11193)
    print("No. of flips :",res)

def main():
    #ternarySearchTest()
    #slTest()
    #rankSelectionTest()
    
    #POLTest()
    #fakeCoinTest()
    bitflipstest()
    #minMaxTest() 


if __name__ == '__main__':
    main()