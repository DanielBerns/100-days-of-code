import xml.etree.cElementTree as ET

# https://riptutorial.com/python/example/29019/searching-the-xml-with-xpath

RESOURCE = 'catalog.xml'

def first_example():
    tree = ET.parse(RESOURCE)
    books = tree.findall('Books/Book')
    for bb in books:
        print(bb.tag)
        for key, value in bb.items():
            print(key, value)
        for child in bb:
            print(child.tag, child.text)
    cc = tree.find("Books/Book[Title='The Colour of Magic']")
    print(cc.tag)
    for key, value in cc.items():
        print(key, value)    

if __name__ == '__main__':
    first_example()
