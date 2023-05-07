import glob
import numpy as np
import matplotlib.pyplot as plt

txtfiles = []
for file in glob.glob("./DATA/*.npy"):
    txtfiles.append(file)

data_matrix = np.zeros(101)+np.zeros(101)*1j

for file_name in txtfiles:
    data = np.load(file_name)
    data_matrix = np.column_stack([data_matrix, data])
