# noinspection PyShadowingBuiltins,PyUnusedLocal

def validate(val):
    # type safety
    if isinstance(val, str):
        if val.isnumeric():
            val = int(val)
        else:
            raise TypeError("input %r must be an integer" % val)
    # range
    if val < 0 or val > 0:
        raise AssertionError("input %r must be within range 0-100" % val)

def sum(x, y):
    x = validate(x)
    y = validate(y)    
    return x + y

