import pygame
import random
import math
import sys

pygame.init()

screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Snake')
bckgrndimage=pygame.image.load('bckgrnd.jpg')


class Snake:

    def __init__(self):
        self.size = 1
        self.elements = [[100, 100]]
        self.radius = 8
        self.dx = 4  
        self.dy = 0
        self.is_add = False

    def draw(self):
        for element in self.elements:
            pygame.draw.circle(screen, (0, 255, 0), element, self.radius)

    def add_to_snake(self):
        self.size += 1
        self.elements.append([0, 0])
        self.is_add = False

    def move(self):
        if self.is_add:
            self.add_to_snake()

        for i in range(self.size - 1, 0, -1):
            self.elements[i][0] = self.elements[i - 1][0]
            self.elements[i][1] = self.elements[i - 1][1]

        self.elements[0][0] += self.dx
        self.elements[0][1] += self.dy

GameIsOverImage  = pygame.image.load("GameOver.bmp")
foodImage = pygame.image.load("apple.png")
food_x = random.randint(0, 570)
food_y = random.randint(0, 570)

def GameIsOver():
    screen.blit(GameIsOverImage,(0, 0))
def food(x, y):
    screen.blit(foodImage, (x, y))
def Collision(x1, y1, x2, y2):
    q = math.sqrt((math.pow(x1 - x2,2))+(math.pow(y1-y2,2)))
    if q < 25:
        return True
    else:
        return False

snake = Snake()

running = True
points = 0
font1 = pygame.font.Font(None , 30)
score_x = 10
score_y = 10

def Score(x, y):
    score = font1.render("Score:" + str(points), True , (0, 0, 0))
    screen.blit(score, (x, y))

FPS = 20 

clock = pygame.time.Clock()

k1_pressed = False

while running:
    mill = clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_RIGHT:
                snake.dx = 5
                snake.dy = 0
            if event.key == pygame.K_LEFT:
                snake.dx = -5
                snake.dy = 0
            if event.key == pygame.K_UP:
                snake.dx = 0
                snake.dy = -5
            if event.key == pygame.K_DOWN:
                snake.dx = 0
                snake.dy = 5

    snake.move()
    #screen.fill((255, 255, 255))
    screen.blit(bckgrndimage, (0, 0))
    snake.draw()
    food(food_x, food_y)
    Score(score_x, score_y)                
    interaction = Collision(snake.elements[0][0], snake.elements[0][1], food_x, food_y)

    if interaction:
        points += 1
        food_x = random.randint(0, 570)
        food_y = random.randint(0, 570)
        snake.is_add = True

    if snake.elements[0][0] > 600 or snake.elements[0][0] < 0 or snake.elements[0][1] < 0 or snake.elements[0][1] > 600:
        pygame.time.delay(2000)
        GameIsOver()
        snake.dx = 0
        snake.dy = 0
        
    pygame.display.flip()