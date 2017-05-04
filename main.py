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


beta = 0.9
epsilon = 0.00001

mdp = MDP()

numrows = 10

#parking_mdp = Parking_MDP(rows=numrows, R_handicap=-100, R_coll=-10000)
#parkingfile = open('ParkingMDP2.txt', 'w')
#(states, actions, T, R) = parking_mdp.getMDP()
#parking_mdp.writeMDP(parkingfile)

if len(sys.argv) > -1:
    k = mdp.read_MDP_from_file('ParkingMDP2.txt')
else:
    print("No input file specified!")
    #exit()
    
(states, actions, R, T) = mdp.process_MDP(k)


t = open('output.txt', 'w+')

(V, pi) = value_iter(states, actions, R, T, t, beta, epsilon)


##print("Optimal Value Function:")
#t.write("Optimal Value Function:\n")
#for x in V:
#   # print(x)
#    t.write(str(x)+'\n')
#print
#t.write('\n')
##print("Optimal Policy:")
#t.write("Optimal Policy:\n")
#for x in pi:
#  #  print(x)
#    t.write(str(x)+'\n')
#parkingfile.close()
t.close()