import matplotlib.pyplot as plt

#plt.plot(range(10))
#plt.show()

#now lets create a plot

time = list(range(0,7))
CO2 = [250, 265, 272, 260, 300, 320, 389]

plt.plot(time, CO2, color = 'blue', linestyle= 'dashed')
ax.set(xlabel='time (decade)', ylabel='CO2 conc (ppm)',
       title='About as simple as it gets, folks')
plt.show()


