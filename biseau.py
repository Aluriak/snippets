"""Biseau usage example"""

import biseau


context = """
edge(a,b).
"""

img = biseau.compile_to_single_image(context, outfile='out.png', dotfile='out.dot', dot_prog='neato')
