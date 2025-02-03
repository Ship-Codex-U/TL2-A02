import sys
import os
import re

from module import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.labels = {}
        self.animations = {}
        self.messagesAlert = {}

        self.setupFloatingLabels()

        self.show()

    def setupFloatingLabels(self):
        for widget in self.findChildren(QLineEdit):
            placeholder = widget.placeholderText() or "Ingrese texto"
            widget.setPlaceholderText("")
            label = QLabel(placeholder, self)
            label.setStyleSheet("color: gray; font-size: 12px; width: 200px; height: 40px;")
            label.move(widget.x() + 5, widget.y() - 1)
            label.setAttribute(Qt.WidgetAttribute.WA_TransparentForMouseEvents)

            self.labels[widget] = label
            self.animations[widget] = QPropertyAnimation(label, b"pos")
            self.animations[widget].setDuration(40)

            widget.focusInEvent = lambda event, w=widget: self.onFocusIn(event, w)
            widget.focusOutEvent = lambda event, w=widget: self.onFocusOut(event, w)

    def onFocusIn(self, event, widget: QLineEdit):
        self.animateLabel(widget, widget.x() + 5, widget.y() - 20)
        QLineEdit.focusInEvent(widget, event)

    def onFocusOut(self, event, widget: QLineEdit):
        if not widget.text():
            self.animateLabel(widget, widget.x() + 5, widget.y() - 1)

        else:
            if widget.objectName() == "inputIPv4":
                self.validateIPv4(widget.text(), widget)

        QLineEdit.focusOutEvent(widget, event)

    def animateLabel(self, widget: QLineEdit, x, y):
        label = self.labels.get(widget)
        if label:
            animation = self.animations.get(widget)
            animation.setStartValue(label.pos())
            animation.setEndValue(QPoint(x, y))
            animation.start()    

    def changeColorLabel(self, widget: QLineEdit, color: str):
        label = self.labels.get(widget)
        if label:
            label.setStyleSheet(f"color: {color}; font-size: 12px; width: 200px; height: 40px;")

    def changeTextLabel(self, widget: QLineEdit, text: str):
        label = self.labels.get(widget)
        if label:
            label.setText(text)        

    def mousePressEvent(self, event):
        for widget in self.labels.keys():
            widget.clearFocus()
        super().mousePressEvent(event)


    # Metodos para validar campos

    def validateIPv4(self, ip: str, widget: QLineEdit):
        if re.search("^((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|25[0-5]|2[0-4]\d|[01]?\d\d?)$", ip):
            self.changeColorLabel(widget, "green")
            self.changeTextLabel(widget, "Dirección IP válida")
        else:
            self.changeColorLabel(widget, "red")
            self.changeTextLabel(widget, "Dirección IP NO valida")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
