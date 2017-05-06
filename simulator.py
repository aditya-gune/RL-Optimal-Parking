# -*- coding: utf-8 -*-
"""
Simulator for Parking
"""
import numpy as np

class Simulator:
    def __init__(self, mdp_Tuple: tuple):
        self.s_0 = 0
        self.current = self.s_0
        self.R_tot = 0
        self.actions_taken = []
        self.states_visited = []
        self.terminal = False
        self.states = mdp_Tuple[0]
        self.actions = mdp_Tuple[1]
        self.R = mdp_Tuple[2]
        self.T = mdp_Tuple[3]        
    
    def get_current(self):
        return self.current
    
    def get_R(self):
        return float(self.R[self.current])
    
    def runPolicy(self, policy):
        while not self.terminal:
            current = int(self.current)
            self.states_visited.append(current)
            self.R_tot += float(self.R[current])
            self.take_action(policy[current])
            self.actions_taken.append(policy[current])
        return (self.R_tot, self.actions_taken, self.states_visited)
    
    def take_action(self, action):
        current = int(self.current)
        
        if self.terminal:
            return
        
        tarray = np.array(range(self.states))
        tvals = self.T[action][current]

        distribution = np.add.accumulate(tvals)
        randnum = np.random.random_sample(1)
        index = np.digitize(randnum, distribution)[0]
        if index < self.states-2:
            s_next = tarray[index]
            self.current = s_next
        else:
            self.terminal = True
            return
        
        
        self.terminal = True
        for action in range(self.actions):
            tvals = self.T[action][current]
            if np.sum(tvals) > 0 and self.current < self.states-2:
                self.terminal = False
                break
        
        
        
            