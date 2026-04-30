from UTTT.UTTTLogic import Board
import numpy as np
class UTTTGame():
    """
    This class specifies the base Game class. To define your own game, subclass
    this class and implement the functions below. This works when the game is
    two-player, adversarial and turn-based.

    Use 1 for player1 and -1 for player2.

    See othello/OthelloGame.py for an example implementation.
    """
    def __init__(self,n):
        self.n = n
        pass

    def getInitBoard(self):
        board = []
        for i in range(90):
            board.append(0)
        for i in range(9):
            board.append(1)
        board.append(1)
        return board

    def getBoardSize(self):
        return (self.n,self.n)

    def getActionSize(self):
        return self.n*self.n

    def getNextState(self, board:Board, player, action):
        """
        Input:
            board: current board
            player: current player (1 or -1)
            action: action taken by current player

        Returns:
            nextBoard: board after applying action
            nextPlayer: player who plays in the next turn (should be -player)
        """
        board[action[0],action[1]] = player
        return board

    def getValidMoves(self, board, player):
        """
        Input:
            board: current board
            player: current player

        Returns:
            validMoves: a binary vector of length self.getActionSize(), 1 for
                        moves that are valid from the current board and player,
                        0 for invalid moves
        """
        player
        movelist = []
        board[81] = 
        if board[81] != 9:
            for i in range(0,9):
                if board[] == 0:
                    movelist.append([board.sb,i])
        else:
            for i in range(0,9):
                for j in range(0,9):
                    if board.bs[i][j] == 0:
                        movelist.append([i,j])
        legalMoves = movelist
        valids = [0]*self.getActionSize()
        if len(legalMoves)==0:
            valids[-1]=1
            return np.array(valids)
        for x, y in legalMoves:
            valids[9*x+y]=1
        return np.array(valids)

    def getGameEnded(self, board:Board, player):
        """
        Input:
            board: current board
            player: current player (1 or -1)

        Returns:
            r: 0 if game has not ended. 1 if player won, -1 if player lost,
               small non-zero value for draw.
               
        """
        if(player==1):
            o = True
        else:
            o = False
        if board.GameFinished(o):
            return 1
        elif board.GameFinished(not o):
            return -1
        else:
            movelist = []
            if board.sb != 9:
                for i in range(0,9):
                    if board.bs[board.sb][i] == 0:
                        movelist.append([board.sb,i])
            else:
                for i in range(0,9):
                    for j in range(0,9):
                        if board.bs[i][j] == 0:
                            movelist.append([i,j])
            if movelist==[]:
                return 0.0000001
        return 0

    def getCanonicalForm(self, board:Board, player):
        """
        Input:
            board: current board
            player: current player (1 or -1)

        Returns:
            canonicalBoard: returns canonical form of board. The canonical form
                            should be independent of player. For e.g. in chess,
                            the canonical form can be chosen to be from the pov
                            of white. When the player is white, we can return
                            board as is. When the player is black, we can invert
                            the colors and return the board.
        """
        return Board(player*board.bs,board.wonboards,board.o,board.sb).flatten()

    def getSymmetries(self, board:Board, pi):
        """
        Input:
            board: current board
            pi: policy vector of size self.getActionSize()

        Returns:
            symmForms: a list of [(board,pi)] where each tuple is a symmetrical
                       form of the board and the corresponding pi vector. This
                       is used when training the neural network from examples.
        """
                # mirror, rotational
        assert(len(pi) == self.n**2+1)  # 1 for pass
        pi_board = np.reshape(pi[:-1], (self.n, self.n))
        wb_board = np.reshape(board.wonboards,(self.n,self.n))
        temp = []
        for i in range(0,9):
                temp.append(0)
        temp[board.sb-1] = 1
        l = []
        o = board.o
        sb_board = np.reshape(temp,(self.n,self.n))
        for i in range(1, 5):
            for j in [True, False]:
                newB = Board(np.rot90(board.bs, i),np.rot90(wb_board, i),o,np.rot90(sb_board, i))
                newPi = np.rot90(pi_board, i)
                if j:
                    newB = Board(np.fliplr(board.bs, i),np.fliplr(wb_board, i),o,np.fliplr(sb_board, i))
                    newPi = np.fliplr(newPi)
                l += [(newB, list(newPi.ravel()) + [pi[-1]])]
        return l

    def stringRepresentation(self, board):
        """
        Input:
            board: CANONICAL BOARD FFS

        Returns:
            boardString: a quick conversion of board to a string format.
                         Required by MCTS for hashing.
        """
        ret = ""
        for i in range(len(board)):
            ret+=(board[i])
        return ret
    
    @staticmethod
    def PrintBoard(board:Board) ->None: #print board function
        for i in range(0,3):
            for j in range(0,3):
                for k in range(3*i,3*i+3):
                    for l in range(3*j,3*j+3):
                        print(board.bs[k][l],end=" ")
                    print(" ",end="")
                print("\n",end="")
            print("\n",end="")
        pass
