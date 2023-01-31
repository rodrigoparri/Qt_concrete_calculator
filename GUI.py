from PySide6 import QtWidgets as QtW



class MainWindow(QtW.QMainWindow):

    form_fields = {
        0:("b (mm): ", "200"),
        1:("h (mm): ", "300"),
        2:("fck (MPa): ", "25"),
        3:("γc: ", "1.5"),
        4:("fyk (MPa): ", "500"),
        5:("γs: ", "1.15"),
        6:("c (mm): ", "30"),
        7:("Md (mkN): ", "300"),
        8:("", ""),
        9:("", "")
    }
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Concrete Calculator")

        #------------------- LAYOUTS----------------------
        boxh_layout = QtW.QHBoxLayout()  # horizontal layout for form and canvas
        form_layout = QtW.QFormLayout()  # form layout for data input

        #--------------------PARENT WIDGET---------------
        central_widget = QtW.QWidget()  # parent widget
        central_widget.setLayout(boxh_layout)  # set widget layout
        self.setCentralWidget(central_widget)  # set widget as central

        #-------------------CHILD WIDGETS------------------
        left_widget = QtW.QWidget()
        left_widget.setLayout(form_layout)
        boxh_layout.addWidget(left_widget)

        right_widget = QtW.QWidget()
        boxh_layout.addWidget(right_widget)

        #-----------------FORM WIDGETS---------------------
        for i in self.form_fields:
            self.addFormRow(form_layout, self.form_fields[i][0], self.form_fields[i][1])

    def addFormRow(self, layout, label_tx, entry_tx):

        label = Label(label_tx)
        entry = Entry(self, entry_tx)
        layout.addRow(label, entry)


class Entry(QtW.QLineEdit):

    def __init__(self, parent, deftext):
        super(Entry, self).__init__(parent, deftext)

        self.setPlaceholderText(deftext)


class Label(QtW.QLabel):

    def __init__(self, text):
        super(Label, self).__init__(text)




if __name__ == "__main__":
    app = QtW.QApplication([])
    mainWindow = MainWindow()
    mainWindow.show()

    app.exec()
    pass