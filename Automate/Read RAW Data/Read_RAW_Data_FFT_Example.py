# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 22:03:40 2022

@author: xpress_embedo
"""

import ltspy3

# Read RAW Data
simulation_data = ltspy3.SimData('FFT_Example.raw');
variable = simulation_data.variables;            # variable names from raw file
variable_count = simulation_data.novariables;    # number of variables from raw file
values = simulation_data.values;

# Read FFT Data
simulation_data_FFT = ltspy3.SimData('FFT_Example.fft');
variable_fft = simulation_data_FFT.variables;         # variable names from raw file
variable_fft_count = simulation_data_FFT.novariables; # number of variables from raw file
value_FFT = simulation_data_FFT.values;
