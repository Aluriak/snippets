"""There is multiple ways to emulate multiple line comment in python.

A good multiple line comment system allow one to quickly enable/disable
many lines of code (ideally, in a single keystroke).

"""


# this one allow the commented code to be compiled

if (
    True  # code will be compiled but not executed if this line is commented
):
    print('compiled but not executed')



"""
print("never compiled not executed, unless the previous line is commented")
"""#""""""Comment about the block"""
