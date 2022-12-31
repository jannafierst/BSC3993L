"""
This module contains code to draw a koch curve and a fractal snowflake
created with the koch fractal function
"""

def koch(t, n):
    """Draws a koch curve with length n.""" # A Python function comment
    if n < 10:
        t.fd(n)
        return
    m = n/3
    koch(t, m) # the function recursively calls itself
    t.lt(60)
    koch(t, m)
    t.rt(120)
    koch(t, m)
    t.lt(60)
    koch(t, m)

def snowflake(t, n):
    """Draws a snowflake (a triangle with a Koch curve for each side)."""
    for i in range(3):
        koch(t, n) # snowflake calls koch
        t.rt(120)
