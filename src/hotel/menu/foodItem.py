class FoodItem:
    _name = ""
    _description = ""
    def __init__(self, name = "Name", description = "...."):
        self._name = name
        self._description = description

    def __str__(self):
        return self._name + ": " + self._description
    
    def __repr__(self) -> str:
        return f"name: {self._name}, description: {self._description}"

    def getName(self):
        return self._name
    
    def setName(self, name):
        self._name = name
    
    def getDescription(self):   
        return self._description
    
    def setDescription(self, description):
        self._description = description

    # static method
    def create():
        name =  input("Enter food item name: ")
        description = input("Enter food item description: ")
        return name, description
