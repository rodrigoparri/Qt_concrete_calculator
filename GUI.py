from PySide6 import QtWidgets as QtW
from PySide6 import QtGui as QtG

from concrete_cross_sections.rect_beams import RectBeam


class RenderArea(QtW.QWidget):
    
    def __init__(self, parent=None):
        super(RenderArea, self).__init__(parent)

        self.setFixedSize(300, 300)
        self.setBackgroundRole(QtG.QPalette.Base)
        self.setAutoFillBackground(True)

        self.pen = QtG.QPen()
        self.antialiased = False

        self.input_values = {
            "b": 200,
            "h": 300,
            "As1": 0,
            "As2": 0,
            "c": 0
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

            # window dimensions
            width = self.width()
            height = self.height()

            # beam dimensions
            b = self.input_values.get("b", 0)
            h = self.input_values.get("h", 0)
            c = self.input_values.get("c", 0)

            # reinforcement area
            As1 = self.input_values.get("As1", 0)
            As2 = self.input_values.get("As2", 0)

            # scale coefficient
            alpha = 250 / max(b, h)

            b_ = b * alpha
            h_= h * alpha
            c_ = c * alpha
            As1_ = As1 * alpha
            As2_ = As2 * alpha

            # top left beam corner
            x = (width - b_) / 2
            y = (height - h_) / 2

            # reinforcement area rectangles
            b_s = b_ - 2 * c_
            hc1 = As1_ / b_s
            hc2 = As2_ / b_s

            # main rectangle
            painter.drawRect(x, y, b_, h_)
            # top reinforcement rectangle
            painter.drawRect(x + c_, y + c_, b_s, hc1)
            # bottom reinforcement rectangle
            painter.drawRect(x + c_, y + h_ - c_, b_s, hc2)


class MainWindow(QtW.QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Concrete Calculator")
        # self.setFixedSize(500,350)
        # self.setSizePolicy()
        #---------------------MAIN WIDGET------------------
        central_widget = QtW.QWidget()
        self.setCentralWidget(central_widget)

        #-----------------PLACE HOLDER---------------------
        self.b_plcholder = "200"
        self.h_plcholder = "300"
        self.fck_plcholder = "25"
        self.yc_plcholder = "1.5"
        self.fyk_plcholder = "500"
        self.ys_plcholder = "1.15"
        self.Md_plcholder = "300"
        self.x_d_plcholder = "0.3"

        #-----------------FORM WIDGETS---------------------
        self.b_entry = QtW.QLineEdit(self)
        self.b_entry.setPlaceholderText(self.b_plcholder)
        self.h_entry = QtW.QLineEdit(self)
        self.h_entry.setPlaceholderText(self.h_plcholder)
        self.expo_combobox = QtW.QComboBox(self)
        self.find_expo_classes()
        # self.expo_combobox.setPlaceholderText(self.expo_plcholder)
        self.fck_entry = QtW.QLineEdit(self)
        self.fck_entry.setPlaceholderText(self.fck_plcholder)
        self.yc_entry = QtW.QLineEdit(self)
        self.yc_entry.setPlaceholderText(self.yc_plcholder)
        self.fyk_entry = QtW.QLineEdit(self)
        self.fyk_entry.setPlaceholderText(self.fyk_plcholder)
        self.ys_entry = QtW.QLineEdit(self)
        self.ys_entry.setPlaceholderText(self.ys_plcholder)
        self.Md_entry = QtW.QLineEdit(self)
        self.Md_entry.setPlaceholderText(self.Md_plcholder)
        self.x_d_entry = QtW.QLineEdit(self)
        self.x_d_entry.setPlaceholderText(self.x_d_plcholder)
        self.defaults_checkbox = QtW.QCheckBox("Set defaults", self)

        self.b_label = QtW.QLabel("b (mm): ")
        self.b_label.setBuddy(self.b_entry)
        self.h_label = QtW.QLabel("h (mm): ")
        self.h_label.setBuddy(self.h_entry)
        self.expo_label = QtW.QLabel("Exposure class: ")
        self.expo_label.setBuddy(self.expo_combobox)
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
        geo_separator.setLineWidth(1)
        geo_separator.setStyleSheet("color: lightgrey;")
        
        mat_separator = QtW.QFrame()
        mat_separator.setFrameShape(QtW.QFrame.HLine)
        mat_separator.setLineWidth(1)
        mat_separator.setStyleSheet("color: lightgrey;")

        adv_separator = QtW.QFrame()
        adv_separator.setFrameShape(QtW.QFrame.HLine)
        adv_separator.setLineWidth(1)
        adv_separator.setStyleSheet("color: lightgrey;")

        #-------------------BUTTONS----------------------
        self.calc_button = QtW.QPushButton("Calculate")
        self.download_button = QtW.QPushButton("Download")

        #--------------------RENDERAREA------------------
        self.render_area = RenderArea()
        self.render_area.set_antialising(True)

        #--------------------CONNECTIONS-----------
        self.calc_button.clicked.connect(self.calculate)
        self.defaults_checkbox.stateChanged.connect(self.set_defaults)

        # ------------------- LAYOUT----------------------
        layout = QtW.QGridLayout()
        layout.setRowStretch(0, 20)
        layout.setColumnStretch(0, 2)
        layout.addWidget(self.b_label, 0, 0)
        layout.addWidget(self.b_entry, 0, 1)
        layout.addWidget(self.h_label, 1, 0)
        layout.addWidget(self.h_entry, 1, 1)
        layout.addWidget(self.expo_label, 2, 0)
        layout.addWidget(self.expo_combobox, 2, 1)
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
        layout.addWidget(self.defaults_checkbox, 12, 0)
        layout.addWidget(self.calc_button, 13, 1)
        layout.addWidget(self.download_button, 13, 2)


        layout.addWidget(self.render_area, 0, 2, 12, 1)

        central_widget.setLayout(layout)

    def calculate(self):
        b = int(self.b_entry.text())
        h = int(self.h_entry.text())
        expo = self.expo_combobox.currentText()
        fck = int(self.fck_entry.text())
        yc = float(self.yc_entry.text())
        fyk = int(self.fyk_entry.text())
        ys = float(self.ys_entry.text())
        Md = float(self.Md_entry.text())
        x_d = float(self.x_d_entry.text())

        beam = RectBeam(b, h, expo, fck, yc, fyk, ys, Md, x_d)
        As = beam.As()

        self.render_area.input_values["b"] = b
        self.render_area.input_values["h"] = h
        self.render_area.input_values["c"] = beam.c
        self.render_area.input_values["As1"] = As[0]
        self.render_area.input_values["As2"] = As[1]

        self.render_area.update()

    def set_defaults(self, state):
        if self.defaults_checkbox.isChecked():
            self.b_entry.setText(self.b_plcholder)
            self.h_entry.setText(self.h_plcholder)
            self.expo_combobox.setCurrentIndex(0)
            self.fck_entry.setText(self.fck_plcholder)
            self.yc_entry.setText(self.yc_plcholder)
            self.fyk_entry.setText(self.fyk_plcholder)
            self.ys_entry.setText(self.ys_plcholder)
            self.Md_entry.setText(self.Md_plcholder)
            self.x_d_entry.setText(self.x_d_plcholder)

        else:
            self.b_entry.setText("")
            self.h_entry.setText("")
            self.expo_combobox.setCurrentIndex(0)
            self.fck_entry.setText("")
            self.yc_entry.setText("")
            self.fyk_entry.setText("")
            self.ys_entry.setText("")
            self.Md_entry.setText("")
            self.x_d_entry.setText("")

    def find_expo_classes(self):

        for expo in RectBeam.c:
            self.expo_combobox.addItem(expo)

if __name__ == "__main__":
    app = QtW.QApplication([])
    mainWindow = MainWindow()
    mainWindow.show()

    app.exec()
    pass