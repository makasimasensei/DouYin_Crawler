import time

from PyQt5.QtCore import QRect, Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QPushButton, QLineEdit, QProgressBar

from MyThread import MyThread
from ui.MyWidget import MyWidget


class Ui_Widget:
    def __init__(self):
        super().__init__()
        self.Widget = MyWidget()
        self.closeButton = QPushButton(self.Widget)
        self.minimizeButton = QPushButton(self.Widget)
        self.lineEdit = QLineEdit(self.Widget)
        self.progressBar = QProgressBar(self.Widget)
        self.thread = MyThread(self.lineEdit, self.progressBar)

    def setupWidget(self):
        self.Widget.resize(1170, 630)
        self.Widget.show()

    def setupCloseButton(self):
        font = QFont()
        font.setPointSize(14)
        self.closeButton.setObjectName("closeButton")
        self.closeButton.setGeometry(QRect(1120, 0, 50, 30))
        self.closeButton.setFont(font)
        self.closeButton.setStyleSheet(
            "QPushButton{background-color:#d6eef5;border-top-right-radius: 25px;border-bottom-left-radius: 10px;}\n"
            "QPushButton:hover{ background-color: #bed7df;}")
        self.closeButton.setText("×")
        self.closeButton.clicked.connect(self.Widget.close)

    def setupMinimizeButton(self):
        font = QFont()
        font.setPointSize(14)
        self.minimizeButton.setObjectName("minimizeButton")
        self.minimizeButton.setGeometry(QRect(1070, 0, 50, 30))
        self.minimizeButton.setFont(font)
        self.minimizeButton.setStyleSheet(
            "QPushButton{background-color:#d6eef5;border-bottom-left-radius: 10px;border-bottom-right-radius: 10px}\n"
            "QPushButton:hover{ background-color: #bed7df;}")
        self.minimizeButton.setText("_")
        self.minimizeButton.clicked.connect(self.Widget.showMinimized)

    def setupLineEdit(self):
        self.lineEdit.setGeometry(QRect(300, 200, 500, 40))
        line_font = QFont()
        line_font.setFamily("Times New Roman")
        line_font.setPointSize(16)
        self.lineEdit.setFont(line_font)
        self.lineEdit.setAlignment(Qt.AlignCenter)
        self.lineEdit.setStyleSheet(
            "QLineEdit{background-color:#ffffff;border: 1px solid #ffffff;border-style: outset;border-radius: 0px;}"
            "QLineEdit:hover {background-color: #ebebeb;}")
        self.lineEdit.setObjectName("ui_3_pageEdit")
        self.lineEdit.setPlaceholderText("输入")
        self.lineEdit.returnPressed.connect(self.startTask)

    def setupProgressBar(self):
        self.progressBar.setGeometry(QRect(315, 300, 500, 40))

    def startTask(self):
        self.thread.start()

    def setupUi(self):
        self.setupWidget()
        self.setupCloseButton()
        self.setupMinimizeButton()
        self.setupLineEdit()
        self.setupProgressBar()
