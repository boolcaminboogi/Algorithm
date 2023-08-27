#2 Do the complexity Analysis for the given algorithms and code them

#2-1	V
def unique_elements(self, A):
    n=len(A)
    for i in range(n-1):
        for j in range(i+1, n):
            if A[i] ==A[j]:
                return False
    return True


#procedure UE(A[0..n-1]):
#for i in range(0, n-1):
#    for j in range(i+1, n):
#        if A[i]==A[j]:
#            return False
#return True        


#2-2 시간 효율적인 알고리즘을 찾아라			V
def GE(self, A):
    n=len(A)
    for i in range(n-1):
    for j in range(i+1, n):
        ratio = A[j][i]/A[i][i]
        for k in range(n+1):
            A[j, k] = A[j][k]-A[i][k]*ratio
    print(A)
            
#procedure GE(A[0..n-1, 0 ..n])
:
#for i in range(0,n-1):
#    for j in range(i+1, n):
#        for k in range(i, n+1):
#            A[j, k] = A[j,k]-A[i,k]*A[j,i]/A[i,i]
            
            
#2-3. n^2을 2^n = 2^n−1 + 2^n−1 공식을 사용해 재귀적으로 풀어라
def power2b(self, n):
#procedure power2(n):
    if(n==0) : return 1
    else : return self.power2b(n-1)+self.power2b(n-1)

#2-3-1
def power2(self, n):
    if n==0:
        return 1
    if n&1:
        return 2*self.power2(n//2)*self.power2(n//2)
    return self.power2(n//2)*self.power(n//2)
    
    
#2-4. 한계단 또는 두계단을 사용해 n계단을 오르는 방법의 수를 구하시오.
#ex)3계단 : 1-1-1, 1-2, 2-1 / 4계단 : 1-1-1-1, 1-2-1, 2-1-2, 2-2 등
 def ways(self, n):
     if n<=2:
         return n
        else: return self.ways(n-1)+self.ways(n-2)

    
#2-5 공약수(반복)
def gcd(self, a, b):
    print("gcd", (a,b))
    while b >0:
        r=a%b
        a=b
        b=r
    print("gcd", (a,b))
    
#procedure gcd((int a, int b))
#    integerr
#    while(b>0):
#        r=a%b
#        a=b
#        b=r


#2-6 공약수(재귀)
procedure gcd((int a, int b))
    if(b=0): return a
    else: return gcd(b, a%b)
    
    
    
    
        def compute_square_A(self, n):
        return n*n
    
    def compute_square_B(self, n):
        sum=0
        for i in range(n):
            sum=sum+n
        return sum
    
    def compute_square_C(self, n):
        sum=0
        for i in range(n):
            for j in range(n):
                sum=sum+1
        return sum
    
                    
    def binary_digits_Rec(self, n):
        if n==1:
            return 1
        else:
            return 1+self.binary_digits_Rec(n//2)
        
    def binary_digits(self, n):
        count=1
        while n>1:
            count=count+1
            n=n//2
        return count


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    