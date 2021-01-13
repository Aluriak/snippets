

# TODO: untested
def clingo_value_from_python_value(val:int or string) -> clingo:
    if isinstance(val, int):
        return clingo.Number(val)
    elif isinstance(val, str):
        return clingo.String(val)
    else:
        raise ValueError(f"I don't know what is the clingo value '{val}' "
                         "of type '{val.type}'")

# TODO: untested
def python_value_from_clingo_value(val:clingo) -> int or string:
    if clingo.type == 'number':
        return clingo.number
    elif clingo.type == 'string':
        return clingo.string
    else:
        raise ValueError(f"I don't know what is the clingo value '{val}' "
                         "of type '{val.type}'")
