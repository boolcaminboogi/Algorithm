#1-Karatsubas Algorithm for Multiplication of Large Intergers

class Karatsuba:    
    def karatsubaMultiplication(self,x ,y):
        x = str(x)
        y = str(y)
    #base cases -
        if len(x) == 1 and len(y) == 1:
            return int(x) * int(y)
        if len(x) < len(y):
            x = self.zeroPad(x, len(y) - len(x))
        elif len(y) < len(x):
            y = self.zeroPad(y, len(x) - len(y))
    
        n = len(x)
        j = n//2
        if (n % 2) != 0:
            j += 1    
        BZeroPadding = n - j
        AZeroPadding = BZeroPadding * 2
        a = int(x[:j])
        b = int(x[j:])
        c = int(y[:j])
        d = int(y[j:])
        #recursive cases
        ac = self.karatsubaMultiplication(a, c)
        bd = self.karatsubaMultiplication(b, d)
        k = self.karatsubaMultiplication(a + b, c + d)
        A = int(self.zeroPad(str(ac), AZeroPadding, False))
        B = int(self.zeroPad(str(k - ac - bd), BZeroPadding, False))
        return A + B + bd
    
    def gradeSchoolMultiplication(self,x, y):
        x = str(x)
        y = str(y)
        zeroPadding = 0
        partialSum = 0
        for i in range(len(y) -1, -1, -1):
            carry = 0
            partial = ''
            partial = self.zeroPad(partial, zeroPadding, False)
        
            for j in range(len(x) -1, -1, -1):
                z = int(y[i])*int(x[j])
                z += carry
                z = str(z)
                if len(z) > 1:
                    carry = int(z[0])
                else:
                    carry = 0
            
                partial = z[len(z) -1] + partial
            if carry > 0:
                partial = str(carry) + partial
                
            partialSum += int(partial)
            zeroPadding += 1
        return partialSum
    
    def zeroPad(self,numberString, zeros, left = True):

        for i in range(zeros):
            if left:
                numberString = '0' + numberString
            else:
                numberString = numberString + '0'
        return numberString
