import pygame
from random import uniform

WIDTH, HEIGHT = 1470, 956
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.toggle_fullscreen()

BLACK = (0, 0, 0)
DARKGREEN = (25, 50, 25)
WHITE = (255, 255, 255)
DARKRED = (50, 25, 25)

FPS = 60

class Player:
    #define initial position
    xPos = WIDTH / 5
    yPos = HEIGHT / 2
    xVel = 0
    yVel = 0
    
    #return the rectangle associated with the plyer for hitbox
    def getPlayerRect(self):
        return pygame.rect.Rect(self.xPos, self.yPos, 50, 50)
    #return the positon of the top left of the player's hitbox
    def getPos(self):
        return (self.xPos, self.yPos)
    #apply the vertical velocity change associated with a flap
    def flapWings(self):
        self.yVel = -10
    #move the player with respect to their velocity, and then apply the standard .3px/frame downward acceleration
    def updatePos(self):
        self.xPos += self.xVel
        self.yPos += self.yVel
        if self.yVel <= 10:
            self.yVel += .3
            
class Pipe:
    xPos = 1500
    xVel = -2
    holeTop = 100
    holeBottom = HEIGHT - 900
    
    def __init__(self):
        self.holeTop = uniform(200, HEIGHT - 325)
        self.holeBottom = self.holeTop + uniform(150, 200)
        
    def getTopRect(self):
        return pygame.rect.Rect(self.xPos, 0, 100, self.holeTop)
    
    def getBottomRect(self):
        return pygame.rect.Rect(self.xPos, self.holeBottom, 100, HEIGHT - self.holeBottom)
    
    def updatePos(self):
        self.xPos += self.xVel
        if self.xPos < -100:
            del(self)
    
    
    

def displayFrame(players, pipes):
    WIN.fill(DARKGREEN)
    
    for pipe in pipes:
        pygame.draw.rect(WIN, DARKRED, pipe.getTopRect(pipe))
        pygame.draw.rect(WIN, DARKRED, pipe.getBottomRect(pipe))        
    
    for player in players:
        pygame.draw.rect(WIN, WHITE, player.getPlayerRect(player))
        
    pygame.display.update()
    
def main():
    
    players = []
    player1 = Player
    players.append(player1)
    
    pipes = []
    
    frameCount = 0
    
    Clock = pygame.time.Clock()
    run = True
    while run:
        Clock.tick(FPS)
        
        frameCount += 1
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return 0
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE or event.key == pygame.K_w:
                    player1.flapWings(player1)
                elif event.key == pygame.K_BACKSPACE:
                    pygame.quit()
                    return 0
        
        if frameCount % 100 == 0:
            newPipe = Pipe
            pipes.append(newPipe)
        
        for pipe in pipes:
            pipe.updatePos(pipe)
        
        for player in players:
            player.updatePos(player)
        
        displayFrame(players, pipes)
    
if __name__ == '__main__':
    main()

