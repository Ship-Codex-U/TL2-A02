from PySide6.QtCore import *
from PySide6.QtWidgets import *
from .field import Field

class FormFields():
    def __init__(self):
        self.fields = []

    def getFields(self):
        return self.fields

    def getInputs(self):
        inputs = []
        for field in self.fields:
            inputs.append(field.input)
        return inputs
    
    def setFields(self, fields):
        self.fields = fields

    def getField(self, index: int):
        return self.fields[index]

    def addField(self, field: Field):
        self.fields.append(field)
    
    def setField(self, field: Field):
        band = False

        for i, obj in enumerate(self.fields):
            if field == obj:
                self.fields[i] = field
                band = True
                break
        
        if not band:
            self.addField(field)

    def searchFieldByInput(self, input: QLineEdit):
        for field in self.fields:
            if field.input == input:
                return field
        return None
