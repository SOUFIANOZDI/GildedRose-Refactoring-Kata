import unittest

from gilded_rose import Item, GildedRose

ITEM_NAME = "Aged Brie"


class AgedBrieTest(unittest.TestCase):
    def test_aged_brie(self):
        item = Item(ITEM_NAME, 1, 20)

        GildedRose([item]).update_quality()

        self.assertEqual(0, item.sell_in)
        self.assertEqual(21, item.quality)

    def test_expired_aged_brie(self):
        item = Item(ITEM_NAME, 0, 20)

        GildedRose([item]).update_quality()

        self.assertEqual(-1, item.sell_in)
        self.assertEqual(22, item.quality)

    def test_aged_brie_quality_stays_at_fifty(self):
        item = Item(ITEM_NAME, 0, 50)

        GildedRose([item]).update_quality()

        self.assertEqual(-1, item.sell_in)
        self.assertEqual(50, item.quality)

    def test_expired_aged_brie_quality_stops_at_fifty(self):
        item = Item(ITEM_NAME, 0, 49)

        GildedRose([item]).update_quality()

        self.assertEqual(-1, item.sell_in)
        self.assertEqual(50, item.quality)


if __name__ == '__main__':
    unittest.main()
