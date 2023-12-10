#!/bin/bash

# Get user input for book details
echo ""
echo "---- Start conversion into E-Book file ----"
echo ""

# sets library position
export LD_LIBRARY_PATH=`pwd`/Resources/calibre-bin/calibre/lib

while true; do
    read -p "Enter the filename without the suffix: " filename
    fullPath=`pwd`/"Books/HTML/${filename}.html"

    if [ -e "$fullPath" ]; then
        echo "File exists: $fullPath"
        # Additional commands for when the file exists
        break  # Exit the loop because the file exists
    else
        echo "File does not exist: $fullPath"
        # Additional commands for when the file does not exist
    fi
done

echo ""
echo "---- Set E-Book metadata ----"
echo ""
read -p "Enter the title: " title
read -p "Enter the author: " author
echo ""

# define epub output file path
fullPathOutput=`pwd`/"Books/EPUB/${filename}.epub"

cd Resources/calibre-bin/calibre/bin
./ebook-convert "${fullPath}" "${fullPathOutput}" --authors "${author}" --input-encoding utf-8 --title "${title}" --output-profile generic_eink_hd

echo ""
echo "---- Conversion complete! ----"
echo ""
