from PySide2.QtWidgets import *

class SQLClientWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.setWindowTitle("SQL CLient")
        self.setMaximumSize(600, 600)

        notificationpnel = QTextEdit()
        buttonspanel = ButtonsPanel()
        resultTable = QTableWidget(5, 3)
        resultTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        layout = QVBoxLayout()
        layout.addWidget(buttonspanel)
        layout.addWidget(notificationpnel)
        layout.addWidget(resultTable)
        self.setLayout(layout)


class ButtonsPanel(QWidget):
        def __init__(self):
            QWidget.__init__(self)

            layout = QHBoxLayout()
            button1 = QPushButton("Configure")
            button2 = QPushButton("Connect")
            button3 = QPushButton("Disconnect")
            layout.addWidget(button1)
            layout.addWidget(button2)
            layout.addWidget(button3)
            self.setLayout(layout)



class LabeledTextField(QWidget):
    def __init__(self, text):
        QWidget.__init__(self)



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
        self.setWindowTitle("Configuration")
        layout.addWidget(text1)
        layout.addWidget(text2)
        layout.addWidget(text3)
        self.setLayout(layout)



if __name__ == "__main__":
    app = QApplication([])
    win = SQLClientWindow()
    won = ConfigurationDialog()
    win.show()
    won.show()
    app.exec_()


