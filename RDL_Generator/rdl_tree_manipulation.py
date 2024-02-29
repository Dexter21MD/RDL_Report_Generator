from lxml import etree


class Rdl_Tree_Manipulation:
    def __init__(self, root=None):
        self.lxml_element_root = root

    def get_rid_of_namespaces(self):
        for element in self.lxml_element_root.iter():
            if not (isinstance(element,  etree._Comment) or isinstance(element, etree._ProcessingInstruction)):
                element.tag = etree.QName(element).localname
        return self.lxml_element_root
