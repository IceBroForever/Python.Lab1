from lxml import etree as __et
import re as __re
from src.Good import Good


def __normilaze_title(name, trash):
    for t_reg in trash.getchildren():
        name = __re.sub(t_reg.text, '', name)
    return name.replace('  ', ' ').strip()


def __normilaze_price(price):
    return int(''.join(price.split(' ')))


def parse(page: str, paths: object, trash: object):
    parser = __et.HTMLParser()
    page_tree = __et.fromstring(page, parser)
    goods = []
    goods_elements = page_tree.xpath(paths.to_goods.text)
    for good_elements in goods_elements:
        try:
            title = __normilaze_title(good_elements
                    .xpath(paths.to_title.text)[0], trash)
            price = __normilaze_price(good_elements
                    .xpath(paths.to_price.text)[0])
            goods.append(Good(title, price))
        except Exception:
            pass
    return goods
