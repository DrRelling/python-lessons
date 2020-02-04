def myFunctionWithADocString(x, y=True):
    """Does nothing useful at all.
    Arguments:
    x -- int, will be multiplied by three
    Keyword arguments:
    y -- bool, defaults to True
    """
    x = x * 3
    y = not y
