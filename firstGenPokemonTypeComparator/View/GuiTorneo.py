# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GuiTorneo.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1005, 632)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(40, 10, 856, 452))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.pkmsemifinal2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.pkmsemifinal2.setText("")
        self.pkmsemifinal2.setObjectName("pkmsemifinal2")
        self.gridLayout.addWidget(self.pkmsemifinal2, 5, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 3, 6, 1, 1)
        self.pokemon6 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.pokemon6.setText("")
        self.pokemon6.setPixmap(QtGui.QPixmap("images/unknown.png"))
        self.pokemon6.setObjectName("pokemon6")
        self.gridLayout.addWidget(self.pokemon6, 2, 10, 1, 1)
        self.pkmfinal1 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.pkmfinal1.setText("")
        self.pkmfinal1.setObjectName("pkmfinal1")
        self.gridLayout.addWidget(self.pkmfinal1, 3, 3, 1, 1)
        self.pkmfinal2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.pkmfinal2.setText("")
        self.pkmfinal2.setObjectName("pkmfinal2")
        self.gridLayout.addWidget(self.pkmfinal2, 3, 7, 1, 1)
        self.winner = QtWidgets.QLabel(self.gridLayoutWidget)
        self.winner.setText("")
        self.winner.setPixmap(QtGui.QPixmap("images/corona.png"))
        self.winner.setObjectName("winner")
        self.gridLayout.addWidget(self.winner, 3, 5, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 5, 0, 1, 1)
        self.pokemon1 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.pokemon1.setText("")
        self.pokemon1.setPixmap(QtGui.QPixmap("images/unknown.png"))
        self.pokemon1.setObjectName("pokemon1")
        self.gridLayout.addWidget(self.pokemon1, 0, 0, 1, 1)
        self.pkmsemifinal3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.pkmsemifinal3.setText("")
        self.pkmsemifinal3.setObjectName("pkmsemifinal3")
        self.gridLayout.addWidget(self.pkmsemifinal3, 1, 8, 1, 1)
        self.pokemon3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.pokemon3.setText("")
        self.pokemon3.setPixmap(QtGui.QPixmap("images/unknown.png"))
        self.pokemon3.setObjectName("pokemon3")
        self.gridLayout.addWidget(self.pokemon3, 4, 0, 1, 1)
        self.pokemon4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.pokemon4.setText("")
        self.pokemon4.setPixmap(QtGui.QPixmap("images/unknown.png"))
        self.pokemon4.setObjectName("pokemon4")
        self.gridLayout.addWidget(self.pokemon4, 6, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 3, 4, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 3, 0, 1, 1)
        self.pokemon7 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.pokemon7.setText("")
        self.pokemon7.setPixmap(QtGui.QPixmap("images/unknown.png"))
        self.pokemon7.setObjectName("pokemon7")
        self.gridLayout.addWidget(self.pokemon7, 4, 10, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 1, 0, 1, 1)
        self.pokemon2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.pokemon2.setText("")
        self.pokemon2.setPixmap(QtGui.QPixmap("images/unknown.png"))
        self.pokemon2.setObjectName("pokemon2")
        self.gridLayout.addWidget(self.pokemon2, 2, 0, 1, 1)
        self.pkmsemifinal1 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.pkmsemifinal1.setText("")
        self.pkmsemifinal1.setObjectName("pkmsemifinal1")
        self.gridLayout.addWidget(self.pkmsemifinal1, 1, 2, 1, 1)
        self.pkmsemifinal4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.pkmsemifinal4.setText("")
        self.pkmsemifinal4.setObjectName("pkmsemifinal4")
        self.gridLayout.addWidget(self.pkmsemifinal4, 5, 8, 1, 1)
        self.pokemon8 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.pokemon8.setText("")
        self.pokemon8.setPixmap(QtGui.QPixmap("images/unknown.png"))
        self.pokemon8.setObjectName("pokemon8")
        self.gridLayout.addWidget(self.pokemon8, 6, 10, 1, 1)
        self.pokemon5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.pokemon5.setText("")
        self.pokemon5.setPixmap(QtGui.QPixmap("images/unknown.png"))
        self.pokemon5.setObjectName("pokemon5")
        self.gridLayout.addWidget(self.pokemon5, 0, 10, 1, 1)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(200, 480, 501, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_3.addWidget(self.pushButton)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem5)
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_3.addWidget(self.pushButton_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1005, 32))
        self.menubar.setObjectName("menubar")
        self.menuConcurso_Pokemon = QtWidgets.QMenu(self.menubar)
        self.menuConcurso_Pokemon.setObjectName("menuConcurso_Pokemon")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuConcurso_Pokemon.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Generar"))
        self.pushButton_2.setText(_translate("MainWindow", "Limpiar Pantalla"))
        self.menuConcurso_Pokemon.setTitle(_translate("MainWindow", "Concurso Pokemon"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
