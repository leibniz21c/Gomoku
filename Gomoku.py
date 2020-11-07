import numpy as np
from scipy import sparse


# Protocol, static

GAME_BLACK_TURN = 2
GAME_WHITE_TURN = 3
GAME_BLACK_WIN = 4
GAME_WHITE_WIN = 5

RES_CANNOT = 8
RES_NOTHING = 9
RES_THREE_THREE = 10
RES_BLACK_WIN = 11
RES_WHITE_WIN = 12

STONE_BLANK = 0
STONE_BLACK = 1
STONE_WHITE = -1

class Game:
    """
    희소행렬 아님. 

    game.board로 보드 접근
    game.put
    """
    turn = GAME_BLACK_TURN # = GAME_BALCK_TURN
    board = np.zeros((19, 19), dtype=int)

    def __init__(self):
        self.board = np.zeros((19, 19), dtype=int)
        self.turn = GAME_BLACK_TURN


    def putStone(self, x, y, type):
        res = self.isStoneValid(x, y, type)
        if res == RES_CANNOT:
            return RES_CANNOT
        elif res == RES_NOTHING:
            if type == STONE_BLACK:
                self.turn = GAME_WHITE_TURN
            elif type == STONE_WHITE:
                self.turn = GAME_BLACK_TURN
            self.board[x, y] = type
            return RES_NOTHING
        elif res == RES_THREE_THREE:
            return RES_THREE_THREE
        elif res == RES_BLACK_WIN:
            self.flag = GAME_BLACK_WIN
            return RES_BLACK_WIN
        else :
            self.flag = GAME_WHITE_WIN
            return RES_WHITE_WIN

    def isStoneValid(self, x, y, type):
        """
        삼삼같은거 걸러내고 게임 셋까지 다 확인
        return : RES_*
        """
        dir = ((0, 1), (1, 1), (1, 0), (1, -1))
        dir_stack = []

        if self.board[x, y] != STONE_BLANK:
            return RES_CANNOT
        
        if self.turn == GAME_BLACK_WIN or self.turn == GAME_WHITE_WIN:
            return RES_CANNOT

        for i in range(4):
            posX, posY = x, y
            dir_stack.append([])
            dir_stack[i].append((posX, posY))

            posX += dir[i][0]
            posY += dir[i][1]
            while posX >= 0 and posX < 19 and  posY >= 0 and posY < 19 and self.board[posX, posY] == type:
                dir_stack[i].append((posX, posY))
                posX += dir[i][0]
                posY += dir[i][1]

            posX, posY = x, y
            posX -= dir[i][0]
            posY -= dir[i][1]
            while posX >= 0 and posX < 19 and  posY >= 0 and posY < 19 and self.board[posX, posY] == type:
                dir_stack[i].append((posX, posY))
                posX -= dir[i][0]
                posY -= dir[i][1]
        
        tt_cnt = 0
        for i in range(4):
            if len(dir_stack[i]) == 5:
                if type == STONE_BLACK :
                    self.flag = GAME_BLACK_WIN
                    return RES_BLACK_WIN
                else :
                    self.flag = GAME_WHITE_WIN
                    return RES_WHITE_WIN
            elif len(dir_stack[i]) == 3:
                tt_cnt += 1
            if tt_cnt == 2:
                return RES_THREE_THREE

        return RES_NOTHING