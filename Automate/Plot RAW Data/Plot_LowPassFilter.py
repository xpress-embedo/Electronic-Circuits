# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 22:03:40 2022

@author: xpress_embedo
"""

# %% Read Low Pass Filter Schematic RAW Data
import ltspy3

filename = 'LowPassFilter';
sim_data = ltspy3.SimData(filename+'.raw');
var_names = sim_data.variables;         # variable names from raw file
var_count = sim_data.novariables;       # number of variables from raw file
time_trace = sim_data.values;           # transient simulation time & trace from raw file
time = sim_data.values[0];              # first element is the time as a matrix
trace = sim_data.values[1:3];           # includes the first but excludes the last, means only 1, and 2 index


# %% Plotting Data
import matplotlib.pyplot as plt
plt.figure()                            # New Figure
plt.plot(time, trace[0], 'ro-');
plt.plot(time, trace[1], 'b^-');
plt.xlabel('Time (sec)',  fontsize=12, color='black');
plt.ylabel('Voltage (V)', fontsize=12, color='black');
plt.title(filename, fontsize=20);
plt.legend(['$V_{in}$', '$V_{out}$'], fontsize=15);
plt.grid(True)
plt.show()

# %% Saving Figures
# NOTE: Use %matplotlib qt in console to display graphs in separate window
# and to revert back use %matplotlib inline
plt.savefig(filename+'byPython.png', dpi=300);


# %% Close all Figures
plt.close('all');