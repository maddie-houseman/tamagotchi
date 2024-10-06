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
        self.happiness -= time_elapsed * 0.01
        self.hygiene -= time_elapsed * 0.03
        
        # Aging the Tamagotchi over time (e.g., 1 unit per hour)
        self.age += time_elapsed / 3600

        # Update the last interaction time
        self.last_interaction_time = current_time
        
        return self.happiness

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

    def name_getter(self):
        return self.name
    
    def health_getter(self):
        return self.health
    
    def happiness_getter(self):
        return self.happiness
    
    def hygiene_getter(self):
        return self.hygiene
    
    def age_getter(self):
        return self.age
    
    def weight_getter(self):
        return self.weight
    
    def intelligence_getter(self):
        return self.intelligence
    
    def hunger_getter(self):
        return self.hunger
    
    def strength_getter(self):
        return self.strength
    
    def last_interaction_time_getter(self):
        return self.last_interaction_time
    
    def saving_attributes(self):
        saved_data=[]
        saved_data.append(self.name_getter())
        print(saved_data)
        saved_data.append(self.health_getter())
        print(saved_data)
        saved_data.append(self.happiness_getter())
        print(saved_data)
        saved_data.append(self.hygiene_getter())
        print(saved_data)
        saved_data.append(self.age_getter())
        print(saved_data)
        saved_data.append(self.weight_getter())
        print(saved_data)
        saved_data.append(self.intelligence_getter())
        print(saved_data)
        saved_data.append(self.hunger_getter())
        print(saved_data)
        saved_data.append(self.strength_getter())
        print(saved_data)
        saved_data.append(self.last_interaction_time_getter())
        print(saved_data)
        file = open('stats.txt', 'w')
        file.write(str(saved_data))
        file.close() 
        
    
    

thisTamagotchi= Tamagotchi("maddie")
thisTamagotchi.saving_attributes()

file = open('stats.txt', 'r')
data = file.read() 
# replacing end of line('/n') with ' ' and 
# splitting the text it further when '.' is seen. 
data_into_list = data.replace('\n', ' ').split(",") 
# printing the data 
print(data_into_list) 
file.close() 





# file = open('stats.txt', 'w')
# file.write(saved_name=thisTamagotchi.name_getter())
# file.write(saved_health=thisTamagotchi.health_getter())
# file.write(saved_happiness=thisTamagotchi.happiness_getter())
# file.write(saved_hygiene=thisTamagotchi.hygiene_getter())
# file.write(saved_age=thisTamagotchi.age_getter())
# file.write(saved_weight=thisTamagotchi.weight_getter())
# file.write(saved_intelligence=thisTamagotchi.intelligence_getter())
# file.write(saved_hunger=thisTamagotchi.hunger_getter())
# file.write(saved_strength=thisTamagotchi.strength_getter())
# file.write(saved_last_interaction_time=thisTamagotchi.last_interaction_time_getter())
# file.close()

# import json

# def save_state(self):
#     state = {
#         'name': self.name,
#         'health': self.health,
#         'happiness': self.happiness,
#         'hygiene': self.hygiene,
#         'age': self.age,
#         'weight': self.weight,
#         'intelligence': self
#     }
    
         


