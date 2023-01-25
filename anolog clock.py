from turtle import pen
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
#from PyQt5.QtWidgets import sip
import sys 

class Clock(QMainWindow):
    def __init__(self):
        super().__init__()
        #timer
        timer = QTimer(self)
        #lost connection
        # adding timer and updating the whole code
        timer.timeout.connect(self.update)

        timer.start(1000)
        self.setWindowTitle("Pro clok")
        self.setGeometry(200,200,300,300)

        self.setStyleSheet("background : white;")
        self.hPointer = QtGui.QPolygon([QPoint(6,7),QPoint(-6,7),QPoint(0,-50)])

        self.mPointer = QtGui.QPolygon([QPoint(6,7),QPoint(-6,7),QPoint(0,-70)])

        self.sPointer = QtGui.QPolygon([QPoint(1,1),QPoint(-1,1),QPoint(0,-90)])

        self.bColor = Qt.green

        self.sColor = Qt.red

    def PaintEvent(self,event):
        rec = min(self.width(),self.height())
        tik =QTime.currentTime()
        painter = QPainter(self)

        def drawPointer(color,rotation,pointer):
            painter.setBrush(QBrush(color))
            painter.save()
            painter.rotate(rotation)
            painter.drawConvexPolygon(pointer)
            painter.restore()

        painter.setRenderHint()
        painter.translate(self.width()/2,self.height()/2)
        painter.scale(rec/200,rec/200)
        painter.setPen(QtCore.Qt.NoPen)
        drawPointer(self.bColor, (30 * (tik.hour() + tik.minute() / 60)), self.hPointer)
        drawPointer(self.bColor, (6 * (tik.minute() + tik.second() / 60)), self.mPointer)
        drawPointer(self.sColor, (6 * tik.second()), self.sPointer)
        painter.setPen(QPen(self.bColor))
        # for loop
        for i in range(0,60):
            #for drawing background lines
            if (i % 5) == 0:
                painter.drawLine(87,0,97,0)
            painter.rotate(6)
        painter.end()

if __name__ == '__main__':
    app = QApplication(sys.argv)

    win = Clock()

win.show()

exit(app.exec_())