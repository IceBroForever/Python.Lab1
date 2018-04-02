from lxml import etree
from src.Good import Good


class GoodsStorage:
    def __init__(self):
        self.__storage = []

    def add(self, good):
        if not isinstance(good, Good):
            return
        finded = None
        for current in self.__storage:
            if current == good:
                finded = current
                break
        if finded is not None:
            finded.try_update_prices(good.price())
        else:
            self.__storage.append(good)

    def extend(self, goods):
        for good in goods:
            self.add(good)

    def to_XML_string(self):
        root = etree.Element('storage')
        for notebook in self.__storage:
            root.append(notebook.to_XML())
        return etree.tostring(root, pretty_print=True, encoding = "unicode")

    def __str__(self):
        string = ''
        for good in self.__storage:
            string += str(good) + '\n'
        return string

    def __repr__(self):
        return self.__str__()
