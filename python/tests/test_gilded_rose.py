# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose

ITEM_NAMES = {
    "standard": "Standard item",
    "aged_brie": "Aged Brie",
    "sulfuras": "Sulfuras, Hand of Ragnaros",
}


class GildedRoseTest(unittest.TestCase):
    def test_standard_item(self):
        item = Item(ITEM_NAMES["standard"], 1, 20)

        GildedRose([item]).update_quality()

        self.assertEqual(ITEM_NAMES["standard"], item.name)
        self.assertEqual(0, item.sell_in)
        self.assertEqual(19, item.quality)

    def test_expired_item(self):
        item = Item(ITEM_NAMES["standard"], 0, 20)

        GildedRose([item]).update_quality()

        self.assertEqual(-1, item.sell_in)
        self.assertEqual(18, item.quality)

    def test_quality_stays_at_zero(self):
        item = Item(ITEM_NAMES["standard"], 0, 0)

        GildedRose([item]).update_quality()

        self.assertEqual(-1, item.sell_in)
        self.assertEqual(0, item.quality)

    def test_quality_does_not_go_negative(self):
        item = Item(ITEM_NAMES["standard"], 0, 1)

        GildedRose([item]).update_quality()

        self.assertEqual(-1, item.sell_in)
        self.assertEqual(0, item.quality)

    def test_already_expired_item(self):
        item = Item(ITEM_NAMES["standard"], -1, 20)

        GildedRose([item]).update_quality()

        self.assertEqual(-2, item.sell_in)
        self.assertEqual(18, item.quality)

    def test_quality_at_fifty_decreases(self):
        item = Item(ITEM_NAMES["standard"], 1, 50)

        GildedRose([item]).update_quality()

        self.assertEqual(0, item.sell_in)
        self.assertEqual(49, item.quality)

    def test_aged_brie(self):
        item = Item(ITEM_NAMES["aged_brie"], 1, 20)

        GildedRose([item]).update_quality()

        self.assertEqual(0, item.sell_in)
        self.assertEqual(21, item.quality)

    def test_expired_aged_brie(self):
        item = Item(ITEM_NAMES["aged_brie"], 0, 20)

        GildedRose([item]).update_quality()

        self.assertEqual(-1, item.sell_in)
        self.assertEqual(22, item.quality)

    def test_aged_brie_quality_stays_at_fifty(self):
        item = Item(ITEM_NAMES["aged_brie"], 0, 50)

        GildedRose([item]).update_quality()

        self.assertEqual(-1, item.sell_in)
        self.assertEqual(50, item.quality)

    def test_sulfuras(self):
        item = Item(ITEM_NAMES["sulfuras"], 1, 80)

        GildedRose([item]).update_quality()

        self.assertEqual(1, item.sell_in)
        self.assertEqual(80, item.quality)

    def test_expired_sulfuras(self):
        item = Item(ITEM_NAMES["sulfuras"], -1, 80)

        GildedRose([item]).update_quality()

        self.assertEqual(-1, item.sell_in)
        self.assertEqual(80, item.quality)

if __name__ == '__main__':
    unittest.main()
