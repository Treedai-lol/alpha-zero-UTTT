#Board format: first 81 squares store the actual board data, 1 for O, 0 for none, -1 for X
#the next 9 stores boards that are won
#the next 9 stores the small boards to play in
#the next one is the player
from copy import deepcopy
class Board():
    def __init__(self, raw:list) -> None:
        assert(len(raw)==100)
        temp = []
        for i in range(9):
            temp.append(raw[9*i:9*i+9])
        self.bs = temp
        self.wonboards = raw[81:90]
        self.sb = raw[90:99]
        self.o = bool(raw[99])
    def GetOwnerShip(self,index:int,o:bool) ->list: #returns the indices of pieces owned
        output = []
        if o:
            for i in range(0,9):
                if self.bs[index][i] == 1:
                    output.append(i)
        else:
            for i in range(0,9):
                if self.bs[index][i] == -1:
                    output.append(i)
        return output
    def MakeMove(self,player,a:int,b:int): #merged with BoardFinished
        o = player
        if o:
            self.bs[a][b] = 1
        else:
            self.bs[a][b] = 2
        if self.wonboards[b] != 0:
            self.sb = 9
        else:
            self.sb = b
        index = a
        output = False
        piecelist = self.GetOwnerShip(index,o)
        winning = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
        for i in winning:
            a = b = c = False
            for j in piecelist:
                if j == i[0]:
                    a = True
                if j == i[1]:
                    b = True
                if j == i[2]:
                    c = True
            if a and b and c:
                output = True
        if output & o == True:
            self.wonboards[index] = 1
        elif output:
            self.wonboards[index] = 2
        self.o = not o
        return self
    def UnmakeMove(self,a:int,b:int,prevsb:int)->None:
        o = self.o
        self.bs[a][b] = 0
        self.sb = prevsb
        index = a
        output = False
        piecelist = self.GetOwnerShip(index,o)
        winning = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
        for i in winning:
            a = b = c = False
            for j in piecelist:
                if j == i[0]:
                    a = True
                if j == i[1]:
                    b = True
                if j == i[2]:
                    c = True
            if a and b and c:
                output = True
        if not output:
            self.wonboards[index] = 0
        self.o = not o
    def GameFinished(self,o:bool) ->bool: #returns whether the game has been finished
        output = False
        tmp = self.wonboards
        piecelist = []
        if o:
            for i in range(0,9):
                if  tmp[i] == 1:
                    piecelist.append(i)
        else:
            for i in range(0,9):
                if  tmp[i] == 2:
                    piecelist.append(i)
        winning = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
        for i in winning:
            a = b = c = False
            for j in piecelist:
                if j == i[0]:
                    a = True
                if j == i[1]:
                    b = True
                if j == i[2]:
                    c = True
            if a and b and c:
                output = True
        return output
    def tostring(self):
        string = ""
        for i in range(9):
            for j in range(9):
                string+=str(self.bs[i][j])
        for i in range(9):
            string+=str(self.wonboards[i])
        string+=str(self.sb)
        string+=str(int(self.o))
        return string
    def flatten(self)->list:
        ret = []
        ret.append(self.bs)
        ret.append(self.wonboards)
        ret.append(self.sb)
        ret.append(int(self.o))
        return ret
    def PrintBoard(board) ->None: #print board function
        for i in range(0,3):
            for j in range(0,3):
                for k in range(3*i,3*i+3):
                    for l in range(3*j,3*j+3):
                        print(board.bs[k][l],end=" ")
                    print(" ",end="")
                print("\n",end="")
            print("\n",end="")
        pass
def main():
    board = []
    for i in range(100):
        board.append(0)
    b = Board(board)
    b.PrintBoard()
if __name__=='__main__':
    main()