from Snake import *
import pygame

class A_star:
    def __init__(self):
        self.closedSet = []
        self.openSet = []
    

    def run(self, body, goal):

        start = body[0].snaketile
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
##            
##            print("Neighbors")
##            for i in neighbors:
##                print(str(i.posx) + ", " + str(i.posy))
##
##            print("Open before:")
##            for i in self.openSet:
##                print(str(i.posx) + ", " + str(i.posy))
##            print("Closed before")
##            for i in self.closedSet:
##                print(str(i.posx) + ", " + str(i.posy))
            
            for i in neighbors:
                #if neighbor is already checked, then ignore it. Also, cannot collide with itself.
                if not self.contains(self.closedSet, i) and not self.inBody(body, i):
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
##                    print(str(i.cameFrom.posx) + ", " + str(i.cameFrom.posy))

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
        if current.posx < 200:
            neighbors.append(Tile(current.posx + 10, current.posy))
        if current.posy > 0:
            neighbors.append(Tile(current.posx, current.posy - 10))
        if current.posy < 200:
            neighbors.append(Tile(current.posx, current.posy + 10))

        return neighbors

    def contains(self, s, tile):
        for i in s:
            if i.tileEquals(tile):
                return True          
        return False

    def inBody(self, s, tile):
        for i in s:
            if i.snaketile.tileEquals(tile):
                return True      
        return False
            

def testAStar():
    pygame.init()
    window = pygame.display.set_mode((200, 200))
    pygame.display.set_caption("AStar Test")
    window.fill((255,255,255))
    clock = pygame.time.Clock()

    start = Tile(0, 0)
    end = Tile(40, 40)

    astar = A_star()
    path = astar.run(start, end)

    for i in path:
        print(str(i.posx) + ", " + str(i.posy))

    run = True
    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.draw.rect(window, (0, 255, 0), (start.posx, start.posy, 10, 10))
        pygame.draw.rect(window, (255, 0, 0), (end.posx, end.posy, 10, 10))

            
        for i in path:
            pygame.draw.rect(window, (0, 0, 255), (i.posx, i.posy, 10, 10))

##        for i in astar.openSet:
##            pygame.draw.rect(window, (255, 0, 255), (i.posx, i.posy, 10, 10))
##            pygame.display.update()
##        for i in astar.closedSet:
##            pygame.draw.rect(window, (0, 0, 0), (i.posx, i.posy, 10, 10))
##            pygame.display.update()

        print("drew stuff")
            
        pygame.display.update()
        window.fill((255,255,255))
        clock.tick(10)

    pygame.quit()


if __name__== "__main__":
        testAStar()
        
    
        
    
