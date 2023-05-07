from nanovna import NanoVNA
import numpy as np
import matplotlib.pyplot as plt
import time

nv = NanoVNA()
nv.set_sweep(1e6, 800e6)

try:
    while True:
        nv.fetch_frequencies()
        freq = nv.frequencies
        S11 = nv.data(0)
        my_time = time.gmtime(time.time())
        file_name = str(my_time.tm_year)+'_'+str(my_time.tm_mon).zfill(2)+'_'+str(my_time.tm_mday).zfill(2)+'-'+str(my_time.tm_hour).zfill(2)+str(my_time.tm_min).zfill(2)+str(my_time.tm_sec).zfill(2)
        np.save(file_name,S11)  
        print ("Saved into",file_name)
        time.sleep(2)
except KeyboardInterrupt:
    print('Acquisition stopped !')

finally:
    print('Exiting')


