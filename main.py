import pygame
import random

pygame.init()

black = (0, 0, 0)
white = (255, 255, 255)

ai = input("Do you want to play against the computer? y/n\n")
spd = int(input("What speed do you want to play at?\n"))

y = 150
y1 = 150
xb = 0
yb = 0
lr = -spd
yr = 0
score = 0
score1 = 0

size = (800, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Game")
done = False
clock = pygame.time.Clock()
pygame.time.delay(3000)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.fill(black)

    p1 = pygame.draw.rect(screen, white, [120, y, 25, 100])
    p2 = pygame.draw.rect(screen, white, [680, y1, 25, 100])
    ball = pygame.draw.rect(screen, white, [390 + xb, 240 + yb, 20, 20])

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        if y > 0:
            y = y - 4
    elif keys[pygame.K_s]:
        if y < 400:
            y = y + 4
    if ai == "n":
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            if y1 > 0:
                y1 = y1 - 4
        elif keys[pygame.K_DOWN]:
            if y1 < 400:
                y1 = y1 + 4

    xb = xb + lr
    yb = yb + yr

    if ball.colliderect(p1):
        lr = spd
        yr = random.uniform(-7, 7)
    if ball.colliderect(p2):
        lr = -spd
        yr = random.uniform(-7, 7)
    if ball.y <= 0:
        yr = random.uniform(1, 3)
    if ball.y >= 480:
        yr = random.uniform(-1, -3)

    if ai == "y":
        if p2.y > 400:
            y1 = y1 - 4
        if p2.y < 0:
            y1 = y1 + 4
        if ball.y + 20 > p2.y + 100 or ball.y < p2.y:
            if ball.y > p2.y:
                y1 = y1 + 4
            if ball.y < p2.y:
                y1 = y1 - 4

    if ball.x >= 790:
        score = score + 1
        xb = 0
        yb = 0
        lr = spd
        y = 150
        y1 = 150
        yr = 0
        pygame.time.delay(2000)
    if ball.x <= 0:
        score1 = score1 + 1
        xb = 0
        yb = 0
        lr = -spd
        y = 150
        y1 = 150
        yr = 0
        pygame.time.delay(2000)

    font = pygame.font.SysFont('Calibri', 50, True, False)
    text = font.render(str(score), True, white)
    screen.blit(text, (350, 10))
    font = pygame.font.SysFont('Calibri', 50, True, False)
    text = font.render(str(score1), True, white)
    screen.blit(text, (450, 10))

    pygame.display.flip()
    clock.tick(60)
pygame.quit()
