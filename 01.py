import matplotlib.pyplot as plt
import math

a = [math.sin(i/1000) for i in range(0,int(math.pi*1000),1)]

plt.plot(a, 'r-*')
plt.show()

