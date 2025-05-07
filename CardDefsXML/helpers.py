from lxml import etree
from lxml.etree import Element


def pprint(element: Element):
    print(etree.tostring(element, pretty_print=True, encoding='unicode'))

