from PySide6 import QtWidgets as QtW
from PySide6 import  QtGui as QtG


class RenderArea(QtW.QWidget):
    
    def __init__(self):
        super(RenderArea, self).__init__()

class MainWindow(QtW.QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Concrete Calculator")
        #---------------------MAIN WIDGET------------------
        central_widget = QtW.QWidget()
        self.setCentralWidget(central_widget)

        #-----------------FORM WIDGETS---------------------

        self.b_entry = QtW.QLineEdit(self)
        self.b_entry.setPlaceholderText("200")
        self.h_entry = QtW.QLineEdit(self)
        self.h_entry.setPlaceholderText("300")
        self.fck_entry = QtW.QLineEdit(self)
        self.fck_entry.setPlaceholderText("25")
        self.yc_entry = QtW.QLineEdit(self)
        self.yc_entry.setPlaceholderText("1.5")
        self.fyk_entry = QtW.QLineEdit(self)
        self.fyk_entry.setPlaceholderText("500")
        self.ys_entry = QtW.QLineEdit(self)
        self.ys_entry.setPlaceholderText("1.15")
        self.c_entry = QtW.QLineEdit(self)
        self.c_entry.setPlaceholderText("30")
        self.Md_entry = QtW.QLineEdit(self)
        self.Md_entry.setPlaceholderText("300")

        self.b_label = QtW.QLabel("b (mm): ")
        self.b_label.setBuddy(self.b_entry)
        self.h_label = QtW.QLabel("h (mm): ")
        self.h_label.setBuddy(self.h_entry)
        self.fck_label = QtW.QLabel("fck (MPa): ")
        self.fck_label.setBuddy(self.fck_entry)
        self.yc_label = QtW.QLabel("γc: ")
        self.yc_label.setBuddy(self.yc_entry)
        self.fyk_label = QtW.QLabel("fyk (MPa): ")
        self.fyk_label.setBuddy(self.fyk_entry)
        self.ys_label = QtW.QLabel("γs: ")
        self.ys_label.setBuddy(self.ys_entry)
        self.c_label = QtW.QLabel("c (mm): ")
        self.c_label.setBuddy(self.c_entry)
        self.Md_label = QtW.QLabel("Md (mkN): ")
        self.Md_label.setBuddy(self.Md_entry)

        # ------------------- LAYOUT----------------------
        layout = QtW.QGridLayout()
        layout.setRowStretch(0, 10)
        layout.setColumnStretch(0, 2)
        layout.addWidget(self.b_label, 0, 0)
        layout.addWidget(self.b_entry, 0, 1)
        layout.addWidget(self.h_label, 1, 0)
        layout.addWidget(self.h_label, 1, 1)
        layout.addWidget(self.fck_label, 2, 0)
        layout.addWidget(self.fck_entry, 2, 1)
        layout.addWidget(self.yc_label, 3, 0)
        layout.addWidget(self.yc_entry, 3, 1)
        layout.addWidget(self.fyk_label, 4, 0)
        layout.addWidget(self.fyk_entry, 4, 1)
        layout.addWidget(self.ys_label, 5, 0)
        layout.addWidget(self.ys_entry, 5, 1)
        layout.addWidget(self.c_label, 6, 0)
        layout.addWidget(self.c_entry, 6, 1)
        layout.addWidget(self.Md_label, 7, 0)
        layout.addWidget(self.Md_entry, 7, 1)

        central_widget.setLayout(layout)


        # for i in self.form_fields:
        #     entry = QtW.QLineEdit()
        #     entry.setPlaceholderText(self.form_fields[i][1])
        #
        #     label = QtW.QLabel(self.form_fields[i][0])
        #     label.setBuddy(entry)
        #
        #     layout.addWidget(label, i, 0)
        #     layout.addWidget(entry, i, 1)

    def addFormRow(self, layout, label_tx, entry_tx):

        label = QtW.QLabel(label_tx)
        entry = QtW.QLineEdit(self)
        entry.setPlaceholderText(entry_tx)
        layout.addRow(label, entry)






if __name__ == "__main__":
    app = QtW.QApplication([])
    mainWindow = MainWindow()
    mainWindow.show()

    app.exec()
    pass