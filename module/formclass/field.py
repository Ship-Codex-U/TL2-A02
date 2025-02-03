from PySide6.QtCore import *
from PySide6.QtWidgets import *

class Field():
    def __init__(self, input: QLineEdit, labelInfo: QLabel, labelMessage: QLabel, animationLabel: QPropertyAnimation):
        self.__input = input
        self.__labelInfo = labelInfo
        self.__labelMessage = labelMessage
        self.__animationLabel = animationLabel

    @property
    def input(self):
        return self.__input
    
    @input.setter
    def input(self, input):
        self.__input = input

    @property
    def labelInfo(self):
        return self.__labelInfo

    @labelInfo.setter
    def labelInfo(self, labelInfo):
        self.__labelInfo = labelInfo

    @property
    def labelMessage(self):
        return self.__labelMessage

    @labelMessage.setter
    def labelMessage(self, labelMessage):
        self.__labelMessage = labelMessage

    @property
    def animationLabel(self):
        return self.__animationLabel

    @animationLabel.setter
    def animationLabel(self, animationLabel):
        self.__animationLabel = animationLabel

    @property
    def inputName(self):
        return self.__input.objectName()
    
    @property
    def labelInfoName(self):
        return self.__labelInfo.objectName()
    
    @property
    def labelMessageName(self):
        return self.__labelMessage.objectName()