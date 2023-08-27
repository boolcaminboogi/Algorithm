#2-Strassen's Algorithm for Matrix multiplication
import numpy as np 


class Strassen:
    def strassen(self,A, B): 		
        n = len(A)
        if n == 1:         	
            return A * B 		

        n2 = n//2
        A11, A12, A21, A22 = A[:n2, :n2], A[:n2, n2:], A[n2:, :n2], A[n2:, n2:] 
        B11, B12, B21, B22 = B[:n2, :n2], B[:n2, n2:], B[n2:, :n2], B[n2:, n2:] 

        M1 = self.strassen(A11+A22, B11+B22)   
        M2 = self.strassen(A21+A22, B11)         
        M3 = self.strassen(A11, B12-B22)         
        M4 = self.strassen(A22, B21-B11)         
        M5 = self.strassen(A11+A12, B22)         
        M6 = self.strassen(A21-A11, B11+B12)   
        M7 = self.strassen(A12-A22, B21+B22)   
  
        C11 = M1 + M4 - M5 + M7   
        C12 = M3 + M5            
        C21 = M2 + M4             
        C22 = M1 + M3 - M2 + M6   		
  
        C = np.vstack((np.hstack((C11, C12)), np.hstack((C21, C22))))  
  
        return C
    

    def multiply(self,A, B, C) :
        n = len(A)
        for i in range(n):						
            for j in range(n):					
                C[i][j] = 0
                for k in range(n):				
                    C[i][j] += A[i][k]*B[k][j]
        return C
