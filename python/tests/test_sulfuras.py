import unittest

from gilded_rose import Item, GildedRose

ITEM_NAME = "Sulfuras, Hand of Ragnaros"


class SulfurasTest(unittest.TestCase):
    def test_sulfuras(self):
        item = Item(ITEM_NAME, 1, 80)

        GildedRose([item]).update_quality()

        self.assertEqual(1, item.sell_in)
        self.assertEqual(80, item.quality)

    def test_expired_sulfuras(self):
        item = Item(ITEM_NAME, -1, 80)

        GildedRose([item]).update_quality()

        self.assertEqual(-1, item.sell_in)
        self.assertEqual(80, item.quality)


if __name__ == '__main__':
    unittest.main()
