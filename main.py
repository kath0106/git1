import matplotlib.pyplot as plt
import random

x = []
y = []
c = []
for i in range(10):
    x.append(random.randint(1,20))
    y.append(random.randint(1,20))
    c.append(random.randint(5, 200))

plt.scatter(x, y, color="red")
plt.savefig('scatter.jpg')
plt.show()