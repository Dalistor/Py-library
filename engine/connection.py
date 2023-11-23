from engine.models import Library

import xml.etree.ElementTree as ET

data_address = 'data/data.xml'
tables = ['client', 'book']

def creatXML(object: dict, name: str):
    root = ET.Element(name)

    for key, value in object.items():
        root_value = ET.SubElement(root, key)
        root_value.text = str(value)

    return root

def getEntityXML(file_address: str, local: str, all: bool = False):
    tree = ET.parse(file_address)
    root = tree.getroot()

    tags = None
    if all:
        tags = root.findall(f'.//{local}')
    else:
        tags = root.find(f'.//{local}s')

    return tree, root, tags

class DataConnection():
    def remember():
        for value in tables:
            _, _, tags = getEntityXML(file_address=data_address, local=value, all=True)

            for tag in tags:
                elements = {el.tag: el.text for el in tag}

                if value == 'client':
                    Library.Client(elements)
                elif value == 'book':
                    Library.Book(elements)


    def save(object: dict, local: str):
        info = creatXML(object=object, name=local)

        tree, _, tag = getEntityXML(file_address='data/data.xml', local=local)

        tag.append(info)
        tree.write('data/data.xml')

    def find_entity(field: str, key: str, value):
        _, _, tags = getEntityXML(file_address=data_address, local=field, all=True)

        result = []
        for tag in tags:
            tag_value = tag.find(key).text

            if tag_value == value:
                result.append({el.tag: el.text for el in tag})

        return result
