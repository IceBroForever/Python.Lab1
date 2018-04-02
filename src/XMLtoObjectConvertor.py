from lxml import objectify as __obj


def convert(string: str):
    return __obj.fromstring(string)
