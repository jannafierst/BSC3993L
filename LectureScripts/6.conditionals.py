

''''
def x_if(x): # alternative execution
  if x > 0:
    print('x is positive')
  else:
    print('x is negative')

def x_if(x): # chained conditional
  if x > 0:
    print('x is positive')
  elif x < 0:
    print('x is negative')
  else:
    print('x = 0')

def x_if(x): # chained conditionals can be built up >2
  if x > 0:
    print('x is positive')
  elif x < 0:
    print('x is negative')
  elif x == 0:
    print('x = 0')
  else:
    pass
'''

def x_y(x,y): # nested conditional
      if x == y:
         print('x and y are equal')
      else:
         if x < y:
            print('x is less than y')
         else:
            print('x is greater than y')

x_y(7,-5)

#x_if(-5)

#x_if(0)
