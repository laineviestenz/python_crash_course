import matplotlib.pyplot as plt

x = range(1,6)
y = [n**3 for n in x]

xa = range(1,5001)
ya = [n**3 for n in xa]

plt.style.use('default')
fig, (ax, aa) = plt.subplots(1, 2)

ax.scatter(x,y, c=y, cmap = plt.cm.Reds)
aa.scatter(xa, ya, c=ya, cmap = plt.cm.Blues, s=1)

plt.show()