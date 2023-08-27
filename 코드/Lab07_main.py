from Lab07 import*
import unittest

#1
def testPCP():
    pcp = PCP()
    A = pcp.numberOfPathsRec(3,3)
    B = pcp.numberOfPathsDP(3,3)
    C = pcp.numberOfPathsComb(3,3)
    print("1_1. Number of Path Rec : ",A)
    print("1_2. Number of Path Dinamic Programing :\n ",B)
    print("1_3. Number of Path Comb : ",C)

#2
def testCoinsCollection():
    cc = CoinsCollection()
    A=[[0,1,1,0,1,0],
       [1,1,12,6,1,1],
       [1,12,0,41,1,1],
       [0,1,1,1,1,0]]
    print("2_1. ccDP")
    F=cc.ccDP(A)
    print()
    print("2_2. Final F matrix")
    for r in F:
        print(r)
    cc.paths(F)
    
#3
def testMCM():
    mcm = MCM()

    # Test getMatricesDim()
    dims = mcm.getMatricesDim(5)

    # Test matrixChainMultiplicationRec()
    dims = [1, 2, 3, 4, 3]
    cost = mcm.matrixChainMultiplicationRec(dims, 0, len(dims) - 1)
    print("MCM_REC : ",cost)

    # Test matrixChainMultiplicationDP()
    dims = [1, 2, 3, 4, 3]
    M, P = mcm.matrixChainMultiplicationDP(dims)
    print("MCM_DP : ", M,P)

    # Test printOrder()
    dims = [1, 2, 3, 4, 3]
    M, P = mcm.matrixChainMultiplicationDP(dims)
    print("=> Optimal multiplication order:")
    mcm.printOrder(P, 0, len(dims) - 2)
    

def testOBST():
    obst = OBST()

    # Test findMinCostRec()
    freq = [34, 8, 50]
    cost = obst.findMinCostRec(freq, 0, len(freq) - 1, 1)
    #assert cost == 142

    freq = [10, 12, 16, 21]
    cost = obst.findMinCostRec(freq, 0, len(freq) - 1, 1)
    #assert cost == 68

    # Test findMinCostDP()
    nodes = [Node(10, 34), Node(12, 8), Node(16, 50)]
    A, R = obst.findMinCostDP(nodes)
    #assert A[0][2] == 142

    nodes = [Node(10, 10), Node(12, 12), Node(16, 16), Node(21, 21)]
    A, R = obst.findMinCostDP(nodes)
    #assert A[0][3] == 68

    # Test print_BST()
    key = [10, 12, 16, 21]
    root = [[1, 1, 2, 2], [0, 2, 2, 3], [-1, 0, 3, 3], [-1, -1, 0, 3]]
    obst.print_BST(root, key, 0, len(root) - 1, -1, True)
    
 

def main():
    #testPCP()
    #testCoinsCollection()
    testMCM()
    #testOBST()


if __name__ == '__main__':
    main()

