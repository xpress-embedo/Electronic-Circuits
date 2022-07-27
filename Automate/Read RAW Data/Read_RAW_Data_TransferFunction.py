# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 22:03:40 2022

@author: xpress_embedo
"""

import ltspy3

# Read RAW of Emitter Follower Transfer Function Schematic
simulation_data = ltspy3.SimData('TF_EmitterFollower.raw');
variable_TF = simulation_data.variables;            # variable names from raw file
variable_TF_count = simulation_data.novariables;    # number of variables from raw file
dc_TF = simulation_data.values;

# Read OP RAW (Operating Point RAW Data) of Emitter Follower Transfer Function Schematic
simulation_data_TF = ltspy3.SimData('TF_EmitterFollower.op.raw');
variable_OP = simulation_data_TF.variables;         # variable names from raw file
variable_OP_count = simulation_data_TF.novariables; # number of variables from raw file
dc_OP = simulation_data_TF.values;
