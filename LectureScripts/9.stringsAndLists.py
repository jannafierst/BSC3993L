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

'''
for letter in prefixes:
    if letter in ('O', 'Q'):
        print(letter + 'u' + suffix)
    else:
        print(letter + suffix)

for letter in prefixes:
    if letter in ('O','Q'):
        letter+="u"
    print(letter+suffix)
'''

for letter in prefixes:
    if letter == "O":
        print(letter + "u" + suffix)
    elif letter == "Q":
        print(letter + "u" + suffix)
    else:
        print(letter + suffix)
