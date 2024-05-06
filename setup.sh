#!/bin/bash

# Kleurrijke output
echo -e "\e[1;33mInstalling required Python packages and modules...\e[0m"

# Controleer het besturingssysteem
if [ "$(uname)" == "Darwin" ]; then
    # Voor Mac
    echo -e "\e[1;33mMacOS Detected\e[0m"
    echo -e "\e[1;33mInstalling pip3...\e[0m"
    brew install python@3
elif [ "$(expr substr $(uname -s) 1 5)" == "Linux" ]; then
    # Voor Linux
    echo -e "\e[1;33mLinux Detected\e[0m"
    echo -e "\e[1;33mUpdating package list...\e[0m"
    sudo apt update
    echo -e "\e[1;33mInstalling python3-pip...\e[0m"
    sudo apt install python3-pip -y
else
    echo -e "\e[1;31mUnsupported Operating System\e[0m"
    exit 1
fi

# Installeer Python-modules
echo -e "\e[1;33mInstalling required Python modules...\e[0m"
pip3 install colorama google
pip3 install googlesearch-python
pip3 install requests
pip3 install beautifulsoup4

echo -e "\e[1;32mSetup complete!\e[0m"
