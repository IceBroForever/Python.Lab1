import pytest
from lxml import etree
from src import Good


def test_constructor():
    title = "abc"
    price = 4
    good = Good(title, price)
    assert title == good.title()
    assert price == good.min_price()\
        == good.max_price() == good.price()


def test_tostring():
    title = "abc"
    price = 4
    good = Good(title, price)
    assert '{} : {} - {} uah'.format(title, price, price)\
        == str(good)


def test_repr():
    title = "abc"
    price = 4
    good = Good(title, price)
    assert '{} : {} - {} uah'.format(title, price, price)\
        == repr(good)


@pytest.mark.parametrize('a,b,expected', [
    (Good('abc', 1), None, False),
    (Good('abc', 1), Good('abc', 1), True),
    (Good('abc', 1), Good('abc', 2), True),
    (Good('Abc', 1), Good('abc', 2), True),
    (Good('Asus X555LAB', 1), Good('ASUS X555LAB', 2), True),
    (Good('Asus X566LCD', 1), Good('Asus X555LAB', 2), False)
])
def test_equals(a, b, expected):
    assert (a == b) == expected


@pytest.mark.parametrize('a,price,test_condition', [
    (Good('a', 1), 1, 'a.min_price() == a.max_price() == price'),
    (Good('a', 1), 2, 'a.max_price() == price'),
    (Good('a', 1), 0, 'a.min_price() == price')
])
def test_update(a, price, test_condition):
    a.try_update_prices(price)
    assert eval(test_condition)


def test_xml():
    title = 'a'
    price = 123
    root = etree.Element('notebook')
    title_element = etree.Element('title')
    title_element.text = title
    root.append(title_element)
    price_element = etree.Element('price')
    price_element.text = str(price)
    root.append(price_element)
    xpath = './title/text()'
    assert Good(title, price).to_XML().xpath(xpath) == root.xpath(xpath)
