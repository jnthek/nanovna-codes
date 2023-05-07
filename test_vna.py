from nanovna import NanoVNA
import numpy as np
import matplotlib.pyplot as plt
nv = NanoVNA()
nv.set_sweep(1e6, 300e6)
nv.fetch_frequencies()

freq = nv.frequencies
s11 = nv.data(0)
s12 = nv.data(1)
plt.plot(freq, np.real(s11))
plt.plot(freq, np.imag(s11))
plt.show()
