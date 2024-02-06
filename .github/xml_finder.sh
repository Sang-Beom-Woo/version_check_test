#!/bin/bash

# Set the root directory to start the search
root_directory="../"

# Find all package.xml files and loop through them
find "$root_directory" -type f -name "package.xml" | while read -r package_file; do
    # Extract the version number using grep and sed
    version=$(grep -oP '(?<=<version>)[^<]+' "$package_file" | sed -n 1p)

    # Set an environment variable with the version number
    export PACKAGE_VERSION="$version"

    # Display the result (optional)
    echo "Package.xml file: $package_file, Version: $PACKAGE_VERSION"
done
