import numpy as np
import matplotlib.pyplot as plt
sps=2000
freq_hz=440.0
duration_s=1

waveform= np.sin(2*np.pi* 440 * np.arange(sps* 0.5) / sps)
waveform2= np.sin(2*np.pi* 880* np.arange(sps* 0.5) / sps)
waveform3= np.sin(2*np.pi* 1320 * np.arange(sps* 0.5) / sps)

a= np.zeros(int(sps* 1.5))
a[0:int(sps*0.5)] += waveform
a[int(sps*0.5):int(sps*1)] += waveform2

a[int(sps*1):int(sps*1.5)] += (waveform *1)
a[int(sps*1):int(sps*1.5)] += (waveform2 *0.8)
a[int(sps*1):int(sps*1.5)] += (waveform3 *0.1)
a[int(sps*1):int(sps*1.5)] /= 3





import matplotlib.pyplot as plt
import numpy as np

b=list(a)
#y=2*np.sin(4*x)-x*2+10*x  #f(x)=2sin(4x)-x^2+10x
plt.plot(b)
plt.xlabel("T[s]")
plt.show()