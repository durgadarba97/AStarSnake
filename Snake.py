import random

#Sets up the snake class
class Snake:
    def __init__(self, x, y):
        self.width = 10
        self.height = 10
        self.head = Tile(x,y)
        self.body = self.createBody()
        self.direction = 2
    
    # helper method to create body
    def createBody(self):
        b = [self.head]
        b.append(Tile(self.head.posx - 10, self.head.posy))
        b.append(Tile(self.head.posx - 20, self.head.posy))
        b.append(Tile(self.head.posx - 30, self.head.posy))
        return b
    
    # helper method to get head x
    def headx(self):
        return self.body[0].x()

    # helper moethd to get head y
    def heady(self):
        return self.body[0].y()

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
    # appends new tile to the end of the snake
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
    
    def x(self):
        return self.tile.x()
    
    def y(self):
        return self.tile.y()

    #Generates food at a random point 
    def generateFood(self, body):
        f = self.genfoodHelper(body)
        self.tile.posx = f[0]
        self.tile.posy = f[1]

    # recursive method to generate food that doesn't land on the snake
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
class Tile:
        def __init__(self, x, y):
            self.posx = x
            self.posy = y
            self.fScore = 0
            self.gScore = 0
            self.cameFrom = None

            self.width = 10
            self.height = 10

        def x(self):
            return self.posx
        
        def y(self):
            return self.posy 
                
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

        
        
        
        
	
