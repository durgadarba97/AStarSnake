import pygame
from Snake import *
from A_star import *

class GUI:
        def __init__(self):
                pygame.init()
                self.window = self.createWindow()
                self.clock = self.createClock()

        def createWindow(self):
                window = pygame.display.set_mode((200, 200))
                pygame.display.set_caption("Snake")  
                return window
        
        def createClock(self):
              clock = pygame.time.Clock()  
              return clock

        def tick(self):
                self.clock.tick(10)

        def update(self, body, food):

                for x in body:
                        pygame.draw.rect(self.window, (80,80,80), (x.posx, x.posy, x.width, x.height))

                pygame.draw.rect(self.window, (248, 131, 121), (food.tile.posx, food.tile.posy, 10, 10))
                pygame.display.update()

                self.window.fill((255,255,255))
                
                self.tick()

        def handleQuit(self):
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                return False
                return True
        
        def exitGame(self):
                pygame.quit()

# def notmain():

#         #Sets up the window and initializes everything
#         pygame.init()
#         window = pygame.display.set_mode((200, 200))
#         pygame.display.set_caption("Snake")
#         window.fill((255,255,255))
#         pygame.font.init()

#         clock = pygame.time.Clock()

#         #Main loops that controls the game states
#         while True:
#                 if gameplayState(window, clock) == False:
#                         break
#                 if endgameState(window, clock) == False:
#                         break
#         pygame.quit()
                

# #The state that handle the game play itself
# def gameplayState(window, clock):

#         #Creates snake head and a couple body parts to start out with.
#         head = Snake(50,50)
#         body = [head]
#         body.append(Snake(40,50))
#         body.append(Snake(30,50))
#         body.append(Snake(20,50))
#         food = Food()

#         aStar = A_star()
        
#         tmppath = aStar.run(body, food.tile)
#         if tmppath is not None:
#                 path = tmppath
#                 path.pop()

        
#         #Main Game loop
#         while True:

#                 #Checks to see if window was quit
#                 for event in pygame.event.get():
#                         if event.type == pygame.QUIT:
#                                 return False

#                 #Handles A* path
#                 if len(path) == 0:
#                         tmppath = aStar.run(body, food.tile)

#                         if tmppath is not None:
#                                 path = tmppath
#                                 path.pop()

#                 if tmppath is not None:
#                         lastelement = path.pop()
# ##                        print("lastelement: "+str(lastelement.posx) + ", " + str(lastelement.posy))
#                         if lastelement.posx > head.tile.posx:
#                                 head.direction = 3
#                         elif lastelement.posx < head.tile.posx:
#                                 head.direction = 4
#                         elif lastelement.posy > head.tile.posy:
#                                 head.direction = 2
#                         elif lastelement.posy < head.tile.posy:
#                                 head.direction = 1
                
#                 #Handles key movement. Manual movement messes with the algorithm, so i commented it out.
# ##                keys = pygame.key.get_pressed()
# ##
# ##                if keys[pygame.K_UP] and head.direction != 2:
# ##                        head.direction = 1
# ##                elif keys[pygame.K_DOWN] and head.direction != 1:
# ##                        head.direction = 2
# ##                elif keys[pygame.K_RIGHT] and head.direction != 4:
# ##                        head.direction = 3
# ##                elif keys[pygame.K_LEFT] and head.direction != 3:
# ##                        head.direction = 4
                        
#                 head.move(body)

#                 #If snake gets to the food, then it adds to the end of snake body.
#                 if head.tile.posx == food.tile.posx and head.tile.posy == food.tile.posy:
#                         sx = body[(len(body)-1)].tile.posx
#                         sy = body[(len(body)-1)].tile.posy
#                         if head.direction == 1:
#                                 body.append(Snake(sx , (sy+10)))
#                         if head.direction == 2:
#                                 body.append(Snake(sx , (sy-10)))
#                         if head.direction == 3:
#                                 body.append(Snake((sx-10) , sy))
#                         if head.direction == 4:
#                                 body.append(Snake((sx+10) , sy))
                                
#                         food.generateFood()

#                 #Sets up the game rules. Cannot go outside the window and can't collide with itself
#                 if head.tile.posx < 0 or head.tile.posx >= 200 or head.tile.posy < 0 or head.tile.posy >= 200:
#                         pygame.time.wait(500)
#                         return True
                        
#                 if hasCollided(body):
#                         pygame.time.wait(500)
#                         return True

#                 #Draws and updates screen     
#                 for x in body:
#                         pygame.draw.rect(window, (80,80,80), (x.tile.posx, x.tile.posy, x.width, x.height))

#                 pygame.draw.rect(window, (248, 131, 121), (food.tile.posx, food.tile.posy, 10, 10))
#                 pygame.display.update()

#                 window.fill((255,255,255))
                
#                 clock.tick(10)

# #State that handles what happens when you lose
# def endgameState(window, clock):

#         #Sets up the font used in Game over Screen
#         myfont = pygame.font.SysFont('Comic Sans MS', 30)

#         while True:

#                 #Checks if screen is exited or player wishes to restart by clicking the screen
#                 for event in pygame.event.get():
#                         if event.type == pygame.QUIT:
#                                 return False
#                         elif event.type == pygame.MOUSEBUTTONUP:
#                                 return True

#                 #Draws and update screen
#                 window.fill((255,255,255))
#                 textsurface = myfont.render('Game Over', False, (0, 0, 0))
#                 window.blit(textsurface,(0,0))
#                 pygame.display.update()

#                 clock.tick(10)

# #Helper method for collision detection
# def hasCollided(body):
        
#         x = body[0].tile.posx
#         y = body[0].tile.posy

#         #Goes through the length of the snake to see if the head position matches the body position.
#         #Not entirely a great way to do this. I want to reorginze this in the future.
#         for i in range(1, len(body)-1):
#                 if body[i].tile.posx == x and body[i].tile.posy == y:
#                         return True
        
#         return False
        

# if __name__== "__main__":
#         notmain()

