🌌 DistroFusion: Blend Arch Linux & Debian Seamlessly
Welcome to DistroFusion, a powerful tool that combines Arch Linux and Debian into a single, unified environment. 🚀 Run pacman and apt side by side, all on your Arch Linux system! Designed for enthusiasts and tinkerers, it’s easy to set up with our auto-installer. Let’s get started! 😄
🎯 What is DistroFusion?
DistroFusion creates a unique environment where:

Arch Linux delivers its fast, bleeding-edge packages.
Debian provides stable, reliable tools.
Both work together using overlayfs, letting you enjoy the best of both worlds! ✨

🛠️ Installation Guide
Follow these steps to set up DistroFusion on Arch Linux. It’s quick and simple!
1. Download the Installer
Open your terminal and grab the installer script:
wget -O install.sh https://raw.githubusercontent.com/klovych/distrofusion/main/install.sh

2. Make It Executable
Give the script permission to run:
chmod +x install.sh

3. Run the Installer
Launch it with sudo (root privileges):
sudo ./install.sh

This downloads distrofusion.py and fusion.conf, plus installs dependencies like python-click, pacstrap, and debootstrap.
4. Create the Fusion
Build the combined Arch-Debian environment:
sudo ./distrofusion.py create

5. Enter the Fusion
Start the fused system:
sudo ./distrofusion.py run

Now you’re inside! Try these commands:
/bin/bash --version  # See Arch’s bash version
apt update          # Update Debian’s package lists
sudo apt install fastfetch  # Install a cool tool

To exit, type exit or press Ctrl+D.
📸 Example Output
Here’s what you’ll see in your terminal:
Mixing the layers...
Mixing worked!
Starting the system... To leave, press Ctrl+D or type 'exit'
[root@fusion ~]# apt update
Hit:1 http://deb.debian.org/debian stable InRelease
[root@fusion ~]# /bin/bash --version
GNU bash, version 5.2.21(1)-release (x86_64-pc-linux-gnu)

🌟 Why Use DistroFusion?

Dual Distro Power: Arch’s speed meets Debian’s stability.
Simple Setup: One script handles everything.
Learn Linux: Experiment with overlayfs, chroot, and multi-distro setups.
Geek-Friendly: Perfect for hackers, tinkerers, and Linux lovers.

🛡️ Requirements

Arch Linux (other distros not supported yet)
Sudo privileges
Internet connection

🐛 Need Help?

Found a bug? Report it on GitHub Issues.
Want to contribute? Fork the repo, make changes, and submit a pull request!
Questions? Open an issue or check the code.

📜 License
DistroFusion is open-source under the MIT License. Use it, share it, hack it! 🧑‍💻

Built with ❤️ by klovych. Enjoy fusing your distros! 🚀
