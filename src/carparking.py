import pygame
import random

# --- SETTINGS ---
ROWS = 2
COLS = 8
SLOT_WIDTH = 80
SLOT_HEIGHT = 120
LANE_WIDTH = 100
PADDING = 50
FPS = 60
AUTO_SPAWN_DELAY = 120  # frames (2 seconds at 60 FPS)

# Calculate window size
WINDOW_WIDTH = (COLS * SLOT_WIDTH) + LANE_WIDTH + PADDING
WINDOW_HEIGHT = (ROWS * SLOT_HEIGHT) + LANE_WIDTH + PADDING

pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Smart Parking Simulator")
clock = pygame.time.Clock()

# Load car image
car_img = pygame.image.load("car.png").convert_alpha()
car_img = pygame.transform.scale(car_img, (60, 100))

# Slot data
slots = [[None for _ in range(COLS)] for _ in range(ROWS)]
cars = []

auto_mode = False
running = True
title_screen = True
last_spawn_time = -AUTO_SPAWN_DELAY


def draw_parking_lot():
    screen.fill((0, 0, 0))  # Black asphalt
    for row in range(ROWS):
        for col in range(COLS):
            if row == 0:
                y_pos = row * SLOT_HEIGHT
            else:
                y_pos = row * SLOT_HEIGHT + LANE_WIDTH
            x_pos = col * SLOT_WIDTH
            rect = pygame.Rect(x_pos, y_pos, SLOT_WIDTH, SLOT_HEIGHT)
            pygame.draw.rect(screen, (255, 255, 0), rect, 3)


class Car:
    def __init__(self, row, col, leaving=False):
        self.row = row
        self.col = col
        self.x = -100 if not leaving else col * SLOT_WIDTH + 10
        self.y = SLOT_HEIGHT // 2 + (row * (SLOT_HEIGHT + LANE_WIDTH))
        self.angle = 0 if not leaving else 0
        self.parked = False
        self.leaving = leaving
        self.phase = 0
        self.target_x = col * SLOT_WIDTH + 10
        self.target_y = self.y

    def update(self):
        if self.leaving:
            # Leaving phases
            if self.phase == 0:
                # Reverse straight out
                if self.row == 0:
                    if self.y < SLOT_HEIGHT // 2 + (self.row * (SLOT_HEIGHT + LANE_WIDTH)):
                        self.y += 5
                    else:
                        self.phase = 1
                else:
                    if self.y > SLOT_HEIGHT // 2 + (self.row * (SLOT_HEIGHT + LANE_WIDTH)):
                        self.y -= 5
                    else:
                        self.phase = 1
            elif self.phase == 1:
                # Instant turn toward exit
                self.angle = 0
                self.phase = 2
            elif self.phase == 2:
                # Drive to the right until off-screen
                if self.x < WINDOW_WIDTH + 100:
                    self.x += 5
                else:
                    cars.remove(self)
            return

        # Parking sequence
        if not self.parked:
            if self.phase == 0:
                if self.x < self.target_x - 30:
                    self.x += 5
                else:
                    self.phase = 1
            elif self.phase == 1:
                if self.row == 0:
                    if self.y > self.row * SLOT_HEIGHT:
                        self.y -= 5
                    else:
                        self.parked = True
                        slots[self.row][self.col] = self
                else:
                    if self.y < self.row * (SLOT_HEIGHT + LANE_WIDTH):
                        self.y += 5
                    else:
                        self.parked = True
                        slots[self.row][self.col] = self

    def draw(self):
        rotated = pygame.transform.rotate(car_img, self.angle)
        screen.blit(rotated, (self.x, self.y))


def find_nearest_free_slot():
    for col in range(COLS):
        for row in range(ROWS):
            if slots[row][col] is None:
                return row, col
    return None


def add_car():
    global last_spawn_time
    slot = find_nearest_free_slot()
    if slot:
        row, col = slot
        car = Car(row, col)
        cars.append(car)
        last_spawn_time = pygame.time.get_ticks()


def remove_car():
    parked_cars = [c for c in cars if c.parked and not c.leaving]
    if parked_cars:
        car = random.choice(parked_cars)
        slots[car.row][car.col] = None
        car.leaving = True
        car.phase = 0


# --- Main Loop ---
while running:
    if title_screen:
        screen.fill((30, 30, 30))
        font = pygame.font.SysFont(None, 72)
        title_text = font.render("Smart Parking Simulator", True, (255, 255, 0))
        screen.blit(title_text, (50, 150))
        font_small = pygame.font.SysFont(None, 36)
        start_text = font_small.render("Press SPACE to Start", True, (200, 200, 200))
        screen.blit(start_text, (200, 300))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                title_screen = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    title_screen = False
        continue

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                add_car()
            if event.key == pygame.K_r:
                remove_car()
            if event.key == pygame.K_t:
                auto_mode = not auto_mode

    now = pygame.time.get_ticks()
    if auto_mode:
        if now - last_spawn_time > AUTO_SPAWN_DELAY * (1000 // FPS) and random.randint(1, 60) == 1:
            add_car()
        if random.randint(1, 100) == 1:
            remove_car()

    draw_parking_lot()
    for car in list(cars):
        car.update()
        car.draw()

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
