
# LTspice Installation Path
dir_XVIIx64 = "C:\Program Files\LTC\LTspiceXVII"

import subprocess

'''
We can only update the text file easily using Python.
And to generate the text file, first we need to generate the *.cir, which can
be generated using SPICE netlist and saving it as *cir file and the same file
can be saved as *.txt file, and that will work for us
'''

original_file = "LowPassFilter.txt";
res_original = "res=1k";
cap_original = "cap=0.1u";

with open(original_file, 'rb') as file:     # Read the file as binary data
    original_data = file.read();
    print (original_data);                  # only for debugging
    # replace resistance and capacitor value with the updated value
    # first replace the resistor value to 10k
    data_temp = original_data.replace( res_original.encode('ascii'), \
                                       'res=10k'.encode('ascii'));
    # second replace the resistor value to 10u
    data_temp = data_temp.replace( cap_original.encode('ascii'), \
                                  'cap=10u'.encode('ascii'));
    
with open('newfile.txt', 'wb') as file:
    file.write(data_temp);

subprocess.call(dir_XVIIx64 + "\XVIIx64.exe -b newfile.txt")