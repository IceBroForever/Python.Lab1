from lxml import etree
from src import WebSiteLoader, XMLtoObjectConvertor, FileProcessor


def test_loader():
    desc_str = FileProcessor.read('tests/test_data/test_loader.xml')
    desc = XMLtoObjectConvertor.convert(desc_str)
    loader = WebSiteLoader(desc)

    assert loader.is_all_pages_loaded() == False

    i = 1
    n = int(desc.limit.text)
    while i <= n:
        page = loader.get_next_page()
        parser = etree.HTMLParser()
        page_tree = etree.fromstring(page, parser)
        print(page_tree.xpath(desc.path.text))
        assert page_tree.xpath(desc.path.text)[0] == desc.expected[i-1].text
        i += 1

    assert loader.is_all_pages_loaded() == True
