# 🌌 DistroFusion: Mix Arch & Debian Like Magic! 🪄

Hey there! Welcome to **DistroFusion**, a super cool tool that lets you **combine Arch Linux and Debian** into one awesome system. 🚀 Want to use `pacman` *and* `apt` in the same place? This is for you! 

Built for Arch Linux users, it’s easy to set up with our auto-installer. Let’s dive in! 😎

## 🎉 What’s DistroFusion?

DistroFusion creates a special environment where:
- **Arch Linux** brings its speedy, cutting-edge vibe.
- **Debian** adds its stable, reliable tools.
- You get to use **both** in one system, thanks to overlayfs magic! ✨

It’s like mixing your favorite snacks into one epic bowl. 🍕 + 🍔 = 😋

## 🛠️ How to Get Started

###Step 1: Grab the Installer
Open your terminal and run:

```bash
wget -O install.sh https://github.com/klovych/distrofusion/install.sh

###Step2: Make it ready
Give the script permission to run:
```bash
chmod +x install.sh

###Step 3: Run the magic:
Use sudo to start the installer:
```bash
sudo ./install.sh

This will grab everything you need, including distrofusion.py and fusion.conf

###Step4: Create the fusion:
Build the mixed system:
```bash
sudo ./distrofusion.py create

###Step5: Jump in:
Start the fused environment:
```bash
sudo ./distrofusion.py run


Now you are in, you can try commands like:
```bash
/bin/bash --version # Check Arch's bash
apt update # Use Debian's apt package manager
sudo apt install fastfetch # Install cool stuff or application

To leave from environment, type exit.

🖼️ What It Looks Like
Imagine this in your terminal:
Mixing the layers...
Mixing worked!
Starting the system... To leave, press Ctrl+D or type 'exit'
[root@fusion ~]# apt update
Hit:1 http://deb.debian.org/debian stable InRelease
[root@fusion ~]# pacman -Syu
:: Synchronizing package databases...


🌟 Why It’s Awesome
Mixes Two Worlds: Arch’s speed + Debian’s stability.
Easy Setup: One script does it all.
Learn Linux: Play with two distros at once!
For Hackers & Geeks: Experiment with overlayfs and chroot.


🛡️ Requirements
Arch Linux (sorry, other distros not yet!)
Sudo powers
Internet connection


