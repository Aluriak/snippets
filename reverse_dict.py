
from collections import defaultdict

def reverse_dict(d:dict, aggregator=set) -> dict:
    """Return a new dict containing keys as values (aggregated into an `aggregator`)
    and values as keys.

    >>> sorted(tuple(reverse_dict({1: 2, 2: 3, 4: 2}).items()))
    ((2, {1, 4}), (3, {2}))

    """
    out = defaultdict(list)
    for key, val in d.items():
        out[val].append(key)
    return {key: aggregator(val) for key, val in out.items()}
