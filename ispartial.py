from functools import partial

def ispartial(obj:object, cls:object) -> bool:
    if obj is cls: return True
    while type(obj) is partial:
        obj = obj.func
    return obj is cls


def test_ispartial():
    def f(): pass
    assert ispartial(f, f)
    assert ispartial(partial(f), f)
    assert ispartial(partial(partial(f)), f)
    assert ispartial(partial(partial(partial(f))), f)
