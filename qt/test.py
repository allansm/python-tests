import sys
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel

def test():
    global input

    print(input.text())
    input.setText("")

app = QApplication(sys.argv)

window = QWidget()

input = QLineEdit(window)
input.setGeometry(10, 30, 150, 25)

button = QPushButton("click me", window)
button.setGeometry(170, 30, 70, 25);

label = QLabel("Name:", window)
label.setGeometry(10, 10, 50, 15)

button.clicked.connect(test)

window.resize(250, 65)
window.setMaximumSize(250, 60);
window.setWindowTitle("Test");
window.show()

sys.exit(app.exec())
