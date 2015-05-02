import sys
from PyQt4 import QtCore, QtGui

from basic_ui import Ui_Dialog
from logo import *


class MyForm(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        QtCore.QObject.connect(self.ui.pushButton, QtCore.SIGNAL("clicked()"), self.setName)

    def setName(self):
        # TODO Get branch choice from GUI
        # Only items fitting to branch in corresponding directory
        branches = FolderFinder("./branches").getAllFolderNames()
        print(branches)

        branch = branch_choice
        palettes_string = "./branches/" + branch + "/palettes"
        primitives_string = "./branches/" + branch + "/primitives"
        symbols_string = "./branches/" + branch + "/symbols"
        templates_string = "./branches/" + branch + "/templates"
        fonts_string = "./branches/" + branch + "/fonts"

        user_input = self.ui.lineEdit.text()
        dirColors = FileFinder(palettes_string, "xml")
        dirShapes = FileFinder(primitives_string, "svg")
        dirSymbols = FileFinder(symbols_string, "svg")
        dirTemplates = FileFinder(templates_string, "xml")
        dirFonts = FileFinder(fonts_string, "xml")

        colorPalette1 = ColorPalette(dirColors.getRandomFile())
        shape01 = ShapePrimitive(dirShapes.getRandomFile())
        symbol01 = ShapeSymbol(dirSymbols.getRandomFile())
        font01 = ShapeText(dirFonts.getRandomFile())

        logo_text = str(user_input)

        font01.text = logo_text

        logo = LogoTemplate(dirTemplates.getRandomFile(), shape01, symbol01, font01, colorPalette1)
        logo.writeFile("logo.svg")
        scene = QtGui.QGraphicsScene()

        scene.addPixmap(QtGui.QPixmap('logo.svg'))
        self.ui.graphicsView.setScene(scene)
        self.ui.graphicsView.show()


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())
