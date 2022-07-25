# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 22:03:40 2022

@author: xpress_embedo
"""

import ltspy3

simulation_data = ltspy3.SimData('LowPassFilterACAnalysis.raw');
variable_names = simulation_data.variables;     # variable names from raw file
variable_count = simulation_data.novariables;   # number of variables from raw file
freq_complex = simulation_data.values;
freq = simulation_data.values[0];
trace_complex = simulation_data.values[1:3];
