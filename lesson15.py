import pygame

pygame.init()

W = 500
H = 500
x = 200
y = 200
x1 = 100
y1 = 100
sc = pygame.display.set_mode((W, H))
fps = pygame.time.Clock()

def draw():
    sc.fill((150, 135, 140))
    pygame.draw.circle(sc, ((120, 150, 230)), (x, y), 70)
    pygame.draw.rect(sc, ((120, 130, 250)), (x1, y1, 100, 100))
    pygame.draw.ellipse(sc, ((150, 120, 230)), (300, 350, 100, 150))
    pygame.display.update()

def move():
    global x
    x += 1
    if x >= H+100:
        x = -100

def move1():
    global y1
    y1 += 1
    if y1 >= W+100:
        y1 = -100


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    draw()
    move()
    move1()
    fps.tick(240)