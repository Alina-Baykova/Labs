import numpy as np

filename_40  = '40 blood-data 2022-11-17 14:22:22.txt'
filename_80  = '80 blood-data 2022-11-17 14:24:07.txt'
filename_120 = '120 blood-data 2022-11-17 14:25:24.txt'
filename_160 = '160 blood-data 2022-11-17 14:26:23.txt'

with open(filename_40, 'r') as file0:
    lines = file0.readlines()

vals0 = []
vals0_str = lines[4::1]
for line in vals0_str:
    line.rstrip('\n')
    val0 = int(line)
    vals0.append(val0)

# print(vals0)
val0_mean = np.mean(vals0)
print(val0_mean)