import pygame
import random
import time

pygame.init()

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Flicky Aim Trainer")

TARGET_RADIUS = 25
TARGET_COUNT = 5
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (1, 50, 34)
FONT = pygame.font.SysFont("Arial", 36)
TOP_BLOCK_HEIGHT = 120
TOP_BLOCK = pygame.Rect(0, 0, SCREEN_WIDTH, TOP_BLOCK_HEIGHT)

MENU = "menu"
PLAYING = "playing"
END = "end"
state = MENU

GAME_TIME = 60

def spawn_targets(n):
    targets = []
    for _ in range(n):
        x = random.randint(TARGET_RADIUS, SCREEN_WIDTH - TARGET_RADIUS)
        y = random.randint(TARGET_RADIUS, SCREEN_HEIGHT - TARGET_RADIUS)
        rect = pygame.Rect(x - TARGET_RADIUS, y - TARGET_RADIUS, TARGET_RADIUS * 2, TARGET_RADIUS * 2)

        if rect.colliderect(TOP_BLOCK):
            continue

        overlap = False
        for t in targets:
            if rect.colliderect(t):
                overlap = True
                break

        if overlap:
            continue
        
        targets.append(rect)

    return targets

def draw_targets(targets):
    for t in targets:
        pygame.draw.circle(SCREEN, RED, t.center, TARGET_RADIUS)

def draw_text(text, y, color=WHITE):
    label = FONT.render(text, True, color)
    rect = label.get_rect(center = (SCREEN_WIDTH//2, y))
    SCREEN.blit(label, rect)

def draw_button(text, rect, color):
    pygame.draw.rect(SCREEN, color, rect)
    label = FONT.render(text, True, WHITE)
    label_rect = label.get_rect(center = rect.center)
    SCREEN.blit(label, label_rect)

start_button = pygame.Rect(SCREEN_WIDTH//2 - 100, 300, 200, 60)
replay_button = pygame.Rect(SCREEN_WIDTH//2 - 100, 350, 200, 60)

start_time = 0
score = 0
targets = spawn_targets(TARGET_COUNT)

running = True
while running:

    SCREEN.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if state == MENU:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if start_button.collidepoint(event.pos):
                    state = PLAYING
                    score = 0
                    targets = spawn_targets(TARGET_COUNT)
                    start_time = time.time()

        elif state == PLAYING:
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
                    score += 1

                    if len(targets) == 0:
                       targets = spawn_targets(TARGET_COUNT)
        elif state == END:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if replay_button.collidepoint(event.pos):
                    state = PLAYING
                    score = 0
                    targets = spawn_targets(TARGET_COUNT)
                    start_time = time.time()

    if state == MENU:
        draw_text("FPS TRAINER", 150)
        draw_button("START", start_button, GREEN)

    elif state == PLAYING:
        elapsed = time.time() - start_time
        time_left = max(0, GAME_TIME - int(elapsed))
        if time_left == 0:
            state = END

        draw_text(f"Time: {time_left}", 40)
        draw_text(f"Score: {score}", 80)

        draw_targets(targets)

    elif state == END:
        draw_text("Time's Up!", 150)
        draw_text(f"Final Score: {score}", 230)
        draw_button("Replay?", replay_button, RED)
    
    pygame.display.update()

pygame.quit()
        