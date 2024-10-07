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

# Tamagotchi attributes OBVIOUSLY WILL TAKE ATTRIBUTES FROM MADDIES CODE
tamagotchi_stats = {
    "name": "Tommy",
    "health": 80,
    "happiness": 60,
    "age": 10,
    "weight": 5,
    "intelligence": 40,
    "hunger": 50,
    "strength": 30
}

# Age of the Tamagotchi (for testing)
age = 0

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
