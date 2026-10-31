from aims.cart import Cart
from aims.dvd import DigitalVideoDisc

import unittest

class TestCart(unittest.TestCase):

    def test_cart_appending(self):
        cart = Cart()
        for _ in range(20):
            cart.add_dvd(DigitalVideoDisc("The Lion King", "Animation", "Roger Allers", 87, 19.95))
        
        assert not cart.add_dvd(DigitalVideoDisc("The Lion King", "Animation", "Roger Allers", 87, 19.95))
