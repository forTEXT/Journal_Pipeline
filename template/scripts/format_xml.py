import sys
import xml.etree.ElementTree as ET

# Function to add align="left" and valign="top" attributes to <td> and <th> tags
def add_align_valign_to_table(xml_file):
    # Parse the XML file
    tree = ET.parse(xml_file)
    root = tree.getroot()

    # Iterate over all elements and add the attributes to <td> and <th> tags
    for elem in root.iter():
        if elem.tag == 'td' or elem.tag == 'th':
            elem.set('align', 'left')
            elem.set('valign', 'top')

    # Save the modified XML file with the same name
    tree.write(xml_file, encoding="utf-8", xml_declaration=True)

    print(f"The XML file '{xml_file}' has been successfully modified.")

if __name__ == "__main__":
    # Ensure that the XML file path is provided as an argument
    if len(sys.argv) != 2:
        print("Usage: python format_xml.py <xml_file_path>")
        sys.exit(1)

    # Read the XML file path from command line argument
    xml_file = sys.argv[1]

    try:
        # Call the function to format the table in the XML file
        add_align_valign_to_table(xml_file)
    except Exception as e:
        print(f"Error while modifying the XML file: {e}")
        sys.exit(1)
