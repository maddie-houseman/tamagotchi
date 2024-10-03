import pygame
import sys

# Initialize pygame
pygame.init()

# Constants for screen size and colors
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BUTTON_COLOR = (100, 200, 100)

# Set up display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Tamagotchi')

# Load Tamagotchi images for different ages
tamagotchi_baby = pygame.image.load("C:\\Users\\mcost\\OneDrive - Wellington College\\Pictures\\Saved Pictures\\Tamagatchi_baby.png")
tamagotchi_child = pygame.image.load("C:\\Users\\mcost\\OneDrive - Wellington College\\Pictures\\Saved Pictures\\Tamagatchi_child.png")
tamagotchi_adult = pygame.image.load("C:\\Users\\mcost\\OneDrive - Wellington College\\Pictures\\Saved Pictures\\Tamagatchi_adult.png")

# Resize images
tamagotchi_baby = pygame.transform.scale(tamagotchi_baby, (200, 200))
tamagotchi_child = pygame.transform.scale(tamagotchi_child, (200, 200))
tamagotchi_adult = pygame.transform.scale(tamagotchi_adult, (200, 200))

# To put into the functions
feedPressed = False
washPressed = False
playPressed = False
sleepPressed = False
doctorPressed = False
workoutPressed = False

# Age of the Tamagotchi (can be 0=baby, 1=child, 2=adult)
age = 0

# Button class
class Button:
    def __init__(self, x, y, width, height, text):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text

    def draw(self, screen):
        pygame.draw.rect(screen, BUTTON_COLOR, self.rect)
        font = pygame.font.Font(None, 36)
        text_surf = font.render(self.text, True, BLACK)
        text_rect = text_surf.get_rect(center=self.rect.center)
        screen.blit(text_surf, text_rect)

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)

# Create buttons
buttons = [
    Button(50, 450, 100, 50, 'Feed'),
    Button(200, 450, 100, 50, 'Wash'),
    Button(350, 450, 100, 50, 'Play'),
    Button(500, 450, 100, 50, 'Sleep'),
    Button(650, 450, 100, 50, 'Doctor'),
    Button(300, 520, 150, 50, 'Workout')
]

# Function to display Tamagotchi image based on age
def display_tamagotchi(age):
    if age>= 0 and age < 14:
        screen.blit(tamagotchi_baby, (300, 200))
    elif age > 14 and age < 30:
        screen.blit(tamagotchi_child, (300, 200))
    elif age > 30 and age < 60:
        screen.blit(tamagotchi_adult, (300, 200))

# Main game loop
running = True
while running:
    screen.fill(WHITE)
    
    # Display Tamagotchi
    display_tamagotchi(age)
    
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
    
    pygame.display.flip()

# Quit pygame
pygame.quit()
sys.exit()