import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.uic import *


import database_design

form_class = uic.loadUiType("untitled.ui")[0]                 # Load the UI
class MyWindowClass(QtGui.QMainWindow, form_class):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.pushButton(self.pushButton)  # Bind the event handlers



app = QtGui.QApplication(sys.argv)
myWindow = MyWindowClass(None)
myWindow.show()
app.exec_()


def initializeModel(model):
    model.setTable('GroupNames')
    model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)
    model.select()
    model.setHeaderData(0, QtCore.Qt.Horizontal, "ID")
    model.setHeaderData(1, QtCore.Qt.Horizontal, "First name")
    # model.setHeaderData(2, QtCore.Qt.Horizontal, "Last name")

def createView(title, model):
    view = QtGui.QTableView()
    view.setModel(model)
    view.setWindowTitle(title)
    return view



def addrow(self):
    print(model.rowCount())
    ret = model.insertRows(model.rowCount(), 1)
    # sportsconnection.addNewRow(name='Yusuf',surname='Unlu')
    database_design.addNewRow(id=123, name='denemename', surname='denemsurname')
    # model.submitAll();
    # print(ret)
    # model.itemData(self,)
    model.record(2)


def findrow(i):
    delrow = i.row()


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
    db.setDatabaseName('transport.db')
    model = QtSql.QSqlTableModel()
    delrow = -1
    initializeModel(model)

    view1 = createView("Table Model (View 1)", model)
    view1.clicked.connect(findrow)

    dlg = QtGui.QDialog()
    layout = QtGui.QVBoxLayout()
    layout.addWidget(view1)

    button = QtGui.QPushButton("Add a row")
    button.clicked.connect(addrow)
    layout.addWidget(button)
    dlg.resize(500,500)

    btn1 = QtGui.QPushButton("del a row")
    btn1.clicked.connect(lambda: model.removeRow(view1.currentIndex().row()))
    layout.addWidget(btn1)

    dlg.setLayout(layout)
    dlg.setWindowTitle("Database Demo")
    dlg.show()
    sys.exit(app.exec_())