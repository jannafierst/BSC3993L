import random
from repeat import repeater

color = ["CadetBlue4","coral2","deep sky blue","DarkGoldenrod2","black","DarkOrchid4"] # Making our colors fancier

# Permissible colors http://www.tcl.tk/man/tcl8.4/TkCmd/colors.htm

bob = turtle.Turtle()
print(bob)
bob.shape("turtle")
bob.color(random.choice(color),random.choice(color))

repeater(bob)
