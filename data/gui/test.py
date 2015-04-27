import sys
from PyQt4 import QtCore, QtGui

from basic_ui import Ui_Dialog


class MyForm(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        QtCore.QObject.connect(self.ui.pushButton,QtCore.SIGNAL("clicked()"), self.setName)

    def setName(self):
        a = self.ui.lineEdit.text
        scene = QtGui.QGraphicsScene()
        scene.addPixmap(QtGui.QPixmap('logo.svg'))
        self.ui.graphicsView.setScene(scene)
        self.ui.graphicsView.show()
        print(a)



if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())
