import time

class Tamagotchi:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.happiness = 100
        self.hygiene = 100
        self.age = 0
        self.weight = 5
        self.intelligence = 50
        self.last_interaction_time = time.time()
