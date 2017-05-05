# -*- coding: utf-8 -*-
"""
Simulator for Parking
"""
import numpy as np

class Simulator:
    def __init__(self, mdp_Tuple:tuple):
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
        
    def runPolicy(self, policy):
        #(states, actions, R, T) = self.get_MDP()
        while not self.terminal:
            current = self.current
            self.states_visited.append(current)
            self.R_tot += float(self.R[current])
            self.take_action(policy[current])
            self.actions_taken.append(policy[current])
        return (self.R_tot, self.actions_taken, self.states_visited)
    
    def take_action(self, action):
        if self.terminal:return
        #(states, actions, R, T) = self.get_MDP()
        
        tarray = np.array(self.states)
        tvals = self.T[self.current][action]
        
        if np.sum(tvals) > 0:
            distribution = np.add.accumulate(tvals)
            randnum = np.random.random_sample(1)
            index = min(distribution, key=lambda x:abs(x-randnum))
            s_next = tarray[index]
            self.current = s_next
        
            self.terminal = True
            for action in range(self.actions):
                tvals = self.T[self.current][action]
                if np.sum(tvals) > 0:
                    self.terminal = False
                    break
            print('action terminal')
        
        
        
            