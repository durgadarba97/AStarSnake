from Snake import *
import pygame
import math

class A_star:
    def __init__(self):
        self.closedSet = []
        self.openSet = []
    

    def run(self, wall, goal):

        start = wall[0].tile
        self.closedSet = []
        self.openSet = [start]
        path = []

        while self.openSet:
            #Set current to node in openSet with lowest fscore
            current = self.openSet[0]
            currindex = 0
            for i, node in enumerate(self.openSet):
                if node.fScore < current.fScore:
                    current = node
                    currindex = i

            #romove from Open set and add to closed
            self.openSet.pop(currindex)
            self.closedSet.append(current)

            #Reached the end        
            if current.tileEquals(goal):
                print("Done")
                while current is not None:
                    path.append(current)
                    current = current.cameFrom
                return path
            
            neighbors = self.giveNeighbors(current)

##            print("Current: " + str(current.posx) + ", " + str(current.posy))
            
            for i in neighbors:
                #if neighbor is already checked, then ignore it. Also, cannot collide with itself.
                if not self.contains(self.closedSet, i) and not self.inBody(wall, i):
                    #Distance between start adn neighbor. tenative gscore
                    tempGScore = current.gScore + 1

                    #if neighbor is not in openset. Discovered a new node!
                    if not self.contains(self.openSet, i):
                        self.openSet.append(i)
                        i.gScore = tempGScore
                    elif tempGScore <= i.gScore:
                        continue
                    
                    i.gScore = tempGScore
                    i.cameFrom = current
                    i.fScore = i.gScore + self.heuristicCost(i, goal) #f = g + h

##            print("Open:")
##            for i in self.openSet:
##                print(str(i.posx) + ", " + str(i.posy))
##            print("Closed")
##            for i in self.closedSet:
##                print(str(i.posx) + ", " + str(i.posy))


    #Calculates the estimated distance from a given tile to end
    def heuristicCost(self, neighbor, goal):
        #The snake never goes diagonal, therefore calculate manhatten distance
        distance = abs(neighbor.posx - goal.posx) + abs(neighbor.posy - goal.posy)
        return distance

    def giveNeighbors(self, current):
        neighbors = []
        if current.posx > 0:
            neighbors.append(Tile(current.posx - 10, current.posy))
        if current.posx <= 180:
            neighbors.append(Tile(current.posx + 10, current.posy))
        if current.posy > 0:
            neighbors.append(Tile(current.posx, current.posy - 10))
        if current.posy <= 180:
            neighbors.append(Tile(current.posx, current.posy + 10))

        return neighbors

    def contains(self, s, tile):
        for i in s:
            if i.tileEquals(tile):
                return True          
        return False

    def inBody(self, s, t):
        for i in s:
            if i.tile.tileEquals(t):
                return True      
        return False




def ygradient(grid, body):
    i = 0
    while i < len(body):
        x = int(body[i].posx / 10)
        row = grid[x]
        above = []
        below = []
        
        for j in row:
            if j.posy <= body[i].posy:
                above.append(j)

            if j.posy >= body[i].posy:
                below.append(j)

        for j in below:
            jposx = int(j.posx / 10)
            jposy = int(j.posy / 10)
            prevy = grid[jposx][jposy - 1].yweight
            
            if j.yweight != 1:
                grid[jposx][jposy].yweight = (prevy - grid[jposx][jposy].yweight) / 4

        for j in above[::-1]:
            jposx = int(j.posx / 10)
            jposy = int(j.posy / 10)
            prevy = grid[jposx][jposy + 1].yweight
            
            if j.yweight != 1:
                grid[jposx][jposy].yweight = (prevy - grid[jposx][jposy].yweight) / 4          
        
        i+=1
        
def xgradient(grid, body):
    i = 0
    while i < len(body):
        y = int(body[i].posy / 10)
        row = [j[y] for j in grid]
        right = []
        left = []

        for j in row:
            if j.posx <= body[i].posx:
                left.append(j)

            if j.posx >= body[i].posx:
                right.append(j)

        for j in right:
            jposx = int(j.posx / 10)
            jposy = int(j.posy / 10)
            prevx = grid[jposx - 1][jposy].xweight
            
            if j.xweight != 1:
                grid[jposx][jposy].xweight = (grid[jposx][jposy].xweight - prevx) / 4

        for j in left[::-1]:
            jposx = int(j.posx / 10)
            jposy = int(j.posy / 10)
            prevx = grid[jposx + 1][jposy].xweight
            
            if j.xweight != 1:
                grid[jposx][jposy].xweight = (grid[jposx][jposy].xweight - prevx) / 4

        i+=1

##        for j in row:
##            print(str(j.posx) + " " + str(j.posy) + " " + str(j.xweight))

def magnitude(grid):
    for i in grid:
        for j in i:
            j.weight = math.sqrt(abs(j.xweight)**2 + abs(j.yweight)**2)


def testAStar():

        pygame.init()
        window = pygame.display.set_mode((200, 200))
        pygame.display.set_caption("Test")
        window.fill((255,255,255))
        pygame.font.init()
        myfont = pygame.font.SysFont('Times', 20)


        grid = [[Tile(i*10, j*10) for j in range(20)] for i in range(20)]
                
        body = [grid[1][1],
            grid[1][2],
            grid[1][3],
            grid[2][3],
            grid[2][4],
            grid[2][5],
            grid[2][6],
            grid[3][6],
            grid[3][7],
            grid[4][7],
            grid[4][8],
            grid[5][8],
            grid[6][8],
            grid[7][8],
            grid[8][8],
            grid[8][7],
            grid[8][6],
            grid[8][5],
            grid[8][4],
            grid[8][3]]

        for i in body:
            i.weight = 1.0
            i.xweight = 1.0
            i.yweight = 1.0

        ygradient(grid, body)
        xgradient(grid, body)
        magnitude(grid)
        
        clock = pygame.time.Clock()
        run = True
        while run:
            for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run = False

            for i in body:
                pygame.draw.rect(window, (80,80,80), (i.posx, i.posy, 10, 10))

            for i in grid:
                for j in i:
                    x = j.posx
                    y = j.posy

                    print(str(j.weight))

                    if j.weight != 0 or j.weight != 1:
                        pygame.draw.rect(window, (abs(255 - (255 * (j.weight))) , 0, 255), (x, y, 10, 10))

                    textsurface = myfont.render(str(j.comment), False, (0, 0, 0))
                    window.blit(textsurface,(x,y))                    


                
            pygame.display.update()
            window.fill((255,255,255))               
            clock.tick(10)

        pygame.quit()


if __name__ == "__main__":
    testAStar()
            
        
    
        
    
