def add(a, b):
    return a + b


def addFixedValue(a):
    y = 5
    return y + a


def sample(variable):  # @UnusedVariable
    """
    this is my method doc.
    @param variable:
    """
    print "this is my update blabla"


print add(1, 2)
print addFixedValue(1)
sample("pedro")
