# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 22:03:40 2022

@author: xpress_embedo
"""

import ltspy3

simulation_data = ltspy3.SimData('LowPassFilter.raw');
variable_names = simulation_data.variables;     # variable names from raw file
variable_count = simulation_data.novariables;   # number of variables from raw file
time_trace = simulation_data.values;            # transient simulation time & trace from raw file
time = simulation_data.values[0];               # first element is the time as a matrix
trace = simulation_data.values[1:3];            # includes the first but excludes the last, means only 1, and 2 index
