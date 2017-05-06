# -*- coding: utf-8 -*-
"""
Created on Thu May 04 11:13:08 2017

@author: Aditya
"""
import numpy as np
from simulator import Simulator
import random as r
class Qlearning:
    def __init__(self, mdp_Tuple: tuple, s_0 = 0, epsilon =0.1, alpha = 0.01):
        self.simulator = Simulator(mdp_Tuple)
        self.s_0 = 0
        
        self.states = mdp_Tuple[0]
        self.actions = mdp_Tuple[1]
        self.R = mdp_Tuple[2]
        self.T = mdp_Tuple[3]   
        
        
        self.q_table = np.zeros((self.states, self.actions))
        self.iterations = 0
        self.alpha = alpha
        self.beta = 0.5
        
        self.epsilon = epsilon
        
    def run_iteration(self):
        R_tot = 0
        actions_taken = []
        states_visited = []
        
        itr = 0
        
        terminal = False
        while not terminal and itr < 100:
            current = self.simulator.get_current()
            states_visited.append(current)
            
            R_tot += self.simulator.get_R()
            action = self.explore_exploit()#np.argmax(self.q_table[current][:])
            actions_taken.append(action)
            
            self.simulator.take_action(action)
            
            itr+=1
            
        return (R_tot, actions_taken, states_visited)
    
    def learn(self):
        actions_taken = []
        states_visited = []
        R_vals = []
        itr = 0
        
        terminal = False
        while not terminal and itr < 100:
            current = self.simulator.get_current()
            states_visited.append(current)
            
            R_vals.append(self.simulator.get_R())
            action = self.explore_exploit()#np.argmax(self.q_table[current:])
            actions_taken.append(action)
            
            self.simulator.take_action(action)
            
            itr+=1
            
        states_visited.append(self.simulator.get_current())
        R_vals.append(self.simulator.get_R())
        self.update(actions_taken, states_visited, R_vals)
    
    #greedy in the limit of exploration
    def explore_exploit(self):
        if self.iterations == 0 or r.uniform(0, 1) <= self.epsilon:
            n = self.q_table.shape[1]
            return r.randint(0, n-1)
        else:
            return np.argmax(self.q_table[self.current:])
   
    def _update(self, s, a, ns, r):
        m = self.q_table.shape[1]
        V = self.q_table[s][a]
        E_star = np.max([self.q_table[ns][i] for i in range(m)])
        V_opt = r + self.beta * E_star
        update = self.alpha * (V_opt - V)
        V += update
        return V
            
    def update(self, actions_taken, states_visited, R_vals):
        for i in range(len(actions_taken)-1, 0, -1):
            s = states_visited[i]
            a = actions_taken[i]
            r = R_vals[i]
            ns = states_visited[i+1]
            self.q_table[s][a] = self._update(s, a, ns, r)