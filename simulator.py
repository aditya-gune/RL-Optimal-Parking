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
        return self.R_tot
    
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
        #print("taking action...")
        if self.terminal:
            #print("terminal state, returning...")
            return
        
        tarray = np.array(range(self.states))
        tvals = self.T[action][current]
        print("tval indices = ", action, current)
        
#        if np.sum(tvals) == 0:
#            print("Sum(tvals) = ", np.sum(tvals),", returning...")
#            return

        distribution = np.add.accumulate(tvals)
        print("dist ", distribution)
        randnum = np.random.random_sample(1)
        print("randnum = ", randnum)
        index = np.digitize(randnum, distribution)[0]
        print("index = ",index)
        s_next = tarray[index-1]
        self.current = s_next
        
        self.terminal = True
        for action in range(self.actions):
            print("current = ", current)
            tvals = self.T[action][current]
            if np.sum(tvals) > 0:
                self.terminal = False
                break
        print('action terminal')
        
        
        
            