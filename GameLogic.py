# Handles all the logic of the game
from Snake import *
from A_star import *
from World import *
import sys

def main(guiinit):
    if guiinit:
        gui = GUI()

    head = Snake(50,50)
    body = [head]
    body.append(Snake(40,50))
    body.append(Snake(30,50))
    body.append(Snake(20,50))
    food = Food()

    everything = Snake(50,50)


    aStar = A_star()
    
    tmppath = aStar.run(body, food.tile)

    if tmppath is not None:
        path = tmppath
        path.pop()

    while True:
        if guiinit and not gui.handleQuit():
            break

        if len(path) == 0:
                tmppath = aStar.run(body, food.tile)

                if tmppath is not None:
                        path = tmppath
                        path.pop()

        if tmppath is not None:
                lastelement = path.pop()
##                        print("lastelement: "+str(lastelement.posx) + ", " + str(lastelement.posy))
                if lastelement.posx > head.tile.posx:
                        head.direction = 3
                elif lastelement.posx < head.tile.posx:
                        head.direction = 4
                elif lastelement.posy > head.tile.posy:
                        head.direction = 2
                elif lastelement.posy < head.tile.posy:
                        head.direction = 1

                for i in path:
                        print(str(i.posx) + ", " + str(i.posy))

                
                #Handles key movement. Manual movement messes with the algorithm, so i commented it out.
##                keys = pygame.key.get_pressed()
##
##                if keys[pygame.K_UP] and head.direction != 2:
##                        head.direction = 1
##                elif keys[pygame.K_DOWN] and head.direction != 1:
##                        head.direction = 2
##                elif keys[pygame.K_RIGHT] and head.direction != 4:
##                        head.direction = 3
##                elif keys[pygame.K_LEFT] and head.direction != 3:
##                        head.direction = 4
                        
                head.move(body)

                for i in everything.body:
                        print(str(i.posx) + ", " + str(i.posy))

                #If snake gets to the food, then it adds to the end of snake body.
                if head.tile.posx == food.tile.posx and head.tile.posy == food.tile.posy:
                        sx = body[(len(body)-1)].tile.posx
                        sy = body[(len(body)-1)].tile.posy
                        if head.direction == 1:
                                body.append(Snake(sx , (sy+10)))
                        if head.direction == 2:
                                body.append(Snake(sx , (sy-10)))
                        if head.direction == 3:
                                body.append(Snake((sx-10) , sy))
                        if head.direction == 4:
                                body.append(Snake((sx+10) , sy))
                        
                        everything.append()
   
                        food.generateFood(body)

                #Sets up the game rules. Cannot go outside the window and can't collide with itself
                if head.tile.posx < 0 or head.tile.posx >= 200 or head.tile.posy < 0 or head.tile.posy >= 200:
                        pygame.time.wait(500)
                        break
                        
                if hasCollided(body):
                        pygame.time.wait(500)
                        break
        
        if guiinit:
                gui.update(body, food)

    
    if guiinit:
        gui.exitGame()

        


        


if __name__ == "__main__":
    if sys.argv[1] == "gui":
        main(True)
    else:
        main(False)