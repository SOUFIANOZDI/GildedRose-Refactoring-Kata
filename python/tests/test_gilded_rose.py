# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_standard_item(self):
        item = Item("foo", 1, 20)

        GildedRose([item]).update_quality()

        self.assertEqual("foo", item.name)
        self.assertEqual(0, item.sell_in)
        self.assertEqual(19, item.quality)

    def test_expired_item(self):
        item = Item("foo", 0, 20)

        GildedRose([item]).update_quality()

        self.assertEqual(-1, item.sell_in)
        self.assertEqual(18, item.quality)

    def test_quality_stays_at_zero(self):
        item = Item("foo", 0, 0)

        GildedRose([item]).update_quality()

        self.assertEqual(-1, item.sell_in)
        self.assertEqual(0, item.quality)

if __name__ == '__main__':
    unittest.main()
