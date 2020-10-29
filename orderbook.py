#!/usr/bin/env python3


import json

from sortedcontainers import SortedDict



class Order:

    def __init__(self, side: str):
        self.side = side
        self.order = set()
        self.quotes = SortedDict()
        self.prices = self.order.keys()
        self.quotes = self.order.items()

    def __repr__(self):
        return "%s: %s\n" (self.side, self.order)

    def __contains__(self, price):
        return price in self.store

    def __len__(self):
        return len(self.quotes)

    @property
    def worst_offer(self):
        return self.quotes[0 if self.side == BID else -1][0]

    def update(self, price, amount):
        self.order[price] = amount
        self.store.add(price)

    def insert(self, price, amount):
        def islice(depth=DEFAULT_DEPTH):
            while len(self.quotes) > depth:
                self.discard(self.worst_offer)

        self.order[price] = amount
        self.store.add(price)
        islice()

    def discard(self, price):
        try:
            del self.order[price]
            self.store.discard(price)
        except KeyError:
            pass

    def process(self, side, price, amount):
        def is_updatable(new_price):
            if len(self) < DEFAULT_DEPTH:
                return True
            old_price = self.worst_offer
            return old_price < new_price if self.side == BID else new_price < old_price

        assert side == self.side

        if amount == 0:
            self.discard(price)
        elif price in self.store:
            self.update(price, amount)
        elif is_updatable(price):
            self.insert(price, amount)

class OrderBook(dict):

    __slots__ = ('asks', 'bids')

    def __init__(self, pair):
        self.asks = Order(ASK)
        self.bids = Order(BID)
        super().__init__({pair: {ASK: self.asks, BID: self.bids}})

    def __repr__(self):
        return "%s\n%s\n" % (self.bids, self.asks)
    
    def get_order_side(self, side):
        return self.bids if side == BID else self.asks

    def update(self, side, price, amount):
        order = self.get_order_side(side)
        order.update(price, amount)

    def insert(self, side, price, amount):
        order = self.get_order_side(side)
        order.insert(price, amount)

    def discard(self, side, price):
        order = self.get_order_side(side)
        order.discard(price)

    def process(self, side, price, amount):
        order = self.get_order_side(side)
        order.process(side, price, amount)



