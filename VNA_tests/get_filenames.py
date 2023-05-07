import glob

txtfiles = []
for file in glob.glob("./DATA/*.npy"):
    txtfiles.append(file)

print (txtfiles)
