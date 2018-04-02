import pytest
from src import FileProcessor


def test_read():
    expected = '123456789qwerty'
    got = FileProcessor.read('tests/test_data/input.txt')
    assert got == expected


@pytest.mark.xfail(raises=FileNotFoundError)
def test_read_no_file():
    FileProcessor.read('1')


def test_write():
    output_file = 'tests/test_data/output.txt'
    data = 'qwerty123456789'
    FileProcessor.write(output_file, data)
    wrote = FileProcessor.read(output_file)
    assert wrote == data