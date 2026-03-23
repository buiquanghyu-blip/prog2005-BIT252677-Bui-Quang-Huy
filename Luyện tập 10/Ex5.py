import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y1 = x**2
y2 = np.sqrt(x)

fig, axs = plt.subplots(1, 2)

axs[0].plot(x, y1)
axs[0].set_title("y = x^2")
axs[0].set_xlabel("x")
axs[0].set_ylabel("y")

axs[1].plot(x, y2)
axs[1].set_title("y = sqrt(x)")
axs[1].set_xlabel("x")
axs[1].set_ylabel("y")

plt.tight_layout()
plt.show()
