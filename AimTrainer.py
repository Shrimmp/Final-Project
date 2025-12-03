import pygame
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

TARGET_RADIUS = 25
TARGET_COUNT = 5
RED = (255, 0, 0)

def spawn_targets(n):
    targets = []
    for _ in range(n):
        x = random.randint(TARGET_RADIUS, SCREEN_WIDTH - TARGET_RADIUS)
        y = random.randint(TARGET_RADIUS, SCREEN_HEIGHT - TARGET_RADIUS)
        rect = pygame.Rect(x - TARGET_RADIUS, y - TARGET_RADIUS, TARGET_RADIUS * 2, TARGET_RADIUS * 2)
        targets.append(rect)

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
        
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = event.pos
            clicked = None

            for t in targets:
                dx = mouse_pos[0] - t.centerx
                dy = mouse_pos[1] - t.centery
                if dx * dx + dy * dy <= TARGET_RADIUS * TARGET_RADIUS:
                    clicked = t
                    break

            if clicked:
                targets.remove(clicked)

                if len(targets) == 0:
                   targets = spawn_targets(TARGET_COUNT)
                    
    draw_targets(targets)
    pygame.display.update()

pygame.quit()
        