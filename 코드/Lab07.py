import sys
import copy
import random

#1. Path counting Problem
class PCP:
    def binomialCoeffDP(self,n, k):
        B = [[0 for x in range(k + 1)] for x in range(n + 1)]
        for i in range(n + 1):
            for j in range(min(i, k) + 1):
                if j == 0 or j == i:
                    B[i][j] = 1
                else:
                    B[i][j] = B[i - 1][j - 1] + B[i - 1][j]
                    print("(i,j) ({},{}) -> B[i][j]={} = B[i - 1][j - 1]={} + B[i - 1][j]={}".format(i, j, B[i][j], B[i - 1][j - 1], B[i - 1][j]))
        return B[n][k]

    def binomialCoeffRec(self, n, k):
        if k > n:
            return 0
        if k == 0 or k == n:
            return 1
        return self.binomialCoeffRec(n - 1, k - 1) + self.binomialCoeffRec(n - 1, k)

    def numberOfPathsRec(self, m, n): #divide/decrease and conquer
        if (m == 1 or n == 1):
            return 1
        return self.numberOfPathsRec(m - 1, n) + self.numberOfPathsRec(m, n - 1)

    def numberOfPathsDP(self, n, m): #dinamic programming based
        #print("numberOfPaths by DP")
        B = [[0 for i in range(n)] for j in range(m)]
        for j in range(n):
            B[0][j] = 1
        for i in range(m):
            B[i][0] = 1
        for i in range(1, m):
            for j in range(1, n):
                B[i][j] = B[i - 1][j] + B[i][j - 1]
        return B

    def numberOfPathsComb(self,m, n):
        #print("numberOfPaths by using combinatorics")
        paths = 1
        for i in range(n, (m + n - 1)):
            paths *= i
            paths //= (i - n + 1)
            print("i={}, paths = {}".format(i, paths))
        return paths


#2. Coin-collecting problem and (print path) 13pg
class CoinsCollection:
    def ccDP(self, A):
        F = copy.deepcopy(A)
        for j in A:
            print(j)
        for r in range(1, len(A)):
            F[r][0]=F[r-1][0]+ A[r][0]
        for c in range(1, len(A[0])):
            F[0][c] = F[0][c - 1] + A[0][c]
        for r in range(1, len(A)):
            for c in range(1, len(A[0])):
                F[r][c] =  A[r][c]+ max(F[r - 1][c], F[r][c - 1])
        for r in F:
            print(r)
        return F

    def paths(self, F):
        m, n = len(F), len(F[0])
        print(m,n)
        B = [['-' for i in range(n)] for j in range(m)]
        for r in B:
            print(r)
        row = m - 1
        column = n - 1
        print(row, column)
        B[row][column] = '*'

        while row >= 1:
            if column != 0 and (F[row][column - 1] > F[row - 1][column]):  # leftward
                B[row][column - 1] = '*'
                column = column - 1
            else:
                B[row - 1][column] = '*'  # upward
                row = row - 1
        # the remaining cells path of the first row
        column = column - 1
        while column >= 0:
            B[0][column] = '*'
            column = column - 1
        for r in B:
            print(r)



#3. Chained Matrix Multiplication and (Print Optimal Order)
class MCM:
    def getMatricesDim(self, n):
        dims=[]
        for i in range(n+1):
            dims.append(random.randint(1, 9))
        for i in range(n):
            print("M{}({} x {}) ".format(i+1,dims[i], dims[i+1] ))
        return dims
    
    def matrixChainMultiplicationRec(self, dims, i, j):
        if j <= i + 1:
            return 0
        minmul = sys.maxsize
        for k in range(i + 1, j):
            cost = self.matrixChainMultiplicationRec(dims, i, k)
            cost += self.matrixChainMultiplicationRec(dims, k, j)
            cost += dims[i] * dims[k] * dims[j]
            if cost < minmul:
                minmul = cost
        return minmul
    
    def matrixChainMultiplicationDP(self,dims):
        n = len(dims) - 1
        M = [[0 for x in range(0, n)] for y in range(0, n)]
        P = [[0 for x in range(0, n)] for y in range(0, n)]

        for i in range(0,n):
            P[i][i] = 0
        for l in range(2, n+1):
            for i in range(0, n - l + 1):
                j = i + l - 1 
                if i < j: 
                    cost = [M[i][k] + M[k+1][j] + dims[i] * dims[k+1] * dims[j+1] for k in range(i, j)]
                    (P[i][j], M[i][j]) = min(enumerate(cost), key=lambda x: x[1])
                    print (i, j, [k for k in enumerate(cost)])
                    P[i][j] = P[i][j] + i + 1 
        return M,P

    
    def printOrder(self,P, i, j):
        if i == j:
            print ("A_{}".format(i+1), end="")
        else:
            print ("(", end="")
            self.printOrder(P, i, P[i][j]-1)
            self.printOrder(P, P[i][j], j)
            print (")",end="")
            

#4. Optimal Binary Search Tree and (Build Optimal Binary Search Tree)
class Node:
    def __init__(self, key, freq):
        self.key = key
        self.freq = freq
    def __repr__(self):
        return "Node({},{})".format(self.key, self.freq)

class OBST:
    def findMinCostRec(self, freq, i, j, level):
        if j < i:
            return 0
        minCost = sys.maxsize
        for k in range(i, j + 1):
            leftMinCost = self.findMinCostRec(freq, i, k - 1, level + 1)
            rightMinCost = self.findMinCostRec(freq, k + 1, j, level + 1)
            minCost = min(minCost, freq[k] * level + leftMinCost+ rightMinCost)
        return minCost
      
    def findMinCostDP(self,nodes):
        nodes.sort(key=lambda node: node.key)
        n = len(nodes)
 
        keys = [nodes[i].key for i in range(n)]
        freqs = [nodes[i].freq for i in range(n)]
        A = [[freqs[i] if i == j else 0 for j in range(n)] for i in range(n)]
        sumF = [[freqs[i] if i == j else 0 for j in range(n)] for i in range(n)]
        R = [[i if i == j else 0 for j in range(n)] for i in range(n)]
 
        for diagonal in range(2, n + 1):
            for i in range(n - diagonal + 1):
                j = i + diagonal - 1
                A[i][j] = sys.maxsize  # set the value to "infinity"
                sumF[i][j] = sumF[i][j - 1] + freqs[j]
                for k in range(R[i][j - 1], R[i + 1][j] + 1):  
                    left = A[i][k - 1] if k != i else 0  
                    right = A[k + 1][j] if k != j else 0  
                    cost = left + sumF[i][j] + right
 
                    if A[i][j] > cost:
                        A[i][j] = cost
                        R[i][j] = k
        return A,R
        
    def print_BST(self, root, key, i, j, parent, is_left):
        if i > j or i < 0 or j > len(root) - 1:
            return
 
        node = root[i][j]
        if parent == -1:  
            print(f"{key[node]} is the root of the binary search tree.")
        elif is_left:
            print(f"{key[node]} is the left child of key {parent}.")
        else:
            print(f"{key[node]} is the right child of key {parent}.")
 
        self.print_BST(root, key, i, node - 1, key[node], True)
        self.print_BST(root, key, node + 1, j, key[node], False)
        
        
        
        