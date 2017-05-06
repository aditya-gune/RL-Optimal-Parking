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
    def __init__(self, rows, R_coll = -10000, R_np = 0, R_p = 10, R_handicap = -100):
        self.rows = rows
        self.n = 8 * rows + 1
        self.m = 3  #0 = park, 1 = drive, 2 = exit
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
                        i += 1
        for action in range(self.m):
            self.T.append(np.zeros((self.n,self.n)))
        
        
        
        for action in range(self.m):
            for col in range(2):
                for row in range(rows):
                    for occupied in range(2):
                        for parked in range(2):
                            current = self.stateproperties[(col, row, occupied, parked)]
                            #print(current)
                            if action == 0: #park
                                if parked == 0:
                                    s_next = self.stateproperties[(col, row, occupied, 1)]
                                    self.T[action][current, s_next] = 1
                                else:
                                    s_next = self.terminal
                                    self.T[action][current, s_next] = 1
                                    
                            if action == 1: #drive
                                if parked == 0:
                                    if col == 0 and row == 0:
                                        col_next = 1
                                        row_next = 0
                                    elif col == 0  and row > 0:
                                        col_next = col
                                        row_next = row
                                    elif col == 1 and row == self.rows -1:
                                        col_next = 1
                                        row_next = row
                                    elif col == 1:
                                        col_next = col
                                        row_next = row
                                    
                                    s_1 = self.stateproperties[(col_next, row_next, 0, parked)]
                                    s_2 = self.stateproperties[(col_next, row_next, 1, parked)]
                                    if row == 0:
                                        spot_occupied = 0.001
                                    else:
                                        spot_occupied = (self.rows - row)/self.rows
                                        
                                    self.T[action][current, s_1]= 1 - spot_occupied
                                    self.T[action][current, s_2] = spot_occupied
                                    
                            if action == 2: #exit
                                if parked == 1:
                                    s_next = self.terminal
                                    self.T[action][current, s_next] = 1
    def getMDP(self):
        return(self.n, self.m, self.T, self.R)
    
    def getstateinfo(self, state):
        try:
            (c, r, o, p) = self.stateinfo[state]
            return (c, r, o, p)
        except KeyError:
            print("Terminal state!")
            return (-1,-1,-1,-1)
       
    
    def writeMDP(self, t):
        str0 = str(self.n) + ' ' + str(self.m)
        t.write(str0)
        t.write('\n')
        for i in self.T:
            t.write('\n')
            #str1 = ''
            for j in i:
                str1 = ''
                for k in j:
                    str1 = str1 + str(k)+'\t'
                str1 += '\n'
                t.write(str1)
                #print(len(str1))
            t.write('\n')
        str2=''
        for i in self.R:
            str2 = str2 + str(float(i[0]))+'\t'
        t.write(str2)