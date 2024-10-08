import time

import pygame
import sys

pygame.init()

# Sizes and colors
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (173, 216, 230)  # Light blue for the attributes column background
BUTTON_COLOR = (100, 200, 100)
BUTTON_HEIGHT = 100  # Height for buttons
STATS_WIDTH = 200   # Width of the stats column
BUTTON_PADDING = 0

# Setting up display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Tamagotchi')

# Loading ze Tamagotchi images for different ages
tamagotchi_baby = pygame.image.load("C:\\Users\\mcost\\OneDrive - Wellington College\\Pictures\\Saved Pictures\\Tamagatchi_baby.png")
tamagotchi_child = pygame.image.load("C:\\Users\\mcost\\OneDrive - Wellington College\\Pictures\\Saved Pictures\\Tamagatchi_child.png")
tamagotchi_adult = pygame.image.load("C:\\Users\\mcost\\OneDrive - Wellington College\\Pictures\\Saved Pictures\\Tamagatchi_adult.png")
tamagotchi_old = pygame.image.load("C:\\Users\\mcost\\OneDrive - Wellington College\\Pictures\\Saved Pictures\\Tamagatchi_old.png")

# Resize da images
tamagotchi_baby = pygame.transform.scale(tamagotchi_baby, (300, 300))
tamagotchi_child = pygame.transform.scale(tamagotchi_child, (300, 300))
tamagotchi_adult = pygame.transform.scale(tamagotchi_adult, (300, 300))
tamagotchi_old = pygame.transform.scale(tamagotchi_old, (300,300))

# Button states
feedPressed = False
washPressed = False
playPressed = False
sleepPressed = False
doctorPressed = False
workoutPressed = False
studyPressed = False


# Button class
class Button:
    def __init__(self, x, y, width, height, text):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text

    def draw(self, screen):
        pygame.draw.rect(screen, BUTTON_COLOR, self.rect)
        pygame.draw.rect(screen, BLACK, self.rect, 3)  # Outline the button in black
        font = pygame.font.Font(None, 36)  # Increased font size for buttons
        text_surf = font.render(self.text, True, BLACK)
        text_rect = text_surf.get_rect(center=self.rect.center)
        screen.blit(text_surf, text_rect)

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)

# Function to create buttons that fill the entire bottom row
def create_buttons():
    num_buttons = 7
    button_width = SCREEN_WIDTH // num_buttons  # Full width of the screen
    buttons = []
    for i, label in enumerate(['Feed', 'Wash', 'Play', 'Sleep', 'Doctor', 'Workout', 'Study']):
        x_pos = i * button_width
        y_pos = SCREEN_HEIGHT - BUTTON_HEIGHT
        buttons.append(Button(x_pos, y_pos, button_width, BUTTON_HEIGHT, label))
    return buttons

# Create the buttons
buttons = create_buttons()

# Function to display Tamagotchi image based on age
def display_tamagotchi(age):
    if age >= 0 and age < 14:
        tamagotchi_image = tamagotchi_baby
    elif age > 14 and age < 30:
        tamagotchi_image = tamagotchi_child
    elif age > 30 and age < 60:
        tamagotchi_image = tamagotchi_adult
    else:
        tamagotchi_image = tamagotchi_old

    # Calculate the center position of the character in the reduced top-left space
    available_width = SCREEN_WIDTH
    available_height = SCREEN_HEIGHT - BUTTON_HEIGHT
    tamagotchi_x = (available_width - tamagotchi_image.get_width()) // 2
    tamagotchi_y = (available_height - tamagotchi_image.get_height()) // 4  # Slightly higher to leave room for the buttons

    screen.blit(tamagotchi_image, (tamagotchi_x, tamagotchi_y))

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

# Tamagotchi attributes OBVIOUSLY WILL TAKE ATTRIBUTES FROM MADDIES CODE
tamagotchi_stats = {
    "name": thisTamagotchi.name_getter(),
    "health": thisTamagotchi.health_getter(),
    "happiness": thisTamagotchi.happiness_getter(),
    "age": int(thisTamagotchi.age_getter()),  # Convert age to integer for display
    "weight": thisTamagotchi.weight_getter(),
    "intelligence": thisTamagotchi.intelligence_getter(),
    "hunger": thisTamagotchi.hunger_getter(),
    "strength": thisTamagotchi.strength_getter()
}

# Age of the Tamagotchi (for testing)
age = int(thisTamagotchi.age_getter())

# Function to display Tamagotchi stats
def display_stats():
    # Fill the stats column background with blue
    pygame.draw.rect(screen, BLUE, (SCREEN_WIDTH - STATS_WIDTH, 0, STATS_WIDTH, SCREEN_HEIGHT - BUTTON_HEIGHT))

    font = pygame.font.Font(None, 32)  # Slightly smaller font size for stats
    y_offset = 50
    for key, value in tamagotchi_stats.items():
        text_surf = font.render(f"{key.capitalize()}: {value}", True, BLACK)
        screen.blit(text_surf, (SCREEN_WIDTH - STATS_WIDTH + 20, y_offset))
        y_offset += 50  # Increased line height for readability


# Main game loop
running = True
while running:
    screen.fill(WHITE)
    
    # Display Tamagotchi
    display_tamagotchi(age)
    
    # Display Tamagotchi stats
    display_stats()
    
    # Draw buttons
    for button in buttons:
        button.draw(screen)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            # Check button clicks
            if buttons[0].is_clicked(pos):
                feedPressed = True
                print("Feed button pressed")
            elif buttons[1].is_clicked(pos):
                washPressed = True
                print("Wash button pressed")
            elif buttons[2].is_clicked(pos):
                playPressed = True
                print("Play button pressed")
            elif buttons[3].is_clicked(pos):
                sleepPressed = True
                print("Sleep button pressed")
            elif buttons[4].is_clicked(pos):
                doctorPressed = True
                print("Doctor button pressed")
            elif buttons[5].is_clicked(pos):
                workoutPressed = True
                print("Workout button pressed")
            elif buttons[6].is_clicked(pos):
                studyPressed = True
                print("Study button pressed")
    
    pygame.display.flip()

# Quit pygame
pygame.quit()
sys.exit()