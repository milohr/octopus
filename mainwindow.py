# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.8
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(579, 459)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.widget = QtWidgets.QWidget(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.results = QtWidgets.QToolButton(self.widget)
        icon = QtGui.QIcon.fromTheme("view-filter")
        self.results.setIcon(icon)
        self.results.setAutoRaise(True)
        self.results.setObjectName("results")
        self.verticalLayout.addWidget(self.results)
        self.dictionary = QtWidgets.QToolButton(self.widget)
        icon = QtGui.QIcon.fromTheme("format-text-symbol")
        self.dictionary.setIcon(icon)
        self.dictionary.setAutoRaise(True)
        self.dictionary.setObjectName("dictionary")
        self.verticalLayout.addWidget(self.dictionary)
        self.data = QtWidgets.QToolButton(self.widget)
        icon = QtGui.QIcon.fromTheme("flag-red")
        self.data.setIcon(icon)
        self.data.setAutoRaise(True)
        self.data.setObjectName("data")
        self.verticalLayout.addWidget(self.data)
        self.tags = QtWidgets.QToolButton(self.widget)
        icon = QtGui.QIcon.fromTheme("tag")
        self.tags.setIcon(icon)
        self.tags.setAutoRaise(True)
        self.tags.setObjectName("tags")
        self.verticalLayout.addWidget(self.tags)
        self.toolButton_4 = QtWidgets.QToolButton(self.widget)
        self.toolButton_4.setAutoRaise(True)
        self.toolButton_4.setObjectName("toolButton_4")
        self.verticalLayout.addWidget(self.toolButton_4)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout_2.addWidget(self.widget)
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_2.addWidget(self.frame_2)
        self.stackedWidget = QtWidgets.QStackedWidget(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.page)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.page)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.verticalLayout_2.addWidget(self.plainTextEdit)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.stackedWidget.addWidget(self.page_2)
        self.horizontalLayout_2.addWidget(self.stackedWidget)
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_2.addWidget(self.frame_4)
        self.widget_3 = QtWidgets.QWidget(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy)
        self.widget_3.setObjectName("widget_3")
        self.gridLayout = QtWidgets.QGridLayout(self.widget_3)
        self.gridLayout.setContentsMargins(12, 0, 12, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.ss1_spin = QtWidgets.QSpinBox(self.widget_3)
        self.ss1_spin.setObjectName("ss1_spin")
        self.gridLayout.addWidget(self.ss1_spin, 2, 2, 1, 2)
        self.ss3_spin = QtWidgets.QSpinBox(self.widget_3)
        self.ss3_spin.setObjectName("ss3_spin")
        self.gridLayout.addWidget(self.ss3_spin, 4, 2, 1, 2)
        self.fileLine = QtWidgets.QLineEdit(self.widget_3)
        self.fileLine.setObjectName("fileLine")
        self.gridLayout.addWidget(self.fileLine, 1, 1, 1, 1)
        self.ss2_line = QtWidgets.QLineEdit(self.widget_3)
        self.ss2_line.setObjectName("ss2_line")
        self.gridLayout.addWidget(self.ss2_line, 3, 1, 1, 1)
        self.urlLine = QtWidgets.QLineEdit(self.widget_3)
        self.urlLine.setText("")
        self.urlLine.setObjectName("urlLine")
        self.gridLayout.addWidget(self.urlLine, 0, 1, 1, 1)
        self.ss1_line = QtWidgets.QLineEdit(self.widget_3)
        self.ss1_line.setText("")
        self.ss1_line.setObjectName("ss1_line")
        self.gridLayout.addWidget(self.ss1_line, 2, 1, 1, 1)
        self.fileOpen = QtWidgets.QToolButton(self.widget_3)
        icon = QtGui.QIcon.fromTheme("folder-open")
        self.fileOpen.setIcon(icon)
        self.fileOpen.setObjectName("fileOpen")
        self.gridLayout.addWidget(self.fileOpen, 1, 3, 1, 1)
        self.ss3_line = QtWidgets.QLineEdit(self.widget_3)
        self.ss3_line.setObjectName("ss3_line")
        self.gridLayout.addWidget(self.ss3_line, 4, 1, 1, 1)
        self.fileSpin = QtWidgets.QSpinBox(self.widget_3)
        self.fileSpin.setObjectName("fileSpin")
        self.gridLayout.addWidget(self.fileSpin, 1, 2, 1, 1)
        self.ss2_spin = QtWidgets.QSpinBox(self.widget_3)
        self.ss2_spin.setObjectName("ss2_spin")
        self.gridLayout.addWidget(self.ss2_spin, 3, 2, 1, 2)
        self.urlSpin = QtWidgets.QSpinBox(self.widget_3)
        self.urlSpin.setObjectName("urlSpin")
        self.gridLayout.addWidget(self.urlSpin, 0, 2, 1, 2)
        self.startBtn = QtWidgets.QPushButton(self.widget_3)
        self.startBtn.setObjectName("startBtn")
        self.gridLayout.addWidget(self.startBtn, 5, 2, 1, 2)
        self.addBtn = QtWidgets.QToolButton(self.widget_3)
        icon = QtGui.QIcon.fromTheme("list-add")
        self.addBtn.setIcon(icon)
        self.addBtn.setObjectName("addBtn")
        self.gridLayout.addWidget(self.addBtn, 5, 1, 1, 1)
        self.horizontalLayout_2.addWidget(self.widget_3)
        self.horizontalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(1)
        self.actionQuit.triggered.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.results.setText(_translate("MainWindow", "..."))
        self.dictionary.setText(_translate("MainWindow", "..."))
        self.data.setText(_translate("MainWindow", "..."))
        self.tags.setText(_translate("MainWindow", "..."))
        self.toolButton_4.setText(_translate("MainWindow", "..."))
        self.fileLine.setPlaceholderText(_translate("MainWindow", "file seed"))
        self.ss2_line.setPlaceholderText(_translate("MainWindow", "semantic seed"))
        self.urlLine.setPlaceholderText(_translate("MainWindow", "url seed"))
        self.ss1_line.setPlaceholderText(_translate("MainWindow", "semantic seed"))
        self.fileOpen.setText(_translate("MainWindow", "..."))
        self.ss3_line.setPlaceholderText(_translate("MainWindow", "semantic seed"))
        self.startBtn.setText(_translate("MainWindow", "Start"))
        self.addBtn.setToolTip(_translate("MainWindow", "add semantic seed field"))
        self.addBtn.setText(_translate("MainWindow", "..."))
        self.actionQuit.setText(_translate("MainWindow", "&Quit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

