
# LTspice Installation Path
dir_XVIIx64 = "C:\Program Files\LTC\LTspiceXVII"

import subprocess

# Start simulating the schematic opened on the cmd without pressing the Run button
# subprocess.call(dir_XVIIx64 + "\XVIIx64.exe -Run LowPassFilter.asc")

# Run in batch mode. E.g. "XVIIx64.exe -b deck.cir" will leave the data in file deck.raw
subprocess.call(dir_XVIIx64 + "\XVIIx64.exe -b LowPassFilter.cir")