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
                    Library.Client._id = int(elements.get('id'))
                    Library.Client(elements)
                elif value == 'book':
                    Library.Book._id = int(elements.get('id'))
                    Library.Book(elements)


    def save(object: dict, local: str):
        info = creatXML(object=object, name=local)

        tree, _, tag = getEntityXML(file_address='data/data.xml', local=local)

        tag.append(info)
        tag.set('actualID', str(object.get('id')))
        tree.write('data/data.xml')

    def find(field: str, key: str, value):
        _, _, tags = getEntityXML(file_address=data_address, local=field, all=True)

        result = []
        for tag in tags:
            tag_value = tag.find(key).text

            if tag_value == value:
                result.append({el.tag: el.text for el in tag})

        return result

    def edit(values: list, field: str):
        tree, _, tags = getEntityXML(file_address=data_address, local=field, all=True)

        for tag in tags:
            if tag.find('id').text == values[0][1]:
                values.pop(0)

                for key, value in values:
                    tag.find(key).text = value
                    
                    tree.write(data_address)
                    
                break

    def remove(id: int, field: str):
        tree, root, tags = getEntityXML(file_address=data_address, local=field, all=True)

        for tag in tags:
            tag_id = int(tag.find('id').text)
            
            if tag_id == id:
                root = root.find(f'.//{field}s')

                root.remove(tag)
                tree.write(data_address)

                print(f"Tag com id={id} removida com sucesso.")
                break