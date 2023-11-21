import xml.etree.ElementTree as ET
import json

def creatXML(object: dict, name: str):
    root = ET.Element(name)

    for key, value in object.items():
        root_value = ET.SubElement(root, key)
        root_value.text = str(value)

    return root

def readXML(file_adress: str, local: str):
    tree = ET.parse(file_adress)
    root = tree.getroot()

    tag = root.find(f'.//{local}s')

    return tree, tag

class DataConnection():
    def remember():
        pass

    def save(object: dict, local: str):
        info = creatXML(object=object, name=local)

        tree, tag = readXML(file_adress='data/data.xml', local=local)

        tag.append(info)
        tree.write('data/data.xml')