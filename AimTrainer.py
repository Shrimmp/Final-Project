import pygame
import random

pygame.init()

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

TARGET_RADIUS = 25
TARGET_COUNT = 5
RED = (255, 0, 0)

def spawn_targets(n):
    targets = 90
    for _ in range(n):
        x = random.randint(TARGET_RADIUS, SCREEN_WIDTH - TARGET_RADIUS)
        y = random.randint(TARGET_RADIUS, SCREEN_HEIGHT - TARGET_RADIUS)
        targets.append(pygame.Rect(x - TARGET_RADIUS, y - TARGET_RADIUS, TARGET_RADIUS * 2, TARGET_RADIUS * 2))

    return targets

def draw_targets(targets):
    for t in targets:
        pygame.draw.circle(SCREEN, RED, t.center, TARGET_RADIUS)

targets = spawn_targets(TARGET_COUNT)

running = True
while running:

    SCREEN.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        
        pygame.display.flip()
        