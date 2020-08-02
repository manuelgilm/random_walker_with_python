import argparse
import numpy as np 
import matplotlib.pyplot as plt

class Walker:    
    '''Represents a random walker.
    
        With this class it is possible to graph one or more random walkers
         using matplotlib for this.
    '''
    
    def __init__(self):
        self.x = 0
        self.y = 0        
        self.directions = {0:'left', 1:'right', 2:'up', 3:'down'}
        self.x_pass = [self.x]
        self.y_pass = [self.y]
        
    def walker_pass(self): 
        self.move(self.directions[np.random.choice(4,1)[0]])        
        self.x_pass.append(self.x)
        self.y_pass.append(self.y)
        
    def move(self,d):
        
        if d == 'left':
            self.x -= 1
        elif d == 'right':
            self.x += 1
        elif d == 'up':
            self.y += 1
        else:
            self.y -= 1
            
    def run_walk(self,steps):
        for step in range(steps):
            self.walker_pass()
            print(self.x, self.y)            

    def create_graph(self,color):
        plt.plot(self.x_pass, self.y_pass,'-', color=color)
        
    def show_walkers(self):
        plt.show()