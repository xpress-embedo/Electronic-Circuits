# Rectifiers

### Half Wave Rectifier
This type of rectifier only allows one half-cycle of an AC Voltage waveform to pass, blocking the other half-cycle.  
They are used to convert AC voltage to DC voltage, and only require a single diode to construct.  
The following is the schematic diagram of a Half Wave Rectifier.  
![Schematic](../Support/FullWaveRectifier.png)  

Some important points.
* The output waveform without filtering (capacitor) is as below
  ![Half Wave Rectifier without Output Capacitor](../Support/HalfWaveRectifier_WaveformWoCap.png)  
* By lowering the capacitor value we can see the ripples in the output waveform
* In LTSpice we have a feature known as step simulation, where we can simulate for different values of components
* As can be seen in the below waveform, as the value of capacitor is increased the output becomes more flat or stable
  ![Half Wave Rectifier without Output Capacitor](../Support/HalfWaveRectifier_Waveform.png)  
* The output is little less than the supplied input because of diode, with reduces the voltage by 0.7 V known has junction potential

### Full Wave Rectifier  
This uses a 4-diodes in a bridge configuration to efficiently convert an AC into unidirectional current (pulsating DC).  
A capacitor connected across a rectified output allows an AC signal to pass through it and blocks a DC signal, thereby acting as a high-pass filter.  
Thus AC ripples in a pure DC voltage is obtained across a load resistor.  
The following is the schematic diagram of a Full Wave Rectifier.  
![Schematic](Support\\FullWaveRectifier.png)  

Some Important Points:  
* Because of the junction potential of the 2 diodes in series with the load, the amplitude of the output DC voltage lower than 10V by about 1V. This difference represent the junction potential.
* The following is the waveform if the capacitor is not present.
  ![Waveform](Support\\FullWaveRectifier_WaveformWoCap.png)  
  As can be seen, it's a sine wave with negative side moved to positive side.  
* And the following is the output waveform for different values of capacitors.  
  ![Waveform](Support\\FullWaveRectifier_Waveform.png)  
* It can be observed that capacitive filtering done by 10nF capacitor raises the tail of the half-cycle, the 100nF smoothness the waveform even more but still have a large ripple and then 1uf & 10uF takes out enough of the ripples to make the output DC voltage essentially flat.
* It can be concluded that the larger an RC time constant the flatter the exponential decay, & the closer the approximation to a constant waveform.