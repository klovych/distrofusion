# 🌟 DistroFusion: mix arch and debian together

Hello dear linux user **DistroFusion** is a fun tool that puts **Arch Linux** and **Debian** into one system. 🖥️ You can use `pacman` and `apt` at the same time! It is super easy to set up on Arch Linux. 🚀

## ❓ What is DistroFusion?

DistroFusion makes a special place where:
- **Arch Linux** gives you fast, new stuff.
- **Debian** gives you stable, trusty stable tools.
- They work together like magic! 🪄

It is like mixing ice cream and cookies — yum! 🍦🍪

## 🛠️ How install it

Here is how to get DistroFusion on **Arch Linux**. It is just a few steps!

### 1. Get the installer
Open your terminal and type:

```bash
wget -O install.sh https://raw.githubusercontent.com/klovych/distrofusion/main/install.sh
```

### 2. Make it ready
Tell the computer it’s okay to run the script:

```bash
chmod +x install.sh
```

### 3. Start the installer
Run it with sudo (like a boss):

```bash
sudo ./install.sh
```

This grabs `distrofusion.py` and `fusion.conf`, and sets up tools like `python-click`, `pacstrap`, and `debootstrap`.

### 4. Build the Mix
Make the Arch-Debian mix:

```bash
sudo ./distrofusion.py create
```

### 5. Jump In!
Start the mixed system:

```bash
sudo ./distrofusion.py run
```

Now you are in! Try these:

```bash
/bin/bash --version  # Check Arch’s bash
apt update          # Get Debian’s updates
sudo apt install fastfetch  # Add a cool tool
```

To leave, type `exit` or press `Ctrl+D`.

## 🖼️ What you will see

Your terminal will look like this:

```bash
Mixing the layers...
Mixing worked!
Starting the system... To leave, press Ctrl+D or type 'exit'
[root@fusion ~]# apt update
Hit:1 http://deb.debian.org/debian stable InRelease
[root@fusion ~]# /bin/bash --version
GNU bash, version 5.2.21(1)-release
```


## 🌈 Why It is fun

- **Two Systems in One**: Arch’s speed + Debian’s calm.
- **Easy to Use**: Just one script!
- **Learn Stuff**: Play with Linux tricks.
- **For Geeks**: Try new things!

## ✅ What you need

- **Arch Linux** (won’t work on others yet)
- Sudo powers
- Internet

## 🐞 Got a problem?

- **Something broke?** Tell me on [GitHub Issues](https://github.com/klovych/distrofusion/issues).
- **Confused?** Ask on GitHub.

## 📝 License

DistroFusion is free to use under the [MIT License](LICENSE). Share and have fun! 🎉

---
