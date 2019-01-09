import random

#Sets up the snake class
class Snake:
    def __init__(self, x, y):
        self.width = 10
        self.height = 10
        self.tile = Tile(x,y)
        self.direction = 2

    #Moves the snake by going in reverse and setting the last element to the element in front of it
    def move(self, body):
        for i in range(len(body)-1, 0, -1):
            body[i].tile.posx = body[i-1].tile.posx
            body[i].tile.posy = body[i-1].tile.posy

        if self.direction == 1:
            body[0].tile.nextTileUp()
        if self.direction == 2:
            body[0].tile.nextTileDown()
        if self.direction == 3:
            body[0].tile.nextTileRight()
        if self.direction == 4:
            body[0].tile.nextTileLeft() 
            

#Sets up food class
class Food:
    def __init__(self):
        self.tile = Tile(100, 100)

    #Generates food at a random point 
    def generateFood(self):
        self.tile.posx = (random.randint(0, 19)) * 10
        self.tile.posy = (random.randint(0, 19)) * 10
        

#Tile class to handle points.
#This class is inefficient and not used as well as intended.
#In the future, I want to set up a grid layout that has tiles.
#This is so that main gameloop doesn't need to handle pixels but can just focus on the logic
#and let the backend supporting classes handle that. Still works though!
class Tile:
        def __init__(self, x, y):
                self.posx = x
                self.posy = y
                self.fScore = 0
                self.gScore = 0
                self.cameFrom = None
                self.xweight = 0
                self.yweight = 0
                self.weight = 0

                self.comment = " "
                
        def nextTileRight(self):
                self.posx = self.posx + 10

        def nextTileDown(self):
                self.posy = self.posy + 10
		
        def nextTileUp(self):
                self.posy = self.posy - 10
                
        def nextTileLeft(self):
                self.posx = self.posx - 10

        def tileEquals(self, t):
                if self.posx == t.posx and self.posy == t.posy:
                    return True
                else:
                    return False

        
        
        
        
	
