from PyQt5 import QtCore, QtGui, QtWidgets
from test1gui import Ui_myfirstgui

class MyFirstGuiProgram(Ui_myfirstgui):
    def __init__(self, dialog):
        Ui_myfirstgui.__init__(self)
        self.setupUi(dialog)

        # Connect "add" button with a custom function (addInputTextToListbox)
        self.addBtn.clicked.connect(self.addInputTextToListbox)

    def addInputTextToListbox(self):
        txt = self.myTextInput.text()
        self.listWidget.addItem(txt)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    dialog = QtWidgets.QDialog()

    prog = MyFirstGuiProgram(dialog)

    dialog.show()
    sys.exit(app.exec_())
        self.perform_scan_button.clicked.connect(self.perform_scan)
    def perform_scan(self):
        inital_wavelength = int(self.initial_wavelength.toPlainText())
        final_wavelength = int(self.final_wavelength.toPlainText())
        ##result_graph =  #perform scan method
        ##self.result.setText(result_graph)
