# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 22:03:40 2022

@author: xpress_embedo
"""

import ltspy3

simulation_data = ltspy3.SimData('DCSweepTemperature.raw');
variable_names = simulation_data.variables;     # variable names from raw file
variable_count = simulation_data.novariables;   # number of variables from raw file
dc_op_sweep = simulation_data.values;
step_variable = simulation_data.stepvariables;
step_values = simulation_data.stepvalues;
