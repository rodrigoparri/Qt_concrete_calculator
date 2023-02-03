import sys
from PySide6 import QtWidgets

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
layout = QtWidgets.QFormLayout()

# Add form fields to the layout
h_label = QtWidgets.QLabel("h:")
h_edit = QtWidgets.QLineEdit()
h_edit.setPlaceholderText("300")
layout.addRow(h_label, h_edit)

b_label = QtWidgets.QLabel("b:")
b_edit = QtWidgets.QLineEdit()
b_edit.setPlaceholderText("200")
layout.addRow(b_label, b_edit)

# Set the layout for the window
window.setLayout(layout)

# Show the window
window.show()

sys.exit(app.exec_())