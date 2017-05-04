# -*- coding: utf-8 -*-
"""
Misc Functions
"""
import numpy as np
from mdp import MDP
import sys

def value_iter(states, actions, R, T, t, beta, epsilon):
    #VALUE ITERATION STARTS HERE
    V = np.zeros(states)
    Vp = np.zeros(states)
    pi = np.zeros(states)
    temparray = []
    itr = 0
    #do value iteration
    for itr in range(100000):
    
        for j in range(states):
            E = [np.dot(T[k][j:], Vp) for k in range(actions)] #Get expectation
            V[j] = float(R[j]) + beta * np.max(E)   #Get V*
        norm = np.linalg.norm(V - Vp,ord=np.inf)    #use Bellman eqn norm for stopping condition
        if norm <= epsilon : break
        Vp = np.array(V)
        
    for j in range(states):
        E = [np.dot(T[k][j:], V) for k in range(actions)] 
        temparray.append(np.argmax(E, axis=0))
    
    pi = [int(x) for x in temparray[0]]
    return (V, pi)