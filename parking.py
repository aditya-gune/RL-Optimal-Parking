# -*- coding: utf-8 -*-
"""
Parking problem
"""

import numpy as np
from mdp import MDP
from collections import defaultdict

"""
R_coll = reward for collision
R_np = reward for not parked state
R_p = reward for parked state
R_handicap = reward for parking in handicapped spot
"""

class Parking_MDP(MDP):
    def __init__(self, rows, R_coll = -10000, R_np = -1, R_p = 10, R_handicap = -100):
        self.rows = rows
        self.n = 8 * rows + 1
        self.m = 3
        self.terminal = self.n - 1
        self.T=[]
        self.R  = np.zeros((self.n, 1))
        self.R[self.terminal] = self.n - 1
        self.stateinfo=defaultdict()
        self.stateproperties = defaultdict()
        i = 0
        for col in range(2):
            for row in range(rows):
                for occupied in range(2):
                    for parked in range(2):
                        self.stateinfo[i] = (col, row, occupied, parked)
                        self.stateproperties[(col, row, occupied, parked)] = i
                        
                        #parked
                        if parked == 1:
                            #parked in an occupied spot, causing collision
                            if occupied == 1:
                                self.R[i] = R_coll
                            #parked in handicapped spot
                            elif row == 0:
                                self.R[i] = R_handicap
                            #parked ok, get Reward * distance from store
                            else:
                                self.R[i] = R_p * (self.rows - row)
                        else:
                            self.R[i]=R_np
        for action in range(self.m):
            self.T.append(np.zeros((self.n,self.n)))
        
        for action in range(self.m):
            for col in range(2):
                for row in range(rows):
                    for occupied in range(2):
                        for parked in range(2):
                           