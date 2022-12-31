from matplotlib import pyplot as plt

years = [1950,1960,1970,1980,1990,2000,2010]

gdp =  [300.2, 543.3, 1075.9, 2862.5, 5979.6,10289.7, 14958.3]

plt.plot(years, gdp, color='purple', marker='*',
linestyle='none')

plt.title("Nominal GDP")
plt.ylabel("Billions of $")
plt.show()

#Plotting with numpy

import numpy as np

a = np.arange(15).reshape(3,5)
print(a)

print(a.shape)
print(a.ndim)

print(a[0])
print(a[0][0])
print(a[1])
print(a[1][0])

b = np.arange(16).reshape(2,4,2)

print(b)
print(b.shape)
print(b.ndim)

print(b*0.1)

# Plotting with matplotlib

import numpy as np
import matplotlib.pyplot as plt

men_means = (20,35,30,35,27)
women_means = (25,32,34,20,25)
group_means = (45,67,64,55,52)
ind = np.arange(len(men_means))
width = 0.5
fig, ax = plt.subplots()
rects1 = ax.bar(ind - width/2, men_means, width, color="SkyBlue", label= "Men")
rects2 = ax.bar(ind + width/2, women_means, width, color="ForestGreen", label= "Women")

ax.set_ylabel('Scores')
ax.set_title('Scores by group and gender')
ax.set_xticks(ind)
ax.set_xticklabels(('G1','G2','G3','G4','G5'))
ax.legend()
plt.show()
