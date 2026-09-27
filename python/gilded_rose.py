
class GildedRose:
    def __init__(self, items):
        self.items = items
        self._handlers = {
            "Aged Brie": self._update_aged_brie,
            "Backstage passes to a TAFKAL80ETC concert": self._update_backstage_pass,
            "Sulfuras, Hand of Ragnaros": self._update_sulfuras,
        }

    def update_quality(self):
        for item in self.items:
            handler = self._handlers.get(item.name, self._update_standard_item)
            if item.name.startswith("Conjured "):
                handler = self._update_conjured_item
            handler(item)

    def _update_standard_item(self, item):
        self._update_degrading_item(item, 1)

    def _update_conjured_item(self, item):
        self._update_degrading_item(item, 2)

    def _update_degrading_item(self, item, degradation):
        if item.quality > 0:
            item.quality = max(0, item.quality - degradation)
        item.sell_in = item.sell_in - 1
        if item.sell_in < 0 and item.quality > 0:
            item.quality = max(0, item.quality - degradation)

    def _update_aged_brie(self, item):
        if item.quality < 50:
            item.quality = item.quality + 1
        item.sell_in = item.sell_in - 1
        if item.sell_in < 0 and item.quality < 50:
            item.quality = item.quality + 1

    def _update_backstage_pass(self, item):
        if item.quality < 50:
            item.quality = item.quality + 1
            if item.sell_in < 11 and item.quality < 50:
                item.quality = item.quality + 1
            if item.sell_in < 6 and item.quality < 50:
                item.quality = item.quality + 1
        item.sell_in = item.sell_in - 1
        if item.sell_in < 0:
            item.quality = item.quality - item.quality

    def _update_sulfuras(self, item):
        pass


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return f"{self.name}, {self.sell_in}, {self.quality}"
