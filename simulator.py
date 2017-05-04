# -*- coding: utf-8 -*-
"""
Created on Thu May 04 11:24:13 2017

@author: Aditya
"""
import numpy as np

class Simulator:
    def __init__(self, mdp):
        self.mdp = mdp
        self.s_0 = 0
        self.current = self.s_0
        self.R_tot = 0
        self.actions_taken = []
        self.states_visited = []
        self.terminal = False
        
        
    def runPolicy(self, policy):
        (states, actions, R, T) = self.mdp.get_MDP()
        while not self.terminal:
            current = self.current
            self.states_visited.append(current)
            self.R_tot += R[current]
            self.take_action(policy[current])
            self.actions_taken.append(policy[current])
        return (self.R_tot, self.actions_taken, self.states_visited)
    
    def take_action(self, action):
        if self.terminal:return
        (states, actions, R, T) = self.mdp.get_MDP()
        
        tarray = np.array(states)
        tvals = T[self.current][action]
        
        if np.sum(tvals) > 0:
            distribution = np.add.accumulate(tvals)
            randnum = np.random.random_sample(1)
            index = min(distribution, key=lambda x:abs(x-randnum))
            s_next = tarray[index]
            self.current = s_next
        
            self.terminal = True
            for action in range(actions):
                tvals = T[self.current][action]
                if np.sum(tvals) > 0:
                    self.terminal = False
                    break
            
        
        
        
            