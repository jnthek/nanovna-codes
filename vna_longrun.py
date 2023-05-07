from nanovna import NanoVNA
import numpy as np
import matplotlib.pyplot as plt
import time 

nv = NanoVNA()
nv.set_sweep(1e6, 300e6)

# plt.figure()
# nv.fetch_frequencies()
# freq = nv.frequencies
# s11 = nv.data(0)
# s12 = nv.data(1)
# plt.plot(freq, np.real(s11))
# plt.plot(freq, np.imag(s11))
# 
# plt.figure()
# nv.fetch_frequencies()
# freq = nv.frequencies
# s11 = nv.data(0)
# s12 = nv.data(1)
# plt.plot(freq, np.real(s11))
# plt.plot(freq, np.imag(s11))
# plt.show()


# import numpy as np
# import math
# import matplotlib.pyplot as plt
# from matplotlib import animation
# from pylab import *
# from rtlsdr import *
# import time 

try:
	while True:
		nv.fetch_frequencies()
		freq = nv.frequencies
		S11 = nv.data(0)
		my_time = time.gmtime(time.time())
		file_name = str(my_time.tm_year)+'_'+str(my_time.tm_mon).zfill(2)+'_'+str(my_time.tm_mday).zfill(2)+'-'+str(my_time.tm_hour).zfill(2)+str(my_time.tm_min).zfill(2)+str(my_time.tm_sec).zfill(2)
		np.save(file_name,S11)  
		print "Saved into",file_name
except KeyboardInterrupt:
	print('Acquisition stopped !')

finally:
	sdr.close()
	print('Exiting')


