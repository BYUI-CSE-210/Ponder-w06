import pygame 
from pygame.locals import *

pygame.init()   

#screen
screen_width = 600
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Batter")

#define colors
bg = (234, 218, 184)
#brick colors
block_red = (242, 85, 96,)
block_blue = (86, 174, 87)
block_green = (69, 177, 233)
#paddle colrs
paddle_col = (142, 135, 123)
paddle_outline = (100,100,100)
#ball color


#game varibles
cols = 6
rows = 6
clock = pygame.time.Clock()
fps = 60

class wall():
    def __init__(self):
        self.width = screen_width // cols
        self.height = 50

    def create_wall (self):
        self.blocks = []
        block_individual = []
        for row in range (rows):
            block_row = []
            for col in range (cols):
                block_x = col * self.width 
                block_y = row * self.height
                rect = pygame.Rect(block_x,block_y, self.width, self.height)
                if row < 2:
                    strength = 3 
                elif row < 4:
                    strength = 2 
                elif row < 6:
                    strength = 1 
                block_individual = [rect, strength]
                block_row.append(block_individual)
            self.blocks.append(block_row)


def draw_wall(self):
    for row in self.blocks:
        for block in row:
            if block [1] == 3:
                block_col = block_blue
            elif block [1] == 2:
                block_col = block_green
            elif block [1] == 1:
                block_col = block_red
            pygame.draw.rect(screen, block_col, block[0])
            pygame.draw.rect(screen, bg, (block[0]),2)

class paddle ():
    def __init__(self):
        #paddle varibles
        self.width = int(screen_width / cols)
        self.height = 20
        self.x = int((screen_width/2)-(self.width / 2))
        self.y = screen_height = (self.height *2)
        self.speed = 10 
        self.rect = Rect(self.x, self.y, self.width, self.height)
        self.direction = 0

    def move (self):
        self.direction = 0 
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
            self.direction = -1
        if key[pygame.K_RIGHT] and self.rect.right < screen_width:
            self.rect.x += self.speed
            self.direction = 1
    def draw(self):
        pygame.draw.rect(screen, paddle_col, self.rect)    
        pygame.draw.rect(screen, paddle_outline, self.rect, 3)    

class game_ball():
    def __init__(self, x, y):
                self.ball_rad =10
                self.x = x - self.ball_rad
                self.y = y 
                self.rect = Rect (self.x, self.y, self.ball_rad * 2, self.ball_rad * 2)
                self.speed_x = 4
                self.speed_y = -4
                self.game_over = 0

    def draw (self):
        pygame.draw.circle(screen, paddle_col, (self.rect.x + self.ball_rad, self.rect.y + self.ball_rad),self.ball_rad)    
        pygame.draw.circle(screen, paddle_outline, (self.rect.x + self.ball_rad, self.rect.y + self.ball_rad),self.ball_rad)    

    def move(self):
        #check with collision with walls 
        if self.rect.left < 0 or self.rect.right > screen_width:
            self.speed_x *= -1
        #check collision with top and bottom 
        if self.rect.top < 0:
            self.speed_y *= -1
        if self.rect.bottom > screen_height:
            self.game_over = -1

        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        return self.game_over




#create wall
wall = wall()
wall.create_wall()
#create paddle
player_paddle = paddle()
#create ball
ball= game_ball(player_paddle.x + (player_paddle.width // 2), player_paddle.y - player_paddle.height )




#main game loop
run = True
while run:
    clock.tick(fps)
    screen.fill(bg)

    #draw wall
    #wall.draw_wall()

    #draw paddle
    player_paddle.draw()
    player_paddle.move()

    #draw ball
    ball.draw()
    ball.move()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()