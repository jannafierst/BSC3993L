import random

iterations = 10000

neuron_average = 0

for i in range(iterations):
  neuron_activation = False # neuron is repressed by default
  I1 = bool(random.randint(0,1)) # select inputs at random
  I2 = bool(random.randint(0,1))
  I3 = bool(random.randint(0,1))
  if I1 and I2 or I3 == True:
    neuron_activation = True
    neuron_average += 1

print(neuron_average/iterations)
