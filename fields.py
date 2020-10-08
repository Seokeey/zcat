#/usr/bin/env python3


class Field(float):

    def __init__(self, value=0.0):
        if isinstance(value, (str, int)):
            value = float(value)
        self.value = value
        self.dtype = type(self).__name__
        self

    def __repr__(self):
        return repr(self.value)

    def __abs__(self):
        return self.__class__(abs(self.value))

    def __neg__(self):
        return -self.value



class Price(Field):

    def __repr__(self):
        return "%s(%.8f)" % (self.dtype, self.value)

class Amount(Field):

    def __repr__(self):
        return "%s(%.8f)" % (self.dtype, self.value)
