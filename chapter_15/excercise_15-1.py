import matplotlib.pyplot as plt
"""plot the first 5 and first 5000 cubes in 2 separate graphs in the same figure"""

x = range(1,6)
y = [n**3 for n in x]

xa = range(1,5001)
ya = [n**3 for n in xa]

plt.style.use('default')
fig, (ax, aa) = plt.subplots(1, 2)

ax.scatter(x,y)
aa.scatter(xa, ya, s=1)

plt.show()