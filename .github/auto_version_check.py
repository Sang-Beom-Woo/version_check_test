import os
import re
import sys
from lxml import etree

# Read the CHANGELOG.rst file
desired_version = sys.argv[1]

# Step 1: Read the CHANGELOG.rst file
with open('../CHANGELOG.rst', 'r') as file:
    changelog = file.read()

error = False

# Step 2: Find the CHANGELOG.rst version
version_pattern = re.compile(r'\d+\.\d+\.\d+')
changelog_version = version_pattern.findall(changelog)[0]
if changelog_version != desired_version :
    print('version check error in CHANGELOG.rst \t expected: ',desired_version,' actual: ',changelog_version)
    error = True

# Step 3: Find all package.xml files in directory
for root, dirs, files in os.walk('..'):
    for file in files:
        if file == 'package.xml':
            package_xml_path = os.path.join(root, file)

            # Step 4: Open each package.xml and update the version information
            tree = etree.parse(package_xml_path)
            root = tree.getroot()

            for version_tag in root.iter('version'):
                if version_tag.text != desired_version :
                    print('version check error in', package_xml_path, '\t expected: ', desired_version ,' actual: ', version_tag.text)
                    error = True
if not error :
    print('no error in version number')
sys.exit(error)
