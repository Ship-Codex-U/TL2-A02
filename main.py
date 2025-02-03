import sys
import os

from module import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.labels = {}
        self.animations = {}

        self.setupFloatingLabels()

        self.show()

    def setupFloatingLabels(self):
        """ Configura etiquetas flotantes y eventos para todos los QLineEdit """
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

    def onFocusIn(self, event, widget):
        """ Mueve la etiqueta arriba cuando el campo recibe foco """
        self.animateLabel(widget, widget.x() + 5, widget.y() - 20)
        QLineEdit.focusInEvent(widget, event)

    def onFocusOut(self, event, widget):
        """ Baja la etiqueta solo si el campo está vacío """
        if not widget.text():
            self.animateLabel(widget, widget.x() + 5, widget.y() - 1)
        QLineEdit.focusOutEvent(widget, event)

    def animateLabel(self, widget, x, y):
        """ Aplica animación a la etiqueta flotante correspondiente al campo """
        label = self.labels.get(widget)
        if label:
            animation = self.animations.get(widget)
            animation.setStartValue(label.pos())
            animation.setEndValue(QPoint(x, y))
            animation.start()            

    def mousePressEvent(self, event):
        """ Hace que cualquier campo pierda el foco al hacer clic fuera de ellos """
        for widget in self.labels.keys():
            widget.clearFocus()
        super().mousePressEvent(event)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
