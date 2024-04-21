import numpy as np
import matplotlib.pyplot as plt

data = np.genfromtxt("lab7/lp data 15.csv", delimiter=",", skip_header=1)
freq = data[:, 1]
db = data[:, 3]

x = np.array(freq)
y = np.array(db)


# Fit with polyfit
best_fit = np.polyfit(x, y, 5)
plt.plot(x, y, 'o')
plt.plot(x, np.polyval(best_fit, x), 'r-')
plt.xscale('log')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Gain (db)')
plt.title('Frequency Analysis of Low Pass Filter')
plt.show()
