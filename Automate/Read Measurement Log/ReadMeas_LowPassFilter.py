# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 22:03:40 2022

@author: xpress_embedo
"""

# %% Read Measurement from log data file
import ltspy3meas
# User input: meas names are given as below
meas_list = ['vout_avg','vout_max','vout_min','vout_at_time','vout_dev','vout2','vout2x'] # last two are incorrect names


# %% print the log file
file_name = 'LowPassFilter_Meas'
log = ltspy3meas.LogGetClass(file_name +'.log', meas_list)
log.log_print()

# %% read measurement and flag
# Input: file names and measurement names
# Output1: measurment in a row in NumPy array,
# Output2: updateFlag of each measurement; 
#          True = has measurement been found; False = no measurement is found in log file
[meas, flag] = log.log_data()
