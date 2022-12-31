"""
This module draws a turtle starburst with
an outline and fill color"""

def repeater(t):
    t.begin_fill()
    while True:
        t.fd(180)
        t.lt(170)
        if abs(t.pos()) < 1:
            break
    t.end_fill()
