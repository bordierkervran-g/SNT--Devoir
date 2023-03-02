import pygame, sys
from pygame.locals import Rect
import random
pygame.init()

size = width, height = 400, 400
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Snake")

touch:bool
pos:tuple[int,int]
position_history:list
coor: tuple[int, int]
direction:str
gameOver:bool
gameOverBtn:Rect
gameOverSurface:pygame.Surface
gameoverOverlay:pygame.Surface
apple:pygame.Surface
bg:pygame.Surface
lenght:int
allowAction:bool
WHITE:tuple[int,int,int] = (255,255,255)
BLACK:tuple[int,int,int] = (0,0,0)

class Button():
    def __init__(self, x, y, image) -> None:
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
    def draw(self):
        screen.blit(self.image, (self.rect.x,self.rect.y))
    def collidepoint(self, pos):
        return self.rect.collidepoint(pos)

def display_apple(new_coor = False):
    global coor
    if new_coor:
        while True:
            coor = (random.randint(1,20)*int(height/20)-apple.get_height(), random.randint(1,20)*int(width/20)-apple.get_width())
            if (int((coor[0])/20),int((coor[1])/20)) not in position_history[::-1][:lenght]: break
    screen.blit(apple, coor)

def update():
    global score
    screen.fill(WHITE)
    screen.blit(bg, (0, 0))
    display_apple()
    color = int(255/len(position_history[::-1][:lenght]))
    color_step = 1
    for i in position_history[::-1][:lenght]:
        pygame.draw.rect(screen,(color*color_step,color*color_step,color*color_step),(int(height/20*i[0]), int(width/20*(i[1])),20,20))
        color_step += 1
    font: pygame.Font = pygame.font.SysFont(None, 48, bold=True)
    img:pygame.Surface
    img = img = font.render(str(lenght - 2), True, BLACK)
    screen.blit(img, (0, 0))

def init():
    global touch,pos,position_history,coor,direction,gameOver,gameOverSurface,gameOverBtn,gameoverOverlay,apple,bg,lenght,allowAction
    touch = False
    pos = coor = 9, 9
    pygame.draw.rect(screen,(255,0,0),(int(height/20)*pos[0], int(width/20)*pos[1],20,20))
    position_history = []
    position_history.append(pos)
    direction = random.choice(["up", "down", "left", "right"])
    gameOverSurface = pygame.image.load("GameoverButton.png")
    gameOverSurface = pygame.transform.scale(gameOverSurface,(height/3,width/10))
    gameOverBtn = Button(width/3, height/10*7, gameOverSurface)
    gameoverOverlay = pygame.image.load("Gameover.png")
    gameoverOverlay = pygame.transform.scale(gameoverOverlay,(height,width))
    apple = pygame.image.load("Apple.png")
    apple = pygame.transform.scale(apple, (int(height/20), int(width/20)))
    bg = pygame.image.load("Background.png")
    bg = pygame.transform.scale(bg,(height,width))
    lenght = 2
    allowAction = True
    display_apple(True)
    for i in range(4):
        update()
        font: pygame.Font = pygame.font.SysFont(None, 48, bold=True)
        img:pygame.Surface
        if i - 3 != 0: img = font.render(str(3-i), True, BLACK)
        else: img =    img = font.render("Go !", True, BLACK)
        screen.blit(img, (width/2-img.get_width(), height/2-img.get_height()))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
        pygame.time.wait(1000)
    gameOver = False

init()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    update()
    if not gameOver:
        pygame.time.wait(100)
        if direction == "up":      pos = tuple((list(pos)[0],pos[1]-1)); position_history.append(pos)
        elif direction == "down":  pos = tuple((list(pos)[0],pos[1]+1)); position_history.append(pos)
        elif direction == "left":  pos = tuple((list(pos)[0]-1,pos[1])); position_history.append(pos)
        elif direction == "right": pos = tuple((list(pos)[0]+1,pos[1])); position_history.append(pos)
        if (int((coor[0])/20),int((coor[1])/20)) == pos: touch = True
        allowAction = True
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and allowAction:
                if event.key == pygame.K_RIGHT and direction not in ["right", "left"]: direction = "right"; allowAction = False
                if event.key == pygame.K_LEFT and direction not in ["right", "left"]:  direction = "left";  allowAction = False
                if event.key == pygame.K_UP and direction not in ["down", "up"]:       direction = "up";    allowAction = False
                if event.key == pygame.K_DOWN and direction not in ["down", "up"]:     direction = "down";  allowAction = False
        if pos[0] < 0 or pos[0] > 19 or pos[1] < 0 or pos[1] > 19 or pos in position_history[:-1][::-1][:lenght-1]: gameOver = True
        if touch:
            display_apple(True)
            lenght += 1
            touch = False
    else:
        pygame.time.wait(250)
        screen.blit(gameoverOverlay, (0, 0))
        gameOverBtn.draw()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                if gameOverBtn.collidepoint(pygame.mouse.get_pos()):
                    init()
    pygame.display.update()
