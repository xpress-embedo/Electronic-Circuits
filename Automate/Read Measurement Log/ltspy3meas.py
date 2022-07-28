# -*- coding: utf-8 -*-
"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Created on Sat Oct 12 13:24:31 2019
@author: Ye Zhao, EEsanity
Email: EEsanity@gmail.com
Created on 10/12/2019
Last updated on: 02/08/2020 (Monday)
Current Version: 0.6
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
=================================   History   =================================
Version 0.6: 02/08/2021 (Monday)
    A bug is fixed in step measurement
Version 0.5: 07/18/2020 (Saturday)
    A bug is fixed in the measurement name list
Version 0.4: 06/14/2020 (Sunday)
    Able to read stepped sweep measurement
Version 0.3: 04/18/2020 (Saturday)
    Able to read scientific format display of a number in exponential notation

"""


import re  # Regular expression to extract the measurement data
import numpy as np
import sys

#  
# [----   Notes   ----]
# Input: file names and measurement names
# Output1: measurment in a row in NumPy array,
# Output2: updateFlag of each measurement
#
# =============================================================================
class LogGetClass:
# =============================================================================
    def __init__(self, logFile, measName):

        self.logFile = logFile
        self.logFile_correctName = True
        # check the extension of the file
        if not self.logFile.endswith(".log"):
            # if the extension of the file is NOT ending with ".log"
            self.logFile_correctName = False
            print("****  Invalid Filename. The file should end with '.log'  ****")
            sys.exit("****  Problem is found in log file name  ****") # exit the imported module
        self.fileName = logFile[:-4]
        # Updated for stepped measurements in log files 06/10/2020
        # First, check if we have stepped measurement in the .op.raw file
        self.stepped = False   # the flag of stepped sweep in the measurement
        self.steplen = None    # step data length
        self.nosteps = None   # nubmer of steps
        self.steppoints = None
        self.stepvariables = None
        self.stepvalues = None
        self.step_legend = []
#        print(self.fileName + '.op.raw')
        try:
            hand_opraw = open(self.fileName + '.op.raw', 'r', encoding="UTF-16 LE") # use encoding
            for line in hand_opraw:
                line = line.rstrip() # strips whitespace (\n) from the RHS of a string
                if line.startswith('Flags:'): # This line contains the key word "stepped"
    #                print(line)
                    if line.find('stepped') == -1: continue
    #                print(line)
                    self.stepped = True
                    self.step_legend = []
#                    print('self.stepped is ',self.stepped)
            hand_opraw.close()
        except: 
            print('*******   Note: cannot find the file with the .op.raw extension    *******')
            hand = open(self.logFile, 'r') # open log file by File handling. Mode is 'r' for reading
            num_step = 0
            for line in hand: # for loop over each line in the file
                line = line.rstrip() # strips whitespace (\n) from the RHS of a string
                if re.search('^.step' ,line) or re.search('step ' ,line):
                    num_step = num_step + 1
                if num_step > 1: # initial 3; change to > 1 on 2/8/2021
                    self.stepped = True
#            print(self.stepped)
            hand.close()
        # The measurement names of each variable
        self.measName = measName
        self.measNameLo = [x.lower() for x in self.measName]  #convert to lower cases
        #  NumPy array of zeros to hold the meas
        #  True = has measurement found; False = no measurement is found in log file
        self.meas = np.zeros([1, len(self.measNameLo)], dtype = float)  # Data will be saved in this np array!
        self.updateFlag = [False]*len(self.measNameLo) # A list of True or False.
        
        
# ============================================================================= 
# ============        Print out each line in the .log file        ============= 
# =============================================================================
    def log_print(self): # create a method
        hand = open(self.logFile, 'r') # open log file by File handling. Mode is 'r' for reading
        for line in hand: # for loop over each line in the file
            line = line.rstrip() # strips whitespace (\n) from the RHS of a string
            print(line)
        hand.close()
        
# ============================================================================= 
# ============        Read the measurment in the .log file        ============= 
# =============================================================================
    def log_data(self): # create a method
        # 1) No Stepped Sweep
        if self.stepped == False: 
            hand = open(self.logFile, 'r') # open log file by File handling. Mode is reading
            for line in hand: # for loop over each line in the file
                line = line.rstrip() # strips whitespace (\n) from the RHS of a string
                # search for variable names
                for i in range(len(self.measNameLo)):
                    # parentheses  to extract the portion of numbers and period
                    # x = re.findall(self.measNameLo[i] + '.+=([+-]?[0-9.]+)',line)
                    line_split = line.split(': ') # line_split is a list
                    if self.measNameLo[i] in line_split: # make sure that this measurement is in the line_split list
                        x = re.findall(self.measNameLo[i] +':' + '.+=([-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)?)',line)
                        #print(x)
                        if len(x) > 0:  # x is a list of tuples
                            x0 = x[0] # credit to: https://stackoverflow.com/questions/638565/parsing-scientific-notation-sensibly
                            self.meas[0][i] = float(x0[0]) # It is a tuple. save the 1st element in NumPy array 
                            self.updateFlag[i] = True # turn Flag to True if we find the variable
                    # search for measurement FAIL'ed ----> working on this
                if re.search("^Measurement \S* FAIL'ed", line):
                    print('*********   Found error in .log file: ' + line + '   **********') # error message
            hand.close()

        # 2) Stepped Sweep
        if self.stepped == True: 
            hand = open(self.logFile, 'r', encoding="utf-8") # open log file by File handling. Mode is reading
            nosteps = 0 # index for stepped
            for line in hand: # for loop over each line in the file
                line = line.rstrip() # strips whitespace (\n) from the RHS of a string
#                print(line)
                # to create "step_legend". Let's search for the key word ".step"
                if line.startswith('.step'):
                    nosteps = nosteps + 1  # j is the total number of stepped sweeps
            print('# of stepped: ', nosteps)
            hand.close()
            
            # working on 06/14/2020 AM: to find the index of measurement under each step
            lineIndex_measNameLo = np.zeros([nosteps, len(self.measNameLo)], dtype = int)  # Data will be saved in this np array!
            hand = open(self.logFile, 'r') # open log file by File handling. Mode is reading
            k = 0 # index for line numbers after rstrip(), starting from 0
            for line in hand: # for loop over each line in the file
                line = line.rstrip() # strips whitespace (\n) from the RHS of a string
                # to create "step_legend". Let's search for the key word ".step"
                # search for variable names
                for i in range(len(self.measNameLo)):
                    line_split = line.split(': ') # line_split is a list
                    if self.measNameLo[i] in line_split: # make sure that this measurement is in the line_split list
                        # parentheses  to extract the portion of numbers and period
                        if re.search('Measurement: ' ,line) and re.search(self.measNameLo[i],line):
#                            print(' ~~~~~~~~~~~~~~~~~ #line index is ', k , '~~~~~~~~~~~~~~~~~')
                            for j in range(nosteps):
                                lineIndex_measNameLo[j][i] = k + j + 2 # each column saves the line number of measurement data.
                k = k + 1
#            print(lineIndex_measNameLo)
            hand.close()
            
            # 
            
            ## search for variable names
            #for i in range(len(self.measNameLo)):
            #    # parentheses  to extract the portion of numbers and period
            #    x = re.findall(self.measNameLo[i] + '.+=([+-]?[0-9.]+)',line) 
            #    if len(x) > 0:
            #        self.meas[0][i] = float(x[0]) # save in NumPy array 
            #        self.updateFlag[i] = True # turn Flag to True if we find the variable
            #    
            self.meas = np.zeros([nosteps, len(self.measNameLo)], dtype = float)
            self.updateFlag = [False]*len(self.measNameLo)
            
            hand = open(self.logFile)
            all_lines = hand.readlines()
            for i in range(len(self.measNameLo)):
                for j in range(nosteps):
                    line_index = lineIndex_measNameLo[j][i] # line number
                    if line_index > 0: # only consider non-zero line numbers. line index 0 is the first line
                        line_content = all_lines[line_index].split() # line content
                        if len(line_content) > 1:
#                            print(line_content)
#                            print(line_content[1])
                            self.meas[j][i] = line_content[1]
                            self.updateFlag[i] = True
        # Return the final results
            hand.close()
        return self.meas, self.updateFlag
    
    def log_legend(self): # create a method
        if self.stepped == True:
            # The first round is to get the total number of stepped sweeps
            self.step_legend = []
            hand = open(self.logFile, 'r') # open log file by File handling. Mode is reading
            j = 0
            for line in hand: # for loop over each line in the file
                line = line.rstrip() # strips whitespace (\n) from the RHS of a string
                # to create "step_legend". Let's search for the key word ".step"
                if line.startswith('.step'):
                    j = j + 1  # j is the total number of stepped sweeps
                    self.step_legend.append(line[6:])
            hand.close()
        # Return the final results, if NOT Stepped, return a empty string
        return self.step_legend