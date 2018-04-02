from threading import Thread, Lock
from src import XMLtoObjectConvertor, FileProcessor,\
    WebSiteLoader, PageParser, GoodsStorage


def parse(desc):
    loader = loader = WebSiteLoader(desc)
    while not loader.is_all_pages_loaded():
        page = loader.get_next_page()
        goods = PageParser.parse(page, desc.paths, desc.trash)
        lock.acquire()
        storage.extend(goods)
        lock.release()
    del loader


storage = GoodsStorage()
lock = Lock()

input_data = FileProcessor.read('input.xml')
sites = XMLtoObjectConvertor.convert(input_data)

threads = []

for site_desc in sites.getchildren():
    thread = Thread(target=parse, args=(site_desc,))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

output_data = storage.to_XML_string()
FileProcessor.write('output.xml', output_data)
