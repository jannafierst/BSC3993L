def countdown(n):
  if n <= 0:
    print('Blastoff!')
  else:
    print(n)
    countdown(n-1)

def out(n):
  print(n)
  out(n)

#countdown(5)

#out(5)
