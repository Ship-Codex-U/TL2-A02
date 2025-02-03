import sys
import os
import re

from module import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.formFields = FormFields()

        self.setupLabels()
        self.show()

    def setupLabels(self):
        for input in self.findChildren(QLineEdit):
            placeholder = input.placeholderText() or "Ingrese texto"
            input.setPlaceholderText("")
            
            # Create floating label
            floatingLabel = QLabel(placeholder, self)
            floatingLabel.setStyleSheet("color: gray; font-size: 12px; width: 200px; height: 40px;")
            floatingLabel.move(input.x() + 5, input.y() - 1)
            floatingLabel.setAttribute(Qt.WidgetAttribute.WA_TransparentForMouseEvents)

            #Create message label
            messageLabel = QLabel("Ingrese la información solicitada", self)
            messageLabel.setStyleSheet("color: gray; font-size: 10px; width: 200px; height: 40px;")
            messageLabel.move(input.x() + 5, input.y() + 30)

            #Create animation
            floatingLabelAnimation = QPropertyAnimation(floatingLabel, b"pos")
            floatingLabelAnimation.setDuration(40)

            # Store labels and animations
            field = Field(input, floatingLabel, messageLabel, floatingLabelAnimation)
            self.formFields.addField(field)

            input.focusInEvent = lambda event, w=field: self.onFocusIn(event, w)
            input.focusOutEvent = lambda event, w=field: self.onFocusOut(event, w)

    def onFocusIn(self, event, field: Field):
        input = field.input

        self.animateLabel(field.animationLabel, field.labelInfo, input.x() + 5, input.y() - 20)
        QLineEdit.focusInEvent(input, event)

    def onFocusOut(self, event, field: Field):
        input = field.input
        animation = field.animationLabel
        labelInfo = field.labelInfo
        labelMessage = field.labelMessage

        if not input.text():
            self.changeColorLabel(labelMessage, "gray")
            self.changeTextLabel(labelMessage, "Ingrese la información solicitada")
            self.animateLabel(animation, labelInfo, input.x() + 5, input.y() - 1)

        else:
            if input.objectName() == "inputIPv4":
                self.validateIPv4(input.text(), labelMessage)

        QLineEdit.focusOutEvent(input, event)

    def animateLabel(self, animation: QPropertyAnimation, labelInfo: QLabel, x, y):
        animation.setStartValue(labelInfo.pos())
        animation.setEndValue(QPoint(x, y))
        animation.start()    

    def changeColorLabel(self, label: QLabel, color: str):
        label.setStyleSheet(f"color: {color}; font-size: 10px; width: 200px; height: 40px;")

    def changeTextLabel(self, label: QLabel, text: str):
        label.setText(text)        

    def mousePressEvent(self, event):
        for input in self.formFields.getInputs():
            input.clearFocus()

        super().mousePressEvent(event)


    # Metodos para validar campos

    def validateIPv4(self, ip: str, messageLabel: QLabel):
        if re.search("^((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|25[0-5]|2[0-4]\d|[01]?\d\d?)$", ip):
            self.changeColorLabel(messageLabel, "green")
            self.changeTextLabel(messageLabel, "Dirección IP válida")
        else:
            self.changeColorLabel(messageLabel, "red")
            self.changeTextLabel(messageLabel, "Dirección IP NO valida")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
