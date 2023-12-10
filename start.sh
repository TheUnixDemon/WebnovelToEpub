#!/bin/bash

# check required resources
destinationFolder="Resources/calibre-bin"
if [ ! -d "$destinationFolder" ]; then
    # installs insolated resources
    ./Scripts/setup.sh
fi

# Create HTML mainfile
cd App/
python main.py

read -p "Do you want to convert a book now? (y/n): " response
if [[ $response == "y" ]]; then
    cd ..
    ./Scripts/convert.sh
else
    # Commands to execute if the response is not "yes"
    echo "Book conversion skipped."
fi

