import numpy as np
import csv
import matplotlib.pyplot as plt

resistance = 250
diode_name = 'Zener Diode in Regular Orientation'
# Data
with open('zener normal2.csv', 'r') as file:
    reader = csv.reader(file)
    arr = list(reader)

time = [row[0] for row in arr[2:]]

for i in range(len(time)):
    x = time[i].split('E')
    time[i] = float(x[0]) * 10 ** int(x[1])
print(time)

voltage_one = [row[1] for row in arr[2:]]
voltage_two = [row[2] for row in arr[2:]]

for i in range(len(voltage_one)):
    x = voltage_one[i].split('E')
    voltage_one[i] = float(x[0]) * (10 ** int(x[1]))
    x = voltage_two[i].split('E')
    voltage_two[i] = float(x[0]) * 10 ** (int(x[1]))

y = []
x = np.array(voltage_one)
for i in range(len(voltage_one)):
    y.append((float(voltage_two[i]) / resistance))
# Fit with polyfit
best_fit = np.polyfit(x, y, 30)
plt.plot(voltage_one, y, 'o')
plt.plot(x, np.polyval(best_fit, x), 'r-')
plt.xlabel('Voltage Diode (V)')
plt.ylabel('Current Diode (A)')
plt.title(f'IV Curve of {diode_name}')
plt.tight_layout()
plt.show()
