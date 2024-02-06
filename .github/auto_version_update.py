import os
import re
from lxml import etree

# Step 1: Read the CHANGELOG.rst file
with open('../CHANGELOG.rst', 'r') as file:
    changelog = file.read()

# Step 2: Find the first version
version_pattern = re.compile(r'\d+\.\d+\.\d+')
version = version_pattern.findall(changelog)[0]

# Step 3: Find all package.xml files in aimbot_base directory
for root, dirs, files in os.walk('..'):
    for file in files:
        if file == 'package.xml':
            package_xml_path = os.path.join(root, file)

            # Step 4: Open each package.xml and update the version information
            tree = etree.parse(package_xml_path)
            root = tree.getroot()

            for version_tag in root.iter('version'):
                version_tag.text = version

            # Step 5: Save the changes to the package.xml file
            tree.write(package_xml_path, xml_declaration=True, encoding='utf-8')
