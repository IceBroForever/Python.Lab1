from src import XMLtoObjectConvertor


def test_convertor():
    xml_str = """<outer>
    <inner>child</inner>
</outer>"""
    xml = XMLtoObjectConvertor.convert(xml_str)
    assert xml.inner.text == 'child'