class TransitStop:
    
    def __init__(self, stop_id, name):
        self.id = stop_id
        self.name = name

    def __str__(self):
        return f"{self.id} - {self.name}"

    def __repr__(self):
        return self.__str__()
    
