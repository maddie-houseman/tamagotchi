import time

class Tamagotchi:
    def __init__(self, name):
        self.name = name
        self.saved_data = self.load_data_from_file()
        
        # Assign attributes from saved_data
        self.health = self.saved_data[1]
        self.happiness = self.saved_data[2]
        self.hygiene = self.saved_data[3]
        self.age = self.saved_data[4]
        self.weight = self.saved_data[5]
        self.intelligence = self.saved_data[6]
        self.hunger = self.saved_data[7]
        self.strength = self.saved_data[8]
        self.first_time = self.saved_data[9]
        self.last_interaction_time = self.saved_data[10]
    
    def load_data_from_file(self):
        try:
            with open("stats.txt", "r") as file:
                data = file.read().split(", ")
                # Convert numeric strings back to floats/integers
                data[1:] = [float(item) if '.' in item else int(item) for item in data[1:]]
            return data
        except FileNotFoundError:
            # If the file doesn't exist, initialize with default data
            default_data = ["maddie", 100, 100, 100, 0, 5, 50, 0, 10, time.time(), time.time()]
            with open("stats.txt", "w") as file:
                file.write(", ".join(map(str, default_data)))
            return default_data

    def print_attributes(self):
        print(self.name, "health", self.health, "etc", "first time:", self.first_time, "last interaction:", self.last_interaction_time, "current time=", time.time())

    def update(self):
        current_time = time.time()
        time_elapsed = current_time - self.last_interaction_time
        self.health -= time_elapsed * 0.01
        self.happiness -= time_elapsed * 0.01
        self.hygiene -= time_elapsed * 0.03
        self.age += time_elapsed / 3600
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
        self.health += 10
        self.check_limits()

    def doctor(self):
        self.update()
        self.health = 100
        self.check_limits()

    def check_limits(self):
        self.health = max(0, min(100, self.health))
        self.happiness = max(0, min(100, self.happiness))
        self.hygiene = max(0, min(100, self.hygiene))
    
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

    def resetting_attributes_infile(self):
        # Update saved_data with current attributes
        self.saved_data[1] = self.health
        self.saved_data[2] = self.happiness
        self.saved_data[3] = self.hygiene
        self.saved_data[4] = self.age
        self.saved_data[5] = self.weight
        self.saved_data[6] = self.intelligence
        self.saved_data[7] = self.hunger
        self.saved_data[8] = self.strength
        self.saved_data[9] = self.first_time
        self.saved_data[10] = self.last_interaction_time

        # Write updated data back to file
        with open("stats.txt", "w") as file:
            file.write(", ".join(map(str, self.saved_data)))

    def print_attributes2(self):
        print(self.name, self.health, "etc", "first time:", self.first_time, "last interaction:", self.last_interaction_time, "current time=", time.time())

# Instantiate Tamagotchi which reads directly from file
thisTamagotchi = Tamagotchi("maddie")
print("new atributes from time passed")
thisTamagotchi.print_attributes()
thisTamagotchi.update()
thisTamagotchi.feed("healthy")
thisTamagotchi.resetting_attributes_infile()
print("new attributes from game played")
thisTamagotchi.print_attributes2()

