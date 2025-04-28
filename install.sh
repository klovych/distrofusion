#!/bin/bash

echo "Hey! Let’s set up DistroFusion on Arch!"

if [ "$EUID" -ne 0 ]; then
    echo "Please run this with sudo, like: sudo ./install.sh"
    exit 1
fi

echo "Updating Arch..."
pacman -Syu --noconfirm

if ! command -v python &> /dev/null; then
    echo "Python not found. Installing it..."
    pacman -S --noconfirm python
else
    echo "Python is good!"
fi

if ! command -v pip &> /dev/null; then
    echo "Pip not found. Installing it..."
    pacman -S --noconfirm python-pip
else
    echo "Pip is good!"
fi

echo "Getting the click tool for Python..."
pacman -S python-click

if ! command -v pacstrap &> /dev/null; then
    echo "Pacstrap not found. Installing it..."
    pacman -S --noconfirm arch-install-scripts
else
    echo "Pacstrap is good!"
fi

if ! command -v debootstrap &> /dev/null; then
    echo "Debootstrap not found. Installing it..."
    pacman -S --noconfirm debootstrap
else
    echo "Debootstrap is good!"
fi
echo "Downloading distrofusion.py..."
wget -O distrofusion.py https://github.com/klovych/distrofusion/main/distrofusion.py
chmod +x distrofusion.py

echo "All set! Now run it with: sudo ./distrofusion.py create"
echo "Then try: sudo ./distrofusion.py run"