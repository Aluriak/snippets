

import itertools
import collections

def window(it:iter, size:int=2):
    it = iter(it)
    window = collections.deque(itertools.islice(it, 0, size), maxlen=size)
    while True:
        yield tuple(window)
        try:
            window.append(next(it))
        except StopIteration:
            return

TESTS = {
    ('ABC', 2): (('A', 'B'), ('B', 'C')),
    ('ABCD', 2): (('A', 'B'), ('B', 'C'), ('C', 'D')),
    ('ABC', 3): (('A', 'B', 'C'),),
    ('ABCD', 3): (('A', 'B', 'C'), ('B', 'C', 'D')),
}


for val, out in TESTS.items():
    res = tuple(window(*val))
    assert res == out, res

