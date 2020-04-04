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
                 
                print(len(path))
                if len(path) == 0:
                    spot = self.genNewSpot(wall)
                    path = self.run(spot, goal)


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

            # print("Open:")
            # for i in self.openSet:
            #     print(str(i.posx) + ", " + str(i.posy))
            # print("Closed")
            # for i in self.closedSet:
            #     print(str(i.posx) + ", " + str(i.posy))


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


    def genNewSpot(self, body):
        x = (random.randint(0, 19)) * 10
        y = (random.randint(0, 19)) * 10
        recur = (x, y)

        print("FOOD position: " + str(x) + ", " + str(y))
        for i in body:
            if i.tile.posx == x  and i.tile.posy == y:
                recur = self.genNewSpot(body)
        
        return recur


            
        
    
        
    
