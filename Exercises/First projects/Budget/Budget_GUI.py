# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Budget_GUI_file.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets




class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1173, 800)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setMaximumSize(QtCore.QSize(100000, 100000))
        self.tabWidget.setSizeIncrement(QtCore.QSize(1, 1))
        self.tabWidget.setBaseSize(QtCore.QSize(1200, 900))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_6 = QtWidgets.QLabel(self.tab)
        self.label_6.setTabletTracking(False)
        self.label_6.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_6.setTextFormat(QtCore.Qt.AutoText)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setWordWrap(False)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_6.addWidget(self.label_6)
        self.diverse_table = QtWidgets.QTableWidget(self.tab)
        self.diverse_table.setRowCount(10)
        self.diverse_table.setColumnCount(2)
        self.diverse_table.setObjectName("diverse_table")
        self.verticalLayout_6.addWidget(self.diverse_table)
        self.gridLayout_2.addLayout(self.verticalLayout_6, 0, 4, 1, 1)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setTabletTracking(False)
        self.label_5.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_5.setTextFormat(QtCore.Qt.AutoText)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setWordWrap(False)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_5.addWidget(self.label_5)
        self.transport_table = QtWidgets.QTableWidget(self.tab)
        self.transport_table.setRowCount(10)
        self.transport_table.setColumnCount(2)
        self.transport_table.setObjectName("transport_table")
        self.verticalLayout_5.addWidget(self.transport_table)
        self.gridLayout_2.addLayout(self.verticalLayout_5, 0, 2, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setTabletTracking(False)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.bolig_table = QtWidgets.QTableWidget(self.tab)
        self.bolig_table.setRowCount(10)
        self.bolig_table.setColumnCount(2)
        self.bolig_table.setObjectName("bolig_table")
        self.verticalLayout.addWidget(self.bolig_table)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setTabletTracking(False)
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setTextFormat(QtCore.Qt.AutoText)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setWordWrap(False)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.mad_table = QtWidgets.QTableWidget(self.tab)
        self.mad_table.setRowCount(10)
        self.mad_table.setColumnCount(2)
        self.mad_table.setObjectName("mad_table")
        self.verticalLayout_2.addWidget(self.mad_table)
        self.gridLayout_2.addLayout(self.verticalLayout_2, 0, 1, 1, 1)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setTabletTracking(False)
        self.label_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_4.setTextFormat(QtCore.Qt.AutoText)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setWordWrap(False)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_4.addWidget(self.label_4)
        self.oevrige_faste_table = QtWidgets.QTableWidget(self.tab)
        self.oevrige_faste_table.setRowCount(10)
        self.oevrige_faste_table.setColumnCount(2)
        self.oevrige_faste_table.setObjectName("oevrige_faste_table")
        self.verticalLayout_4.addWidget(self.oevrige_faste_table)
        self.gridLayout_2.addLayout(self.verticalLayout_4, 0, 3, 1, 1)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_7 = QtWidgets.QLabel(self.tab)
        self.label_7.setTabletTracking(False)
        self.label_7.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_7.setTextFormat(QtCore.Qt.AutoText)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setWordWrap(False)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_7.addWidget(self.label_7)
        self.opsparing_table = QtWidgets.QTableWidget(self.tab)
        self.opsparing_table.setRowCount(10)
        self.opsparing_table.setColumnCount(2)
        self.opsparing_table.setObjectName("opsparing_table")
        self.verticalLayout_7.addWidget(self.opsparing_table)
        self.gridLayout_2.addLayout(self.verticalLayout_7, 0, 5, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setTabletTracking(False)
        self.label_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_3.setTextFormat(QtCore.Qt.AutoText)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setWordWrap(False)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.gaeld_table = QtWidgets.QTableWidget(self.tab)
        self.gaeld_table.setRowCount(10)
        self.gaeld_table.setColumnCount(2)
        self.gaeld_table.setObjectName("gaeld_table")
        self.verticalLayout_3.addWidget(self.gaeld_table)
        self.gridLayout_2.addLayout(self.verticalLayout_3, 0, 6, 1, 1)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.gridLayout_4.setHorizontalSpacing(0)
        self.gridLayout_4.setVerticalSpacing(7)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.button_diverse = QtWidgets.QPushButton(self.tab)
        self.button_diverse.setObjectName("button_diverse")
        self.gridLayout_4.addWidget(self.button_diverse, 5, 0, 1, 1)
        self.button_opsparing = QtWidgets.QPushButton(self.tab)
        self.button_opsparing.setObjectName("button_opsparing")
        self.gridLayout_4.addWidget(self.button_opsparing, 6, 0, 1, 1)
        self.button_bolig = QtWidgets.QPushButton(self.tab)
        self.button_bolig.setObjectName("button_bolig")
        self.gridLayout_4.addWidget(self.button_bolig, 1, 0, 1, 1)
        self.button_mad = QtWidgets.QPushButton(self.tab)
        self.button_mad.setObjectName("button_mad")
        self.gridLayout_4.addWidget(self.button_mad, 2, 0, 1, 1)
        self.button_transport = QtWidgets.QPushButton(self.tab)
        self.button_transport.setObjectName("button_transport")
        self.gridLayout_4.addWidget(self.button_transport, 3, 0, 1, 1)
        self.button_faste = QtWidgets.QPushButton(self.tab)
        self.button_faste.setObjectName("button_faste")
        self.gridLayout_4.addWidget(self.button_faste, 4, 0, 1, 1)
        self.button_gaeld = QtWidgets.QPushButton(self.tab)
        self.button_gaeld.setObjectName("button_gaeld")
        self.gridLayout_4.addWidget(self.button_gaeld, 7, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.tab)
        self.lineEdit.setText("")
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_4.addWidget(self.lineEdit, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.gridLayout_2.addLayout(self.gridLayout_4, 1, 1, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_8 = QtWidgets.QLabel(self.tab)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout_3.addWidget(self.label_8, 0, 0, 1, 1)
        self.ukategoriseret_table = QtWidgets.QTableWidget(self.tab)
        self.ukategoriseret_table.setLineWidth(1)
        self.ukategoriseret_table.setAutoScroll(True)
        self.ukategoriseret_table.setShowGrid(True)
        self.ukategoriseret_table.setRowCount(10)
        self.ukategoriseret_table.setColumnCount(2)
        self.ukategoriseret_table.setObjectName("ukategoriseret_table")

        item = QtWidgets.QTableWidgetItem()
        self.ukategoriseret_table.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.ukategoriseret_table.setItem(0, 1, item)
        self.ukategoriseret_table.horizontalHeader().setVisible(True)
        self.ukategoriseret_table.horizontalHeader().setCascadingSectionResizes(False)
        self.ukategoriseret_table.horizontalHeader().setDefaultSectionSize(55)
        self.ukategoriseret_table.horizontalHeader().setMinimumSectionSize(25)
        self.ukategoriseret_table.horizontalHeader().setSortIndicatorShown(False)
        self.ukategoriseret_table.horizontalHeader().setStretchLastSection(True)
        self.ukategoriseret_table.verticalHeader().setVisible(True)
        self.ukategoriseret_table.verticalHeader().setCascadingSectionResizes(False)
        self.ukategoriseret_table.verticalHeader().setDefaultSectionSize(27)
        self.ukategoriseret_table.verticalHeader().setMinimumSectionSize(0)
        self.ukategoriseret_table.verticalHeader().setStretchLastSection(False)
        self.gridLayout_3.addWidget(self.ukategoriseret_table, 1, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_3, 1, 5, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout_8.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1173, 26))
        self.menubar.setObjectName("menubar")
        self.menuOversigt = QtWidgets.QMenu(self.menubar)
        self.menuOversigt.setObjectName("menuOversigt")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuOversigt.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        #self.button_bolig.released.connect(self.lineEdit.clear)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.bolig_table, self.mad_table)
        MainWindow.setTabOrder(self.mad_table, self.transport_table)
        MainWindow.setTabOrder(self.transport_table, self.oevrige_faste_table)
        MainWindow.setTabOrder(self.oevrige_faste_table, self.diverse_table)
        MainWindow.setTabOrder(self.diverse_table, self.opsparing_table)
        MainWindow.setTabOrder(self.opsparing_table, self.gaeld_table)
        MainWindow.setTabOrder(self.gaeld_table, self.ukategoriseret_table)
        MainWindow.setTabOrder(self.ukategoriseret_table, self.button_bolig)
        MainWindow.setTabOrder(self.button_bolig, self.button_mad)
        MainWindow.setTabOrder(self.button_mad, self.button_transport)
        MainWindow.setTabOrder(self.button_transport, self.button_faste)
        MainWindow.setTabOrder(self.button_faste, self.button_diverse)
        MainWindow.setTabOrder(self.button_diverse, self.button_opsparing)
        MainWindow.setTabOrder(self.button_opsparing, self.button_gaeld)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_6.setText(_translate("MainWindow", "Diverse"))
        self.label_5.setText(_translate("MainWindow", "Transport"))
        self.label.setText(_translate("MainWindow", "Bolig"))
        self.label_2.setText(_translate("MainWindow", "Mad"))
        self.label_4.setText(_translate("MainWindow", "Øvrige faste"))
        self.label_7.setText(_translate("MainWindow", "Opsparing"))
        self.label_3.setText(_translate("MainWindow", "Gæld"))
        self.button_diverse.setText(_translate("MainWindow", "Diverse"))
        self.button_opsparing.setText(_translate("MainWindow", "Opsparing"))
        self.button_bolig.setText(_translate("MainWindow", "Bolig"))
        self.button_mad.setText(_translate("MainWindow", "Mad"))
        self.button_transport.setText(_translate("MainWindow", "Transport"))
        self.button_faste.setText(_translate("MainWindow", "Øvrige faste"))
        self.button_gaeld.setText(_translate("MainWindow", "Gæld"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Input"))
        self.label_8.setText(_translate("MainWindow", "Endnu ikke kategoriseret"))
        self.ukategoriseret_table.setSortingEnabled(False)
        __sortingEnabled = self.ukategoriseret_table.isSortingEnabled()
        self.ukategoriseret_table.setSortingEnabled(False)
        item = self.ukategoriseret_table.item(0, 0)
        item.setText(_translate("MainWindow", "Foetex"))
        item = self.ukategoriseret_table.item(0, 1)
        item.setText(_translate("MainWindow", "201 kr."))
        self.ukategoriseret_table.setSortingEnabled(__sortingEnabled)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Oversigt"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Detaljeret oversigt"))
        self.menuOversigt.setTitle(_translate("MainWindow", "Oversigt"))





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
