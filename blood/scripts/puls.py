import matplotlib.pyplot as plt
import numpy as np

tmp_before_data = []
mean_before_data = []
before_times_fmean = []

start = 65594
step = 726
end = start

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

for i in range(200):
    end += step

    tmp_before_data = np.array(before_data[
                               start:end])
    mean_before_data.append(np.mean(tmp_before_data))

    tmp_before_data = np.array(before_times[start:end])
    before_times_fmean.append(np.mean(tmp_before_data))

    start += step

print(mean_before_data)
print(before_times_fmean)

new_before_data = []
substructer = 0
start = 65594
step = 726
for i in range(200):
    substructer = mean_before_data[i]
    start = 65594 + i * step
    for j in range(step):
        new_before_data.append(before_data[start + j] - substructer)


figure, axes = plt.subplots()
axes.set_xlim([3.32, 12.36])
axes.set_ylim([-1, 1])
axes.set_title('Пульс \nдо физической нагрузки', wrap=True)
axes.plot(before_times[65594:210794:step], new_before_data[::step], ms=0.25, label='Пульс - 80 [уд. мин]')


axes.legend()
plt.show()

