# -*- coding: utf-8 -*-
"""
ADITYA GUNE
Infinite Horizon Value Iteration
"""
import numpy as np
from mdp import MDP
import sys
from valueiter import *

mdp = MDP()
if len(sys.argv) > 1:
    k = mdp.read_MDP_from_file(sys.argv[1])
else:
    print("No input file specified!")
    exit()
(states, actions, R, T) = mdp.process_MDP(k)
t = open('output.txt', 'w+')



beta = 0.1
epsilon = 0.00001
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