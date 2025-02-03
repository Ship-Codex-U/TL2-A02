from field import Field

class FormFields():
    def __init__(self):
        self.fields = []

    def getFields(self):
        return self.fields
    
    def setFields(self, fields):
        self.fields = fields

    def addField(self, field: Field):
        self.fields.append(field)
    
    def getField(self, index: int):
        return self.fields[index]
    
    def setField(self, index: int, field: Field):
        self.fields[index] = field

    def searchFieldName(self, name: str):
        for field in self.fields:
            if field.getInput().objectName() == name:
                return field
        return None
    
    def searchFieldByLabelName(self, name: str):
        for field in self.fields:
            if field.getLabelInfo().objectName() == name:
                return field
        return None
    
    def searchFieldByMessageName(self, name: str):
        for field in self.fields:
            if field.getLabelMessage().objectName() == name:
                return field
        return None

    def setFieldByFieldName(self, name: str, field: Field):
        for i in range(len(self.fields)):
            if self.fields[i].getInput().objectName() == name:
                self.fields[i] = field
                return True
        return False
    
    def setFieldByLabelName(self, name: str, field: Field):
        for i in range(len(self.fields)):
            if self.fields[i].getLabelInfo().objectName() == name:
                self.fields[i] = field
                return True
        return False
    
    def setFieldByMessageName(self, name: str, field: Field):
        for i in range(len(self.fields)):
            if self.fields[i].getLabelMessage().objectName() == name:
                self.fields[i] = field
                return True
        return False
