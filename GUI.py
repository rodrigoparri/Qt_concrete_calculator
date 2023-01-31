from PySide6 import QtWidgets as QtW
from PySide6 import QtCore as QtC

class MainWindow(QtW.QMainWindow):

    def  __init__(self):
        super().__init__()
        self.setWindowTitle("Concrete Calculator")

        self.widgets(self)

    @classmethod
    def widgets(cls,self):
        cls.h = Entry(self, "h")


class Entry(QtW.QLineEdit):
    
    def __init__(self, parent, text):
        super().__init__(parent, text)

        self.setPlaceholderText(text)

if __name__ == "__main__":
    app = QtW.QApplication([])
    mainWindow = MainWindow()
    mainWindow.show()

    app.exec()
    pass