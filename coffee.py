#!/usr/bin/env python3

'''
This file produces the solution to the coffee problem whcih is really 
important to everyone.

To use this file....

This file solves Newton's law of cooling for coffee
'''
import numpy as np
import matplotlib.pyplot as plt


# Define constants for out problem
k=1/300 #coeff of cooling in units of 1/s
T_init, T_env= 90, 20 # initial and environmental temps in units of degree C

def solve_temp(time, k=1/300, T_init=T_init, T_env=T_env):
    '''
    Given an array of time in seconds, calculate the temp terture using 
    Newton's Law of Cooling.

    Returns 
    =======
    temps : numpy array
        An array of temperatures
    '''
    return T_env + (T_init-T_env)*np.exp(-k*time)
    
def time_to_temp(T_target, k=1/300, T_init=T_init, T_env=T_env)
    return (-1/k)*

#Set up time array
time = np.arange(0,600,1)        
# Get temperature for first scenario: no cream until 60 deg
temp_scn1 = solve_temp(time) #Temp vs time
time_scn1 = time_to_temp(60.0) #Time to reach 60C from T_init

#Repeat for scenario 2: add cream immediately
temp_scn2 = solve_temp(time) #Temp vs time
time_scn2 = time_to_temp(60.0) #Time to reach 60C from T_init

# Plot
fig,ax=plt.subplots(1,1)

#Add temp vs. time
ax.plot(time, temp_scn1, label='Scenario 1')
ax.plot(time, temp_scn2, label='Scenario 2')

# Add vert lines:
ax.axvline(time_scn1, ls='--', c='C0', label=r'$t(T=60^{\circ}$)')
ax.axvline(time_scn2, ls='--', c='C1', label=r'$t(T=60^{\circ}$)')