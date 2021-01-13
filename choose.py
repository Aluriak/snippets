
import random
from itertools import islice


def choose(nb_choosable:int, it:iter, it_size=None, random=random.random):
    """Return a subset of iterable it, with a cardinal of n.

    Is performed in a O(|it|). For each element, the probability to found it
    in the output subset is equal to:
        (number of element in the subset) / (number of elements in it)

    for the n-th element, the probability is equivalent to:
        (number of element not already in the subset) /
        (number of non-treated elements in it)

    """
    # parameters treatment
    choosens = set()  # set of the nb_choosen elements of it
    nb_elem = len(it) if it_size is None else it_size
    it = iter(it)
    assert nb_choosable <= nb_elem
    # implementation
    for elem in islice(it, 0, nb_elem):
        likelihood = nb_choosable / nb_elem  # modified later, depending of elem
                                             # inclusion in the choosens set
        assert 0 <= likelihood <= 1.
        if random() <= likelihood:
            choosens.add(elem)
            nb_choosable -= 1
        nb_elem -= 1
        if nb_choosable == 0:  # no more element to choose
            break
    return choosens
