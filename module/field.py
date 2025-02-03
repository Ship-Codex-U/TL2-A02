from PySide6.QtWidgets import *

class Field():
    def __init__(self):
        self.input
        self.labelInfo
        self.labelMessage
        self.animationLabel

    def getInput(self):
        return self.input
    
    def setInput(self, input):
        self.input = input

    def getLabelInfo(self):
        return self.labelInfo
    
    def setLabelInfo(self, labelInfo): 
        self.labelInfo = labelInfo

    def getLabelMessage(self):
        return self.labelMessage
    
    def setLabelMessage(self, labelMessage):
        self.labelMessage = labelMessage
    
    def getAnimationLabel(self):
        return self.animationLabel
    
    def setAnimationLabel(self, animationLabel):
        self.animationLabel = animationLabel

    