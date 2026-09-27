import unittest

from gilded_rose import Item, GildedRose

ITEM_NAME = "Backstage passes to a TAFKAL80ETC concert"


class BackstagePassTest(unittest.TestCase):
    def test_more_than_ten_days(self):
        item = Item(ITEM_NAME, 11, 20)

        GildedRose([item]).update_quality()

        self.assertEqual(10, item.sell_in)
        self.assertEqual(21, item.quality)

    def test_ten_days(self):
        item = Item(ITEM_NAME, 10, 20)

        GildedRose([item]).update_quality()

        self.assertEqual(9, item.sell_in)
        self.assertEqual(22, item.quality)

    def test_six_days(self):
        item = Item(ITEM_NAME, 6, 20)

        GildedRose([item]).update_quality()

        self.assertEqual(5, item.sell_in)
        self.assertEqual(22, item.quality)

    def test_five_days(self):
        item = Item(ITEM_NAME, 5, 20)

        GildedRose([item]).update_quality()

        self.assertEqual(4, item.sell_in)
        self.assertEqual(23, item.quality)

    def test_expired_pass(self):
        item = Item(ITEM_NAME, 0, 20)

        GildedRose([item]).update_quality()

        self.assertEqual(-1, item.sell_in)
        self.assertEqual(0, item.quality)

    def test_quality_does_not_exceed_fifty(self):
        item = Item(ITEM_NAME, 5, 49)

        GildedRose([item]).update_quality()

        self.assertEqual(4, item.sell_in)
        self.assertEqual(50, item.quality)


if __name__ == '__main__':
    unittest.main()
