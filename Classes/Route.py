class Route: 
    def __init__(self, source, destination, time):
        self.source = source        
        self.destination = destination   
        self.time = time

    def __str__(self):
        return f"{self.source.id} -> {self.destination.id} ({self.time} min)"

    def __repr__(self):
        return self.__str__()