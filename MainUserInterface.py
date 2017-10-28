import sys
import PyQt4
from PyQt4 import QtGui
from PyQt4 import QtCore
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtSql import *
#from PyQt4 import QtGui

import database_design
import database_value_change


simge ='truck.jpg'
class tabdemo(QTabWidget):
    def __init__(self, parent=None):
        super(tabdemo, self).__init__(parent)
        self.tab1 = QWidget(self)
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.tab4 = QWidget()
        self.tab5 = QWidget()
        self.tab6 = QWidget()

        self.addTab(self.tab1, "Tab 1")
        self.addTab(self.tab2, "Tab 2")
        self.addTab(self.tab3, "Tab 3")
        self.addTab(self.tab4, "Tab 4")
        self.addTab(self.tab5, "Tab 5")
        self.addTab(self.tab6, "Tab 6")
        self.tab1UI()
        self.tab2UI()
        self.tab3UI()
        self.tab4UI()
        self.tab5UI()
        self.tab6UI()

        self.setWindowTitle("Transport Management")
        self.setWindowIcon(QIcon(simge))

    def tab1UI(self):
        layout = QFormLayout()



        layout.addRow("Address", QLineEdit())
        layout.addRow("X", QTableView())
        layout.addWidget(QRadioButton())
        btn = QtGui.QPushButton("Quit")
        btn.resize(100,100)
        btn.clicked.connect(QtCore.QCoreApplication.instance().quit)
        layout.addWidget(btn)


        self.setTabText(0, "Main Window")
        self.tab1.setLayout(layout)

    def tab2UI(self):
        layout = QFormLayout()
        layout.addRow("City", QLineEdit())
        layout.addWidget(QPushButton("Add"))
        layout.addWidget(QTableView())
        layout.addWidget(QPushButton("Delete"))
        self.setTabText(1, "Add New Cities")
        self.tab2.setLayout(layout)

    def tab3UI(self):
        layout = QFormLayout()
        layout.addRow("Company Name",QLineEdit())
        layout.addRow("Company Contact", QLineEdit())
        layout.addRow("Company City",QLineEdit())
        layout.addRow("Company Phone", QLineEdit())
        layout.addWidget(QPushButton("Add"))
        layout.addWidget(QTableView())
        layout.addWidget(QPushButton("Delete"))
        self.setTabText(2, "Add New Companies")
        self.tab3.setLayout(layout)

    def tab4UI(self):
        layout = QFormLayout()
        layout.addRow("Driver Name",QLineEdit())
        layout.addRow("Driver Address", QLineEdit())
        layout.addRow("Driver City",QLineEdit())
        layout.addRow("Driver Phone", QLineEdit())
        layout.addWidget(QPushButton("Add"))
        layout.addWidget(QTableView())
        layout.addWidget(QPushButton("Delete"))
        self.setTabText(3, "Add New Drivers")
        self.tab4.setLayout(layout)

    def tab5UI(self):
        layout = QFormLayout()
        #sex = QHBoxLayout()
        #sex.addWidget(QRadioButton("Male"))
        #sex.addWidget(QRadioButton("Female"))
        layout.addRow("Goods Name",QLineEdit())
        layout.addRow("Goods Features", QLineEdit())
        layout.addWidget(QPushButton("Add"))
        layout.addWidget(QTableView())
        layout.addWidget(QPushButton("Delete"))
        self.setTabText(4, "Add New Goods")
        self.tab5.setLayout(layout)

    def tab6UI(self):
        layout = QFormLayout()
        layout.addRow("Truck Name", QLineEdit())
        layout.addRow("Truck Plate", QLineEdit())
        layout.addRow("Truck Capacity",QLineEdit())
        layout.addRow("Truck Features", QLineEdit())
        layout.addWidget(QPushButton("Add"))
        layout.addWidget(QTableView())
        layout.addWidget(QPushButton("Delete"))
        self.setTabText(5, "Add New Trucks")
        self.tab6.setLayout(layout)

def main():
    app = QApplication(sys.argv)
    w = 900
    h = 600
    ex = tabdemo()
    ex.resize(w, h)
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
