#!/bin/bash

echo ""
echo "---- Installs required packages ----"
echo ""

wget -nv -O- https://download.calibre-ebook.com/linux-installer.sh | sh /dev/stdin install_dir=Resources/calibre-bin isolated=y

echo ""
echo "---- Creates book folders ----"
echo ""
mkdir Books
mkdir Books/HTML
mkdir Books/EPUB
echo ""