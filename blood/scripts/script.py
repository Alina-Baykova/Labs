import matplotlib.pyplot as plt
import numpy as np

k = 0.0999
b = -8.6347
def get_pressure_mmHg(number):
    result = number * k + b
    return result

lines = []
with open('blood-data-before', 'r') as beforef:
    lines = beforef.readlines()

before_duration_line  = lines[2]
before_duration = float(before_duration_line[12:17])

before_data_lines = lines[4::]
before_data = []
for data_line in before_data_lines:
    data_line.rstrip('\n')
    data = int(data_line)

    data = get_pressure_mmHg(data)

    before_data.append(data)
before_data = np.array(before_data)

before_times = np.arange(0, before_duration, before_duration/len(before_data))

# --- AFTER ---
with open('blood-data-after', 'r') as afterf:
    lines = afterf.readlines()

after_duration_line  = lines[2]
after_duration = float(after_duration_line[12:17])

after_data_lines = lines[4::]
after_data = []
for data_line in after_data_lines:
    data_line.rstrip('\n')
    data = int(data_line)

    data = get_pressure_mmHg(data)

    after_data.append(data)
after_data = np.array(after_data)

after_times = np.arange(0, after_duration, after_duration/len(after_data))

figure, axes = plt.subplots()
#axes.plot(before_times[::100], before_data[::100], ms=0.25, label=r'Давление - 107/59 [мм. рт. ст.]')
#plt.xlabel(r'Время [c]')
#plt.ylabel(r'Давление [мм. рт. ст.]')
#plt.title(r'Артериальное давление до физической нагрузки')
#plt.text(3.62, 108.0, r'Systole')
#plt.text(3.17, 104.5, r'*')
#plt.text(12.73, 61.0, r'Diastole')
#plt.text(12.23, 56.3, r'*')
#plt.grid(True)
axes.plot(after_times[::100], after_data[::100], ms=0.25, label=r'Давление - 116/62 [мм. рт. ст.]')
plt.xlabel(r'Время [c]')
plt.ylabel(r'Давление [мм. рт. ст.]')
plt.title(r'Артериальное давление после физической нагрузки')
plt.text(2.94, 116.1, r'Systole')
plt.text(2.43, 113.6, r'*')
plt.text(14.44, 64.6, r'Diastole')
plt.text(13.74, 59.7, r'*')
plt.grid(True)

axes.legend()
plt.show()