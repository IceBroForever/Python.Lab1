import pytest
from src import GoodsStorage, Good


storage = None


def test_constructor():
    global storage
    storage = GoodsStorage()
    assert storage.size() == 0


@pytest.mark.parametrize('a,test_condition', [
    (None, 'storage.size() == 0'),
    (Good('abcde', 5), 'storage.size() == 1'),
    (Good('qwert', 5), 'storage.size() == 2'),
    (Good('Qwert', 4), 'storage.size() == 2 and storage[1].min_price() == 4'),
    (Good('AbCde', 8), 'storage.size() == 2 and storage[0].max_price() == 8')
])
def test_add(a, test_condition):
    global storage
    storage.add(a)
    assert eval(test_condition)

def test_extend():
    global storage
    n = storage.size()
    a = [Good('OPIKL', 10), Good('OPikL', 5)]
    storage.extend(a)
    assert storage.size() == n + 1
    assert storage[n].min_price() == 5

def test_xml():
    expected = """<storage>
  <notebook>
    <title>qwerty</title>
    <min_price>5</min_price>
    <max_price>5</max_price>
  </notebook>
</storage>
"""
    storage = GoodsStorage()
    storage.add(Good('qwerty', 5))
    assert storage.to_XML_string() == expected

def test_tostring():
    expected = """qwerty : 5 - 5 uah
poiuyy : 10 - 10 uah
"""
    storage = GoodsStorage()
    storage.add(Good('qwerty', 5))
    storage.add(Good('poiuyy', 10))
    assert str(storage) == expected
