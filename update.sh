#!/bin/bash
echo "Update start...."
git submodule init
git submodule update
cd batti
./configure
sudo make install
echo "Update complete."
