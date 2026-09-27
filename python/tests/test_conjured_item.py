import unittest

from gilded_rose import Item, GildedRose

ITEM_NAME = "Conjured Mana Cake"


class ConjuredItemTest(unittest.TestCase):
    def test_conjured_item(self):
        item = Item(ITEM_NAME, 1, 20)

        GildedRose([item]).update_quality()

        self.assertEqual(0, item.sell_in)
        self.assertEqual(18, item.quality)

    def test_expired_conjured_item(self):
        item = Item(ITEM_NAME, 0, 20)

        GildedRose([item]).update_quality()

        self.assertEqual(-1, item.sell_in)
        self.assertEqual(16, item.quality)

    def test_already_expired_conjured_item(self):
        item = Item(ITEM_NAME, -1, 20)

        GildedRose([item]).update_quality()

        self.assertEqual(-2, item.sell_in)
        self.assertEqual(16, item.quality)

    def test_quality_does_not_go_negative(self):
        item = Item(ITEM_NAME, 1, 1)

        GildedRose([item]).update_quality()

        self.assertEqual(0, item.sell_in)
        self.assertEqual(0, item.quality)

    def test_expired_quality_does_not_go_negative(self):
        item = Item(ITEM_NAME, 0, 3)

        GildedRose([item]).update_quality()

        self.assertEqual(-1, item.sell_in)
        self.assertEqual(0, item.quality)

    def test_quality_stays_at_zero(self):
        item = Item(ITEM_NAME, 0, 0)

        GildedRose([item]).update_quality()

        self.assertEqual(-1, item.sell_in)
        self.assertEqual(0, item.quality)


if __name__ == '__main__':
    unittest.main()
