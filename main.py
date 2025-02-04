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
            floatingLabel.setFixedWidth(200)
            floatingLabel.setAttribute(Qt.WidgetAttribute.WA_TransparentForMouseEvents)

            #Create message label
            messageLabel = QLabel("Ingrese la información solicitada", self)
            messageLabel.setStyleSheet("color: gray; font-size: 10px; width: 200px; height: 40px;")
            messageLabel.setFixedWidth(200)
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
            if input.objectName() == "inputContrasenia":
                self.validatePassword(input.text(), labelMessage)

            if input.objectName() == "inputFechaNacimiento":
                self.validateBirthday(input.text(), labelMessage)
            
            if input.objectName() == "inputRFC":
                self.validateRFC(input.text(), labelMessage)

            if input.objectName() == "inputCURP":
                self.validateCURP(input.text(), labelMessage)
            
            if input.objectName() == "inputTelefono":
                self.validatePhoneNumber(input.text(), labelMessage)

            if input.objectName() == "inputIPv4":
                self.validateIPv4(input.text(), labelMessage)

            elif input.objectName() == "inputEmail":
                self.validateEmail(input.text(), labelMessage)

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

    def validateEmail(self, email: str, messageLabel: QLabel):
        if re.search("^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", email):
            self.changeColorLabel(messageLabel, "green")
            self.changeTextLabel(messageLabel, "Correo electrónico válido")
        else:
            self.changeColorLabel(messageLabel, "red")
            self.changeTextLabel(messageLabel, "Correo electrónico NO válido")
    
    def validatePassword(self, password: str, messageLabel: QLabel):
        if re.search("^.*(?=.{8,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=]).*$", password):
            self.changeColorLabel(messageLabel, "green")
            self.changeTextLabel(messageLabel, "Contraseña válida")
        else:
            self.changeColorLabel(messageLabel, "red")
            self.changeTextLabel(messageLabel, "Contraseña NO válida")

    def validateBirthday(self, birthday: str, messageLabel: QLabel):
        if re.search("^(0[1-9]|1[0-9]|2[0-9]|3[0-1])/(0[1-9]|1[0-2])/[0-9]{4}$", birthday):
            self.changeColorLabel(messageLabel, "green")
            self.changeTextLabel(messageLabel, "Fecha de nacimiento válida")
        else:
            self.changeColorLabel(messageLabel, "red")
            self.changeTextLabel(messageLabel, "Fecha de nacimiento NO válida")
    
    def validateRFC(self, rfc: str, messageLabel: QLabel):
        if re.search("^[A-Z]{4}[0-9]{6}[A-Z0-9]{3}$", rfc):
            self.changeColorLabel(messageLabel, "green")
            self.changeTextLabel(messageLabel, "RFC válido")
        else:
            self.changeColorLabel(messageLabel, "red")
            self.changeTextLabel(messageLabel, "RFC NO válido")
    
    def validateCURP(self, curp: str, messageLabel: QLabel):
        if re.search("^[A-Z]{4}[0-9]{6}[HM]{1}[A-Z]{2}[A-Z]{3}[A-Z0-9]{2}$", curp):
            self.changeColorLabel(messageLabel, "green")
            self.changeTextLabel(messageLabel, "CURP válida")
        else:
            self.changeColorLabel(messageLabel, "red")
            self.changeTextLabel(messageLabel, "CURP NO válida")
        
    def validatePhoneNumber(self, phone: str, messageLabel: QLabel):
        if re.search("^[0-9]{10}$", phone):
            self.changeColorLabel(messageLabel, "green")
            self.changeTextLabel(messageLabel, "Número de teléfono válido")
        else:
            self.changeColorLabel(messageLabel, "red")
            self.changeTextLabel(messageLabel, "Número de teléfono NO válido")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
