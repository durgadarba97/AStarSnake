# Handles all the logic of the game
from Snake import *
from A_star import *
from World import *
import sys

def main(guiinit):
    if guiinit:
        gui = GUI()

    food = Food()
    snake = Snake(50,50)


    aStar = A_star()

    tmppath = aStar.run(snake.body, food.tile)

    if tmppath is not None:
        path = tmppath
        path.pop()

    while True:
        if guiinit and not gui.handleQuit():
            break

        if len(path) == 0:
                tmppath = aStar.run(snake.body, food.tile)

                if tmppath is not None:
                        path = tmppath
                        path.pop()

        if tmppath is not None:
                lastelement = path.pop()

                if lastelement.posx > snake.head.posx:
                        snake.direction = 3
                elif lastelement.posx < snake.head.posx:
                        snake.direction = 4
                elif lastelement.posy > snake.head.posy:
                        snake.direction = 2
                elif lastelement.posy < snake.head.posy:
                        snake.direction = 1

                # for i in path:
                #         print(str(i.posx) + ", " + str(i.posy))

                
                #Handles key movement. Manual movement messes with the algorithm, so i commented it out.
                # keys = pygame.key.get_pressed()

                # if keys[pygame.K_UP] and snake.direction != 2:
                #         head.direction = 1
                # elif keys[pygame.K_DOWN] and snake.direction != 1:
                #         head.direction = 2
                # elif keys[pygame.K_RIGHT] and snake.direction != 4:
                #         head.direction = 3
                # elif keys[pygame.K_LEFT] and snake.direction != 3:
                #         head.direction = 4
                        
                # head.move(body)

                snake.move()

                for i in snake.body:
                        print(str(i.posx) + ", " + str(i.posy))

                #If snake gets to the food, then it adds to the end of snake body.
                if snake.head.posx == food.tile.posx and snake.head.posy == food.tile.posy:                    
                        snake.append()
                        food.generateFood(snake.body)

                #Sets up the game rules. Cannot go outside the window and can't collide with itself
                if snake.head.posx < 0 or snake.head.posx >= 200 or snake.head.posy < 0 or snake.head.posy >= 200:
                        pygame.time.wait(500)
                        break
                        
                if hasCollided(snake.body):
                        pygame.time.wait(500)
                        break
        
        if guiinit:
                gui.update(snake.body, food)

    
    if guiinit:
        gui.exitGame()

        
#Helper method for collision detection
def hasCollided(body):

        x = body[0].posx
        y = body[0].posy

        #Goes through the length of the snake to see if the head position matches the body position.
        #Not entirely a great way to do this. I want to reorginze this in the future.
        for i in range(1, len(body)-1):
                if body[i].posx == x and body[i].posy == y:
                        return True
        
        return False

        


if __name__ == "__main__":
    if sys.argv[1] == "gui":
        main(True)
    else:
        main(False)