# -*- coding: utf-8 -*-
"""
Created on Thu May 04 11:24:13 2017

@author: Aditya
"""

class Simulator:
    def __init__(self, mdp):
        self.mdp = mdp
        self.s_0 = 0
        self.current = self.s_0
        self.R_tot = 0
        self.actions_taken = []
        self.states_visited = []
        self.terminal = False
        
    def runPolicy(self, mdp, policy):
        (states, actions, R, T) = mdp.get_MDP()
        while not self.terminal:
            current = self.current
            self.states_visited.append(current)
            self.R_tot += R[current]
            take_action(policy[current])
            self.actions_taken.append(policy[current])
        return (self.R_tot, self.actions_taken, self.states_visited)
    
    
            