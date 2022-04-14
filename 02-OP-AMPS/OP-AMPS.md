# Operational Amplifier

OP-AMPS are linear devices designed for acquiring voltage amplification, signal conditioning, filtering or for performing mathematical operations such as addition, subtraction, integration, differentiation etc.  
They are driven by external DC voltage supplies (+Vs, −Vs) which are ordinarily symmetrical and generally taken in a range of ± 10 to ± 20 V and the output of an OP-Amp is limited to approximately 1.5 V less than these supply voltages. A limiting output implies that an OP-Amp can only amplify signals to a level within a range of supply voltages used, and therefore it is impossible for an OP-Amp to generate a voltage > +Vs or < −Vs.  
A constraint i.e. −Vs < Vout < +Vs may result in clipping of peaks of an output sine wave and can produce distortion in an output wave.  


## OP-AMP as Inverting Amplifier  
The following is the schematic of the OP-Amp working as Inverting Amplifier. The gain of the OP-Amp is ```Av = -Rf/R1``` which in below case is -10.  
![Schematic](Support\\OP-AMP_As_Inverting_Amplifier.png)  

And as can be seen in the below waveform, the input voltage peak is 1V and it's output voltage peek is -10V
![Waveform](Support\\OP-AMP_As_Inverting_Amplifier_Waveform.png)  

Op-Amp can only amplify the signals to a level within the range of supply voltage, so now if the signal is changed to 5V, the output of -50V is not possible because of the Op-Amp supply limitation and the output will be clipped as shown below. 
![Waveform](Support\\OP-AMP_As_Inverting_Amplifier_LimitCrossed_Waveform.png)  

Here it can be seen clearly that input voltage is 5V sine wave, while the output waveform is clipped at +12V and -12V values.  

