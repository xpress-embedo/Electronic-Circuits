# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 20:32:17 2022

@author: xpress_embedo
"""

import os
import time
import ltspy3
import subprocess
import matplotlib.pyplot as plt

# %% Project Constants
# LTspice Installation Path
dir_XVIIx64 = "C:\Program Files\LTC\LTspiceXVII"

# original values from the file
org_R1 = 'res1=1k';
org_C1 = 'cap1=0.1u';
org_R2 = 'res2=1k';
org_C2 = 'cap2=0.1u';

list_R1 = ['res1=1k', 'res1=10k'];
list_R2 = ['res2=1k', 'res2=10k'];
list_C1 = ['cap1=0.1u', 'cap1=1u'];
list_C2 = ['cap2=0.1u', 'cap2=1u'];

# %% Prepare Multiple Simulation Files based on the above data
working_dir = os.getcwd();      # get Current Working Directory

try:
    os.mkdir('SimFolder');
except:
    print('The folder already exists');
    
filename = "LowPassFilter_2ndOrderAutomate";
filename_txt = filename + '.txt';

start_time = time.time();
print("Preparing Multiple Files for Simulation....");

list_all = [];
idx = 0;
for r1 in list_R1:
    for c1 in list_C1:
        for r2 in list_R2:
            for c2 in list_C2:
                new_filename = r1 + '_' + c1 + '_' + r2 + '_' + c2;
                new_filename_txt = new_filename + '.txt';
                list_all.append(new_filename);
                with open(filename_txt, 'rb') as file:
                    file_data = file.read();
                    temp_data = file_data.replace(org_R1.encode('ascii'), r1.encode('ascii'))\
                        .replace(org_C1.encode('ascii'), c1.encode('ascii'))\
                        .replace(org_R2.encode('ascii'), r2.encode('ascii'))\
                        .replace(org_C2.encode('ascii'), c2.encode('ascii'))
                
                with open('SimFolder/' + new_filename_txt, 'wb') as file:
                    file.write(temp_data);
                
                idx = idx+1;
                print ('Running Text File #: ',idx,' out of 16 with filename: ', new_filename, sep='');
                # run LTspice in the for loop, this will generate *.raw file
                subprocess.call(dir_XVIIx64 + "\XVIIx64.exe -b " + 'SimFolder/'+new_filename_txt);


# %% Sun Simulation and Save Figures
try:
    os.mkdir('FigFolder') # no whitespace
except:
    print("The folder already exists!")

idx = 0;
for each_file in list_all:
    if '' in each_file:
        print (each_file);
        simulation_data = ltspy3.SimData('SimFolder/'+each_file+'.raw');
        time_data = simulation_data.values[0];      # the first element is the time
        trace_data = simulation_data.values[1:3];   # the rest elements are traces as in matrices
        # time to plot and save the plots
        plt.figure(1);  # always use 1, because the plot will be closed once saved
        plt.plot(time_data, trace_data[0], label='$V_{in}$');
        plt.plot(time_data, trace_data[1], label='$V_{out}$');
        plt.legend(loc='upper right', shadow=True);
        plt.xlabel('Time (sec)');
        plt.ylabel('Voltage (V)');
        plt.grid(True);
        # Is used to set the main figure title
        plt.suptitle(each_file);
        plt.show();
        # Save Figures
        plt.savefig('FigFolder/' + each_file + '.png', dpi=300);
        # Close Figures
        plt.close('all');
        idx = idx+1;
        print('Saving Figure #: ', idx, 'out of 16, with a file name: ', each_file, sep='');
        

end_time = time.time();
print ('Simulation and Waveform Saving is done.....');
print ('Time Elapsed is:', end_time - start_time);
