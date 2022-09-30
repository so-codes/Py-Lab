# Define a procedurehistogram() that takes a list of integers and prints a histogram to the screen.
from matplotlib import pyplot as plt
import numpy as np

a = np.array([22, 87, 5, 43, 56, 73, 55, 54, 11, 20, 51, 5, 79, 31, 27])
fig, ax = plt.subplots(figsize=(7, 10))
ax.hist(a, bins=[0, 20, 40, 60, 80, 100])
plt.show()