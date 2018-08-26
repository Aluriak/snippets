

from itertools import zip_longest


def grouper(iterable, n, fillvalue=None):
    """Collect data into fixed-length chunks or blocks

    >>> tuple(map(''.join, grouper('ABCDEFG', 3, 'x')))
    ('ABC', 'DEF', 'Gxx')
    >>> tuple(grouper('ABC', 2))
    (('A', 'B'), ('C', None))

    """
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fillvalue)
