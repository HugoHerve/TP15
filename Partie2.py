from PySide2.QtWidgets import *

class LabeledTextField(QWidget):
    def __init__(self, text):
        QWidget.__init__(self)

        self.setWindowTitle("Configuration")

        layout = QHBoxLayout()
        label = QLabel(text)
        texte = QTextEdit()
        layout.addWidget(label)
        layout.addWidget(texte)
        texte.setMaximumHeight(25)

        self.setLayout(layout)

class ConfigurationDialog(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        layout = QVBoxLayout()
        text1 = LabeledTextField("IP address")
        text2 = LabeledTextField("User")
        text3 = LabeledTextField("Password")

        layout.addWidget(text1)
        layout.addWidget(text2)
        layout.addWidget(text3)
        self.setLayout(layout)



if __name__ == "__main__":
    app = QApplication([])
    win = ConfigurationDialog()
    win.show()
    app.exec_()
