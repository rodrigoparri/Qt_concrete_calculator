from PySide6 import QtWidgets as QtW
from PySide6 import QtGui as QtG


class RenderArea(QtW.QWidget):
    
    def __init__(self, parent = None):
        super(RenderArea, self).__init__(parent)

        self.setMinimumSize(200, 200)
        # self.setMaximumSize(400, 600)
        self.setBackgroundRole(QtG.QPalette.Base)
        self.setAutoFillBackground(True)

        self.pen = QtG.QPen()
        self.antialiased = False

        self.input_values = {
            "b": 100,
            "h": 150
        }

    def set_pen(self, pen):
        self.pen = pen
        self.update()

    def set_antialising(self, antialiased):
        self.antialiased = antialiased
        self.update()

    def set_input_values(self, values: dict):
        self.input_values = values

    def paintEvent(self, event) -> None:  # doesn´t return anything

        with QtG.QPainter(self) as painter:
            painter.setPen(self.pen)
            if self.antialiased:
                painter.setRenderHint(QtG.QPainter.Antialiasing)

            width = self.width()
            height = self.height()

            b = self.input_values.get("b", 0)
            h = self.input_values.get("h", 0)

            x = (width - b) / 2
            y = (height - h) / 2

            As1 = self.input_values.get("As1", 0)
            As2 = self.input_values.get("As2", 0)

            painter.drawRect(x, y, b, h)

class MainWindow(QtW.QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Concrete Calculator")
        self.setMaximumSize(400,300)
        #---------------------MAIN WIDGET------------------
        central_widget = QtW.QWidget()
        self.setCentralWidget(central_widget)

        #-----------------FORM WIDGETS---------------------

        self.b_entry = QtW.QLineEdit(self)
        self.b_entry.setPlaceholderText("200")
        self.h_entry = QtW.QLineEdit(self)
        self.h_entry.setPlaceholderText("100")
        self.c_entry = QtW.QLineEdit(self)
        self.c_entry.setPlaceholderText("30")
        self.fck_entry = QtW.QLineEdit(self)
        self.fck_entry.setPlaceholderText("25")
        self.yc_entry = QtW.QLineEdit(self)
        self.yc_entry.setPlaceholderText("1.5")
        self.fyk_entry = QtW.QLineEdit(self)
        self.fyk_entry.setPlaceholderText("500")
        self.ys_entry = QtW.QLineEdit(self)
        self.ys_entry.setPlaceholderText("1.15")
        self.Md_entry = QtW.QLineEdit(self)
        self.Md_entry.setPlaceholderText("300")
        self.x_d_entry = QtW.QLineEdit(self)
        self.x_d_entry.setPlaceholderText("x/d")

        self.b_label = QtW.QLabel("b (mm): ")
        self.b_label.setBuddy(self.b_entry)
        self.h_label = QtW.QLabel("h (mm): ")
        self.h_label.setBuddy(self.h_entry)
        self.c_label = QtW.QLabel("c (mm): ")
        self.c_label.setBuddy(self.c_entry)
        self.fck_label = QtW.QLabel("fck (MPa): ")
        self.fck_label.setBuddy(self.fck_entry)
        self.yc_label = QtW.QLabel("γc: ")
        self.yc_label.setBuddy(self.yc_entry)
        self.fyk_label = QtW.QLabel("fyk (MPa): ")
        self.fyk_label.setBuddy(self.fyk_entry)
        self.ys_label = QtW.QLabel("γs: ")
        self.ys_label.setBuddy(self.ys_entry)
        self.Md_label = QtW.QLabel("Md (mkN): ")
        self.Md_label.setBuddy(self.Md_entry)
        self.x_d_label = QtW.QLabel("x/d")
        self.x_d_label.setBuddy(self.x_d_entry)

        geo_separator = QtW.QFrame()
        geo_separator.setFrameShape(QtW.QFrame.HLine)
        mat_separator = QtW.QFrame()
        mat_separator.setFrameShape(QtW.QFrame.HLine)
        adv_separator = QtW.QFrame()
        adv_separator.setFrameShape(QtW.QFrame.HLine)

        #-------------------BUTTONS----------------------
        self.calc_button = QtW.QPushButton("Calculate")
        self.download_button = QtW.QPushButton("Download")

        #--------------------RENDERAREA------------------
        self.render_area = RenderArea()
        self.render_area.set_antialising(True)

        # ------------------- LAYOUT----------------------
        layout = QtW.QGridLayout()
        layout.setRowStretch(0, 10)
        layout.setColumnStretch(0, 2)
        layout.addWidget(self.b_label, 0, 0)
        layout.addWidget(self.b_entry, 0, 1)
        layout.addWidget(self.h_label, 1, 0)
        layout.addWidget(self.h_entry, 1, 1)
        layout.addWidget(self.c_label, 2, 0)
        layout.addWidget(self.c_entry, 2, 1)
        layout.addWidget(geo_separator, 3, 0, 1, 2)
        layout.addWidget(self.fck_label, 4, 0)
        layout.addWidget(self.fck_entry, 4, 1)
        layout.addWidget(self.yc_label, 5, 0)
        layout.addWidget(self.yc_entry, 5, 1)
        layout.addWidget(self.fyk_label, 6, 0)
        layout.addWidget(self.fyk_entry, 6, 1)
        layout.addWidget(self.ys_label, 7, 0)
        layout.addWidget(self.ys_entry, 7, 1)
        layout.addWidget(mat_separator, 8, 0, 1, 2)
        layout.addWidget(self.Md_label, 9, 0)
        layout.addWidget(self.Md_entry, 9, 1)
        layout.addWidget(adv_separator, 10, 0, 1, 2)
        layout.addWidget(self.x_d_label, 11,0)
        layout.addWidget(self.x_d_entry, 11, 1)
        layout.addWidget(self.calc_button, 12, 1)
        layout.addWidget(self.download_button, 12, 2)

        layout.addWidget(self.render_area, 0, 2, 12, 1)

        central_widget.setLayout(layout)

if __name__ == "__main__":
    app = QtW.QApplication([])
    mainWindow = MainWindow()
    mainWindow.show()

    app.exec()
    pass