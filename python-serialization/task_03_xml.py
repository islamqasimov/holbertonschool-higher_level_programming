#!/usr/bin/python3
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serialize a Python dictionary to XML and save it to a file.
    """

    root = ET.Element('data')

    for key, val in dictionary.items():
        sub = ET.SubElement(root, key)
        sub.text = str(val)

    try:
        tree = ET.ElementTree(root)
        tree.write(filename, encoding="unicode")
        return True
    except FileNotFoundError:
        return False


def deserialize_from_xml(filename):
    """
    Read XML from file and return a Python dictionary.
    """

    tree = ET.parse(filename)
    root = tree.getroot()

    result = {}
    for child in root:
        result[child.tag] = child.text

    return result
