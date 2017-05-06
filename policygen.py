# -*- coding: utf-8 -*-
"""
Policy Generator
"""

import numpy as np
from parking import Parking_MDP



def generate_selfish_driver(numrows):    #deterministically parks in an open spot
    mdp = Parking_MDP(rows=numrows, R_handicap=-100, R_coll=-10000)
    (states, actions, T, R) = mdp.getMDP()
    pi = []
    for i in range(states):
        if R[i] < -100:
            pi.append(1)
        else:
            pi.append(0)
    return pi

def generate_avoid_collisions(numrows, p):
    mdp = Parking_MDP(rows=numrows, R_handicap=-100, R_coll=-10000)
    (states, actions, T, R) = mdp.getMDP()
    pi = []
    parked = 0
    for i in range(states):
        if parked == 1:
            pi.append(2)
        else:
            if R[i] < 0:
                pi.append(1)
            else:
                if np.random.uniform() < p:
                    pi.append(0)
                    parked = 1
                else:
                    pi.append(1)
    return pi

def generate_random(numrows, p):
    mdp = Parking_MDP(rows=numrows, R_handicap=-100, R_coll=-10000)
    (states, actions, T, R) = mdp.getMDP()
    pi = []
    parked = 0
    for i in range(states):
        if parked == 1:
            pi.append(2)    #exit
        elif np.random.uniform() < p:
            pi.append(0)    #park
            parked = 1
        else:
            pi.append(1)    #drive
    return pi

def generate_policy(numrows,option=1, p = 0.5):
    if option == 1:
        return generate_random(numrows, p)
    elif option == 2:
        return generate_avoid_collisions(numrows, p)
    elif option==3:
        return generate_selfish_driver(numrows)