"""
    대충 강화학습용 오목
"""
import sys
import Gomoku
from PyQt5.QtWidgets import QWidget, QApplication, QMessageBox
from PyQt5.QtGui import QPainter, QPen, QColor, QBrush
from PyQt5.QtCore import Qt
import ctypes
import math

# Board in Window
BOARD_START_X = 100
BOARD_START_Y = 100
GAP = 20

# Function
def pointToBoard(x, y):
    return (BOARD_START_X + GAP*x, BOARD_START_Y + GAP*y)

class GameWindow(QWidget):
    game = Gomoku.Game()

    # Constructor
    def __init__(self):
        super().__init__()
        self.setGeometry(0, 0, 800, 600)
        self.setWindowTitle("Gomoku!")
        self.show()

    def mousePressEvent(self, e):
        if e.button() == Qt.LeftButton:
            print(BOARD_START_X, BOARD_START_Y, BOARD_START_X + 18*GAP, BOARD_START_Y + 18*GAP)
            x = e.x()
            y = e.y()
            radius = int(GAP/2 - 2)
            print(x, y, radius)
            # Just for this program
            if x > 100 - radius and x < 460 + radius:
                if y > 100 - radius and y < 460 + radius:
                    x = round((x - 100)/20)
                    y = round((y - 100)/20) 
                    if self.game.turn == Gomoku.GAME_BLACK_TURN:
                        res = self.game.putStone(x, y, Gomoku.STONE_BLACK)
                        # TODO:
                        if res == Gomoku.RES_BLACK_WIN:
                            self.game.flag = Gomoku.GAME_BLACK_TURN
                            self.game.__init__()
                            QMessageBox.about(self, "System", "Black Win!")
                        if res == Gomoku.RES_CANNOT:
                            QMessageBox.about(self, "System", "You cannot set here!")
                        if res == Gomoku.RES_THREE_THREE:
                            QMessageBox.about(self, "System", "Black must follow three three rule!")
                    elif self.game.turn == Gomoku.GAME_WHITE_TURN:
                        res = self.game.putStone(x, y, Gomoku.STONE_WHITE)
                        # TODO:
                        if res == Gomoku.RES_WHITE_WIN:
                            self.game.flag = Gomoku.GAME_WHITE_TURN
                            self.game.__init__()
                            QMessageBox.about(self, "System", "White Win!")
                        if res == Gomoku.RES_CANNOT:
                            QMessageBox.about(self, "System", "You cannot set here!")
            self.update()
        
    def paintEvent(self, e):
        # Callback
        qp = QPainter()
        qp.begin(self)
        self.draw_board(qp)
        qp.end()
    
    def draw_board(self, qp):
        qp.setBrush(QColor(255, 255, 255))
        qp.drawRect(0, 0, 800, 600)

        qp.setPen(QPen(Qt.black, 1, Qt.SolidLine))
        startX, startY = (100, 100)
        gap = 20

        for i in range(19):
            qp.drawLine(startX, startY + i*gap, startX + 18*gap, startY + i*gap)
            qp.drawLine(startX + i*gap, startY, startX + i*gap, startY + 18*gap)

        qp.setPen(QPen(Qt.black, 5, Qt.SolidLine))
        for i in range(3):
            for j in range(3):
                x, y = pointToBoard(3 + 6*i, 3 + 6*j)
                qp.drawPoint(x, y)

        for i in range(19):
            for j in range(19):
                if self.game.board[i, j] == Gomoku.STONE_BLACK:
                    self.draw_stone(i, j, Gomoku.STONE_BLACK, GAP, qp)
                elif self.game.board[i, j] == Gomoku.STONE_WHITE:
                    self.draw_stone(i, j, Gomoku.STONE_WHITE, GAP, qp)

    
    def draw_stone(self, x, y, type, gap, qp):
        cord_x, cord_y = pointToBoard(x, y)
        radius = int(gap/2 - 2)
        if type == Gomoku.STONE_BLACK:
            qp.setPen(QPen(Qt.black, 1))
            for i in range(cord_x-radius, cord_x+radius):
                for j in range(cord_y-radius, cord_y+radius):
                    if (cord_x-i) ** 2 + (cord_y-j) ** 2 <= radius ** 2 :
                        qp.drawPoint(i, j)

        elif type == Gomoku.STONE_WHITE:
            qp.setPen(QPen(Qt.white, 1))
            for i in range(cord_x-radius, cord_x+radius):
                for j in range(cord_y-radius, cord_y+radius):
                    if (cord_x-i) ** 2 + (cord_y-j) ** 2 <= radius ** 2 :
                        qp.setPen(QPen(Qt.white, 1))
                        qp.drawPoint(i, j)
                    if radius ** 2 - GAP < (cord_x-i) ** 2 + (cord_y-j) ** 2  and (cord_x-i) ** 2 + (cord_y-j) ** 2 < radius ** 2 : 
                        qp.setPen(QPen(Qt.black, 1))
                        qp.drawPoint(i, j)
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = GameWindow()

    # TODO : Shell Control

    sys.exit(app.exec_())