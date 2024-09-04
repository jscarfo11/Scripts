import numpy as np
import matplotlib.pyplot as plt

data = np.genfromtxt("lab7/hp data 15.csv", delimiter=",", skip_header=1)
freq = data[:, 1]
db = data[:, 3]

x = np.array(freq)
y = np.array(db)


# Fit with polyfit
plt.plot(x, y, 'o')
plt.plot(x, y, '-r')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Gain (db)')
plt.xscale('log')
plt.title('Frequency Analysis of High Pass Filter')
plt.show()
