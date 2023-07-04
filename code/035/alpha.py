import xml.etree.ElementTree as ET


def extract_tags(xml_file, tags):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    extracted_data = {}
    for tag in tags:
        extracted_data[tag] = []

    for elem in root.iter():
        if elem.tag in tags:
            extracted_data[elem.tag].append(elem.text)

    return extracted_data

# Example usage
xml_file_path = "./example.xml"
tags_to_extract = ["name", "age", "city"]

data = extract_tags(xml_file_path, tags_to_extract)

# Print extracted data
for tag, values in data.items():
    print(tag + ":")
    for value in values:
        print(value)
    print()
 
