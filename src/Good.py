from lxml import etree


class Good:
    def __init__(self, title, price):
        self.__title = title
        self.__min_price = self.__max_price = price

    def title(self):
        return self.__title

    def price(self):
        if self.__min_price == self.__max_price:
            return self.__min_price

    def min_price(self):
        return self.__min_price

    def max_price(self):
        return self.__max_price

    def __eq__(self, other):
        if not isinstance(other, Good):
            return False
        return self.__distance(other) <= 3

    def try_update_prices(self, price):
        if self.__min_price > price:
            self.__min_price = price
        elif self.__max_price < price:
            self.__max_price = price

    def __distance(self, other):
        a = self.__title
        b = other.__title
        n, m = len(a), len(b)
        if n > m:
            a, b = b, a
            n, m = m, n
        current_row = range(n+1)
        for i in range(1, m+1):
            previous_row, current_row = current_row, [i]+[0]*n
            for j in range(1, n+1):
                add, delete, change = previous_row[j]+1,\
                    current_row[j-1]+1, previous_row[j-1]
                if a[j-1] != b[i-1]:
                    change += 1
                current_row[j] = min(add, delete, change)
        return current_row[n]

    def to_XML(self):
        root = etree.Element('notebook')
        title = etree.Element('title')
        title.text = self.__title
        root.append(title)
        min_price = etree.Element('min_price')
        min_price.text = str(self.__min_price)
        root.append(min_price)
        max_price = etree.Element('max_price')
        max_price.text = str(self.__max_price)
        root.append(max_price)
        return root

    def __str__(self):
        return '{} : {} - {} uah'\
            .format(self.title(), self.__min_price, self.__max_price)

    def __repr__(self):
        return self.__str__()
