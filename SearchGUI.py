# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Search.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets
from Search import Search
import sys
import pyperclip
from HelperWindows import DataFrameView, StandardErrorDialog
import os
from datetime import datetime
import logging
logger = logging.getLogger(__name__)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(421, 340)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(20, 10, 381, 311))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.gridLayout.setObjectName("gridLayout")
        self.SearchData = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.SearchData.setFont(font)
        self.SearchData.setObjectName("SearchData")
        self.gridLayout.addWidget(self.SearchData, 1, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.horizontalLayout.setSpacing(4)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.SearchDataButton = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SearchDataButton.sizePolicy().hasHeightForWidth())
        self.SearchDataButton.setSizePolicy(sizePolicy)
        self.SearchDataButton.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.SearchDataButton.setFont(font)
        self.SearchDataButton.setObjectName("SearchDataButton")
        self.horizontalLayout.addWidget(self.SearchDataButton)
        self.ClipboardButton = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ClipboardButton.sizePolicy().hasHeightForWidth())
        self.ClipboardButton.setSizePolicy(sizePolicy)
        self.ClipboardButton.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.ClipboardButton.setFont(font)
        self.ClipboardButton.setObjectName("ClipboardButton")
        self.horizontalLayout.addWidget(self.ClipboardButton)
        self.gridLayout.addLayout(self.horizontalLayout, 5, 0, 1, 1)
        self.SearchButton = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.SearchButton.setFont(font)
        self.SearchButton.setObjectName("SearchButton")
        self.gridLayout.addWidget(self.SearchButton, 2, 0, 1, 1)
        self.line = QtWidgets.QFrame(self.gridLayoutWidget_3)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 4, 0, 1, 1)
        self.ResultsBox = QtWidgets.QComboBox(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.ResultsBox.setFont(font)
        self.ResultsBox.setObjectName("ResultsBox")
        self.gridLayout.addWidget(self.ResultsBox, 3, 0, 1, 1)
        self.SearchLabel = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.SearchLabel.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SearchLabel.sizePolicy().hasHeightForWidth())
        self.SearchLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.SearchLabel.setFont(font)
        self.SearchLabel.setObjectName("SearchLabel")
        self.gridLayout.addWidget(self.SearchLabel, 0, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.SearchButton.clicked.connect(self.getSearchResults)
        self.ClipboardButton.clicked.connect(self.copyToClipboard)
        self.SearchDataButton.clicked.connect(self.createDataFrameWindow)

        self.retValSearch = -2
        self.searchObj = Search()
        logger.info("Search object added")
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        logger.info("SearchGUI window initialized!")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Search GUI"))
        self.SearchDataButton.setText(_translate("MainWindow", "SEARCH DATA TABLE"))
        self.ClipboardButton.setText(_translate("MainWindow", "COPY SELECTED TO CLIPBOARD"))
        self.SearchButton.setText(_translate("MainWindow", "Search!"))
        self.SearchLabel.setText(_translate("MainWindow", "Search Your Stock by Name"))

    def getSearchResults(self):
        data = self.SearchData.text()
        self.searchObj.setName(data.strip())
        self.retValSearch = self.searchObj.topResults()
        if self.retValSearch == -1:
            self.dialog = StandardErrorDialog(parent=None, text=f"Nothing returned for this name: {data}!")
            self.dialog.ui.pushButton.clicked.connect(self.dialog.close)
            self.dialog.exec()
            logger.error(f"Nothing returned for this name: {data}!")
            return
        self.ResultsBox.clear()
        self.ResultsBox.addItems(self.searchObj.results)
        logger.info(f"Items{len(self.searchObj.results)} added from search results!")

    def copyToClipboard(self):
        if self.retValSearch == -2 or self.retValSearch == -1:
            self.dialog = StandardErrorDialog(parent=None, text="Nothing to copy, please enter valid company name and click on 'Search!' Button")
            self.dialog.ui.pushButton.clicked.connect(self.dialog.close)
            self.dialog.exec()
            logger.error("Nothing to copy!")
            return

        data = (self.ResultsBox.currentText().split('-')[1]).strip()
        pyperclip.copy(data)
        logger.info(f"This stock:{data} has been copied successfully!")

    def createDataFrameWindow(self):
        if self.retValSearch == -1:
            self.dialog = StandardErrorDialog(parent=None, text="No results available for this stock name!")
            self.dialog.ui.pushButton.clicked.connect(self.dialog.close)
            self.dialog.exec()
            logger.error("No results available for this stock name!")
            return
        if self.retValSearch == -2:
            self.dialog = StandardErrorDialog(parent=None, text="You haven't searched for anything!")
            self.dialog.ui.pushButton.clicked.connect(self.dialog.close)
            self.dialog.exec()
            logger.error("No search has been done!")
            return
        self.dataWindow = DataFrameView()
        self.dataWindow.setData(self.searchObj.resultsDataFrame)
        self.dataWindow.show()
        logger.info("DataFrameView created!")


if __name__ == "__main__":
    if os.path.isdir('logs'):
        if os.path.isdir('logs/searchgui'):
            pass
        else:
            os.mkdir('logs/searchgui')
    else:
        os.mkdir('logs')
        if os.path.isdir('logs/searchgui'):
            pass
        else:
            os.mkdir('logs/searchgui')

    logFile = 'logs/searchgui/{}.log'.format(
        datetime.now().strftime("%d-%m-%y"))
    logForm = '%(asctime)s.%(msecs)03d %(levelname)s %(module)s -\
%(funcName)s: %(message)s'
    logging.basicConfig(filename=logFile,
                        filemode='a',
                        format=logForm,
                        datefmt='%Y-%m-%d %H:%M:%S',
                        level=logging.DEBUG)
    logging.debug("----- PROGRAM[SearchGUI.py] RUN START FROM HERE -----")

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())