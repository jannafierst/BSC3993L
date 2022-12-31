def countdown(n):
  for i in range(n):
    print(n-i)
  print('Blastoff!')

def countdown2(n):
  while n > 0:
    print(n)
    n = n - 1
  print('Blastoff!')

#countdown(5)

#countdown2(5)
'''
Newton’s method:

For any number, a

Start with an estimate of the square root, x

Calculate y given this formula

y = (x + (a/x)) / 2

Keep calculating until y stops changing (converges)
'''
#a = 4.0

#a = 121.0

#x = 3.0
"""
y = (x + a/x) / 2

print(y)

x = y

y = (x + a/x) / 2

print(y)

x = y

y = (x + a/x) / 2

print(y)

x = y

y = (x + a/x) / 2

print(y)

x = y

y = (x + a/x) /2

print(y)
"""
def my_sqrt(x,a): 
  while True:
    print(x)
    y = (x + a/x) /2
    if y == x:
      break # break at convergence
    x=y

my_sqrt(1100,9)
