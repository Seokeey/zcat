#!/usr/bin/env python3




from sortedcontainers import SortedDict



class Order:

    def __init__(self, side: str):
        self.side = side
        self.order = set()
        self.quotes = SortedDict()
        self.prices = self.order.keys()
        self.quotes = self.order.items()

    def __repr__(self):
        pass
