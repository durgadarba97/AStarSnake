import random

#Sets up the snake class
# TODO Snake is not just the head. Include body list in class.
class Snake:
    def __init__(self, x, y):
        self.width = 10
        self.height = 10
        self.head = Tile(x,y)

        self.body = self.createBody()

        self.direction = 2
    
    def createBody(self):
        b = [self.head]
        b.append(Tile(self.head.posx - 10, self.head.posy))
        b.append(Tile(self.head.posx - 20, self.head.posy))
        b.append(Tile(self.head.posx - 30, self.head.posy))
        return b

    #Moves the snake by going in reverse and setting the last element to the element in front of it
    def move(self):
        for i in range(len(self.body)-1, 0, -1):
            self.body[i].posx = self.body[i-1].posx
            self.body[i].posy = self.body[i-1].posy

        if self.direction == 1:
            self.body[0].nextTileUp()
        if self.direction == 2:
            self.body[0].nextTileDown()
        if self.direction == 3:
            self.body[0].nextTileRight()
        if self.direction == 4:
            self.body[0].nextTileLeft()       
    
    #Don't know if this is a huge issue, but the snake can be appended off screen.
    def append(self):
        sx = self.body[(len(self.body)-1)].posx
        sy = self.body[(len(self.body)-1)].posy

        if self.direction == 1:
                self.body.append(Tile(sx , (sy+10)))
        if self.direction == 2:
                self.body.append(Tile(sx , (sy-10)))
        if self.direction == 3:
                self.body.append(Tile((sx-10) , sy))
        if self.direction == 4:
                self.body.append(Tile((sx+10) , sy))
    
            

#Sets up food class
class Food:
    def __init__(self):
        self.tile = Tile(100, 100)
        self.x = self.tile.posx
        self.y = self.tile.posy

    #Generates food at a random point 
    def generateFood(self, body):
        f = self.genfoodHelper(body)
        self.tile.posx = f[0]
        self.tile.posy = f[1]

    def genfoodHelper(self, body):
        x = (random.randint(0, 19)) * 10
        y = (random.randint(0, 19)) * 10
        recur = (x, y)

        print("FOOD position: " + str(x) + ", " + str(y))
        for i in body:
            if i.posx == x  and i.posy == y:
                recur = self.genfoodHelper(body)
        
        return recur

        

#Tile class to handle points.
#This class is inefficient and not used as well as intended.
#In the future, I want to set up a grid layout that has tiles.
#This is so that main gameloop doesn't need to handle pixels but can just focus on the logic
#and let the backend supporting classes handle that. Still works though!

# TODO make posx and posy a tuple.
class Tile:
        def __init__(self, x, y):
                self.posx = x
                self.posy = y
                self.fScore = 0
                self.gScore = 0
                self.cameFrom = None


                self.comment = " "

                self.width = 10
                self.height = 10
                
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

        
        
        
        
	
