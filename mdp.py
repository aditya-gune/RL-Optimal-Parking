# -*- coding: utf-8 -*-
"""
ADITYA GUNE
MDP Class for Infinite Horiz. Value Iteration
"""

import numpy as np
import re

class MDP:
    
    def __init__(self):
        self.newMDP()
    
    def newMDP(self):
        self.n = 0
        self.m = 0
        self.T = []
        self.R = []
        
    def read_MDP_from_file(self, file):
        self.newMDP()
        matrix = []
        fn = file
        with open(fn) as f:
            for l in f:
                l = l.strip()
                l = re.findall(r"[-+]?\d*\.\d+|\d+", l)
                matrix.append(l)
        return matrix
    
    def process_MDP(self, matrix):
        l = matrix
        tempAction = []
        self.n = int(l[0][0])
        self.m = int(l[0][1])
        self.R = l[-1]
        del l[0]
        del l[-1]
        for item in l:
            if item != []:
                ti = []
                for i in item:
                    i = float(i)
                    ti.append(i)
                tempAction.append(ti)
            else:
                self.T.append(tempAction)
                tempAction = []
        del l
        del self.T[0]
        self.R = np.array(self.R)
        return (self.n, self.m, self.R, self.T)
    
    def tval(self, state, action):
        return self.T[action][state:]