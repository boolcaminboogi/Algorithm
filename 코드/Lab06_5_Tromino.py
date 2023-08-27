#5-Divide and Conquer Algorithm Tromino Puzzle

class Tromino:
    def __init__(self, n=3, tileX=0, tileY=0):
        self.tno=0
        size = 2**n
        self.tileMap = [['x' if i==tileX and j==tileY else '0' for j in range(size)] for i in range(size)]
        if not self.isWithinBounds(tileX, tileY, 0, 0, size-1, size-1):
            print("Invalid tile coordinates...")
        else:
            self.printMap()
            self.solve(n,  0, size-1, 0, size-1, tileX, tileY)
            self.printMap()
       
    def isWithinBounds(self, tileX, tileY, startX, startY, endX, endY):
        return (startX <= tileX <= endX) and (startY <= tileY <= endY)



    def placeTiles(self,x1, y1, x2, y2, x3, y3):
        self.tno+=1
        self.tileMap[x1][y1] = self.tno
        self.tileMap[x2][y2] = self.tno
        self.tileMap[x3][y3] = self.tno


    def solve(self, n, startX, endX, startY, endY, tileX, tileY):
        cX, cY = self.getCenter(startX, endX, startY, endY)
        firstX, firstY = cX, cY
        secondX, secondY = cX+1, cY
        thirdX, thirdY = cX, cY+1
        fourthX, fourthY = cX+1, cY+1

        if tileX <= cX:
            if tileY <= cY:
                self.placeTiles(cX, cY+1, cX+1, cY+1, cX+1, cY)
                firstX, firstY = tileX, tileY
            else:
                self.placeTiles(cX, cY, cX+1, cY, cX+1, cY+1)
                secondX, secondY = tileX, tileY
        else:
            if tileY <= cY:
                self.placeTiles(cX, cY, cX, cY+1, cX+1, cY+1)
                thirdX, thirdY = tileX, tileY
            else:
                self.placeTiles(cX, cY, cX+1, cY, cX, cY+1)
                fourthX, fourthY = tileX, tileY

        if n==1:
            return
        else:
            self.solve(n-1, startX, cX, startY, cY, firstX, firstY)
            self.printMap()
            self.solve(n-1, startX, cX, cY, endY, secondX, secondY)
            self.printMap()
            self.solve(n-1, cX, endX, startY, cY, thirdX, thirdY)
            self.printMap()
            self.solve(n-1, cX, endX, cY, endY, fourthX, fourthY)
            self.printMap()

       
    def getCenter(self, startX, endX, startY, endY):
        return ((startX + endX) // 2, (startY + endY) // 2)

    def printMap(self):
        size = len(self.tileMap)
        print()
        for i in range(size):
            for j in range(size):
                print(" {:>3} ".format(self.tileMap[i][j]), end="")
            print()
        print()
