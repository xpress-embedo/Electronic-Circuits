# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 22:03:40 2022

@author: xpress_embedo
"""

# %% Read Low Pass Filter AC Analysis Schematic RAW Data
import ltspy3

filename = 'LowPassFilterACAnalysis';
sim_data = ltspy3.SimData(filename+'.raw');
var_names = sim_data.variables;         # variable names from raw file
var_count = sim_data.novariables;       # number of variables from raw file
freq_complex = sim_data.values;         # transient simulation time & trace from raw file
freq = sim_data.values[0];              # first element is the freq as a matrix
trace_complex = sim_data.values[1:3];   # includes the first but excludes the last, means only 1, and 2 index


# %% Converting RAW data in dB format
import numpy as np
# Convert magnitude to dB
trace_mag = np.absolute(trace_complex);
trace_mag_dB = 20*np.log10(trace_mag);
# find the angle of Vin and Vout
angle_deg = np.angle(trace_complex);    # Returns angle in degrees


# %% Plotting Data
import matplotlib.pyplot as plt
plt.figure()                            # New Figure
plt.subplot(211)                        # Magnitude in dB
plt.plot(freq, trace_mag_dB[0], 'ro-');
plt.plot(freq, trace_mag_dB[1], 'b^-');
plt.xscale('log');
plt.ylabel('Magnitude (dB)', fontsize=12, color='black');
plt.title('Bode Plot of ' + filename, fontsize=20);
plt.legend(['$V_{in}$', '$V_{out}$'], fontsize=15);
plt.grid(True)

plt.subplot(212)                        # Phase in degrees
plt.plot(freq, angle_deg[0], 'ro-');
plt.plot(freq, angle_deg[1], 'b^-');
plt.xscale('log');
plt.xlabel('Frequency (Hz)', fontsize=12, color='black');
plt.ylabel('Degrees ($^o$)', fontsize=12, color='black');
plt.grid(True)

plt.show()

# %% Saving Figures
# NOTE: Use %matplotlib qt in console to display graphs in separate window
# and to revert back use %matplotlib inline
plt.savefig('Bode Plot of '+filename+'.png', dpi=300);


# %% Close all Figures
plt.close('all');