from lab01 import *

def testSS():
    lab1 = lab01()
    S = [10,34, 22, 25, 90, 10, 63, 67]
    x = 90
    loc=lab1.ssearch(S, x)
    if loc == -1:
        print("Element fount at", loc)
    else:
        print("Element not fount")
        
def main():
    testSS()
    lab1=lab01()
    print("Lets start here")
    print("{}th fibbonacci term using itractive here is = {}", format(n, lab1.fibonacciItr(n)))
    #print("{}th fibbonacci term using recursion here is = {}", format(n, lab1.fibonacciRec(n)))#훨씬 느