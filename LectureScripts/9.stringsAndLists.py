fruit='banana'

print(fruit[-2])

index=0

while index < len(fruit):
  letter = fruit[index]
  print(letter)
  index = index + 1

for a in fruit:
  print(a)

greeting = 'Hello, World!'

print(greeting[0])

greeting[0] = 'J'

print(greeting[0])

fruit.upper()

prefixes = 'JKLMNOPQ'
suffix = 'ack'


for letter in prefixes:
    if letter in ('O', 'Q'):
        print(letter + 'u' + suffix)
    else:
        print(letter + suffix)

for letter in prefixes:
    if letter in ('O','Q'):
        letter+="u"
    print(letter+suffix)

for letter in prefixes:
    if letter == "O":
        print(letter + "u" + suffix)
    elif letter == "Q":
        print(letter + "u" + suffix)
    else:
        print(letter + suffix)

a = [10, 20, 30, 40]

b = ['crunchy frog', 'ram bladder', 'lark vomit']

b.append('racing horse')

c = [5,'hat baby',24,'a!=2'] 

d = [10, 20, 30, [2,10]]

q = [10,20,30,40]

r = ['ab','bc','cd','de']

qr = list(zip(q,r))

qr = q +r

print(qr)

print(len(b))

for w in range(len(b)):
  print(b[w])

for element in b:
  print(element)

b.extend(c)

print(b)

b.sort()

print(sum(r))

b.remove(24)

print(b)

del b[3:6]

print(b)

my_string = 'abracadabra'
t = list(my_string)
print(t)

print(t[2])

mine = 'pining for the fjords'
t = list(mine)
t = mine.split()
print(t)

delimiter = ' '

print(delimiter.join(t))

delimiter = ''

print(delimiter.join(t))
