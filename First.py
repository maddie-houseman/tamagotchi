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
        self.hunger = 0
        self.strength = 10
        self.last_interaction_time = time.time()

def update(self):
        current_time = time.time()
        time_elapsed = current_time - self.last_interaction_time

        # Decrease health, happiness, and hygiene over time
        self.health -= time_elapsed * 0.01  # Health decreases slightly over time
        self.happiness -= time_elapsed * 0.02
        self.hygiene -= time_elapsed * 0.03
        
        # Aging the Tamagotchi over time (e.g., 1 unit per hour)
        self.age += time_elapsed / 3600

        # Update the last interaction time
        self.last_interaction_time = current_time

def feed(self, food):
        self.update()
        if food == 'healthy':
            self.health += 5
            self.weight += 1
        elif food == 'junk':
            self.happiness += 10
            self.weight += 2
            self.health -= 5
        self.check_limits()

def wash(self):
        self.update()
        self.hygiene = 100
        self.check_limits()

def play(self):
        self.update()
        self.happiness += 10
        self.hygiene -= 10
        self.check_limits()

def sleep(self):
        self.update()
        self.health += 10  # Sleeping improves health
        self.check_limits()

def doctor(self):
     self.update()
     self.health = 100
     self.check_limits()

def check_limits(self):
        if self.health > 100:
            self.health = 100
        elif self.health < 0:
            self.health = 0
        
        if self.happiness > 100:
            self.happiness = 100
        elif self.happiness < 0:
            self.happiness = 0
        
        if self.hygiene > 100:
            self.hygiene = 100
        elif self.hygiene < 0:
            self.hygiene = 0

import json

def save_state(self):
    state = {
        'name': self.name,
        'health': self.health,
        'happiness': self.happiness,
        'hygiene': self.hygiene,
        'age': self.age,
        'weight': self.weight,
        'intelligence': self
    }