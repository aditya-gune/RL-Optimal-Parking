# -*- coding: utf-8 -*-
"""
ADITYA GUNE
Infinite Horizon Value Iteration
"""
import numpy as np
from mdp import MDP
import sys
from valueiter import *
from parking import Parking_MDP
from simulator import Simulator
from qlearning import Qlearning

#Set up environment
beta = 0.9
epsilon = 0.00001
numrows = 10

mdp = MDP()

#section = 1 FOR CREATING A PARKING MDP
#section = 2 FOR VALUE ITERATION
#sim = 1 FOR RUNNING A SIMULATION
#qlearn = 1 FOR QLEARNING 
section = 1
sim = 0
qlearn = 0

if section < 1 and sim < 1 and qlearn < 1:
    #exit()

if section == 1:
    parking_mdp = Parking_MDP(rows=numrows, R_handicap=-100, R_coll=-10000)
    parkingfile = open('ParkingMDP4.txt', 'w')
    (states, actions, T, R) = parking_mdp.getMDP()
    parking_mdp.writeMDP(parkingfile)
    parkingfile.close()

if section == 2:
    t = open('output.txt', 'w+')
    
    if len(sys.argv) > -1:
        k = mdp.read_MDP_from_file('ParkingMDP3.txt')
    else:
        print("No input file specified!")
        #exit()
        
    (states, actions, R, T) = mdp.process_MDP(k)
    
    (V, pi) = value_iter(states, actions, R, T, t, beta, epsilon)
    print("Optimal Value Function:")
    t.write("Optimal Value Function:\n")
    for x in V:
        print(x)
        t.write(str(x)+'\n')
    print
    t.write('\n')
    print("Optimal Policy:")
    t.write("Optimal Policy:\n")
    for x in pi:
        print(x)
        t.write(str(x)+'\n')
    t.close()

if sim == 1:
    simulator = Simulator((states, actions, R, T))
    (R_tot, actions_taken, states_visited) = simulator.runPolicy(pi)
    print("Reward: ", R_tot)
    print('Actions Taken: \n', actions_taken)
    print('States Visited: \n', states_visited)

R_avg = []

if qlearn == 1:
    for eps in [.1, .25, .33, .5, .66, .75, .99]:
        ql = Qlearning((states, actions, R, T), epsilon = eps)
        for trial in range(100):
            ql.learn()
        ra = 0
        for trial in range(1000):
            (R_tot, actions_taken, states_visited) = ql.run_iteration()
            ra =+ R_tot
        ra /= 1000
        print(ra)



