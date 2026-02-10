#!/usr/bin/env python3
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serialize a Python dictionary to an XML file.

    Args:
        dictionary (dict): The dictionary to serialize.
        filename (str): The output XML filename.
    """
    root = ET.Element("data")

    for key, value in dictionary.items():
        # Convert value to string for XML storage
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=True)


def deserialize_from_xml(filename):
    """
    Deserialize XML file into a Python dictionary.

    Args:
        filename (str): The XML file to read.

    Returns:
        dict: The reconstructed dictionary.
    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()

        result = {}
        for child in root:
            text = child.text

            # Attempt basic type conversions
            if text is None:
                result[child.tag] = None
            elif text.lower() == "true":
                result[child.tag] = True
            elif text.lower() == "false":
                result[child.tag] = False
            else:
                try:
                    if "." in text:
                        result[child.tag] = float(text)
                    else:
                        result[child.tag] = int(text)
                except ValueError:
                    result[child.tag] = text  # fallback to string

        return result

    except (ET.ParseError, FileNotFoundError, OSError):
        return None
