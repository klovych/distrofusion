#!/usr/bin/env python3

import os
import subprocess
import click
import sys
import configparser

def check_root():
    if os.geteuid() != 0:
        print("Run this with sudo, please!")
        sys.exit(1)

BASE_DIR = "/distrofusion"
STRATA_DIR = f"{BASE_DIR}/strata"
OVERLAY_DIR = f"{BASE_DIR}/overlay"
FUSION_DIR = f"{BASE_DIR}/fusion"

def read_config():
    config = configparser.ConfigParser()
    config.read("fusion.conf")
    return (
        config.get("layers", "arch", fallback="base"),
        config.get("layers", "debian", fallback="coreutils")
    )

def setup_dirs():
    for d in [f"{STRATA_DIR}/arch", f"{STRATA_DIR}/debian", f"{OVERLAY_DIR}/upper", f"{OVERLAY_DIR}/work", FUSION_DIR]:
        os.makedirs(d, exist_ok=True)

def setup_debian_sources():
    sources_list = f"{STRATA_DIR}/debian/etc/apt/sources.list"
    with open(sources_list, "w") as f:
        f.write("deb http://deb.debian.org/debian stable main contrib non-free non-free-firmware\n")
        f.write("deb http://deb.debian.org/debian-security stable-security main contrib non-free non-free-firmware\n")
    print(f"Set up {sources_list}")

# Put the layers together
def install_layers(arch_packages, debian_packages):
    try:
        print("Putting in the Arch layer...")
        arch_pkgs = [pkg.strip() for pkg in arch_packages.split(",")] + ["bash", "sudo"]
        result = subprocess.run(["pacstrap", "-i", f"{STRATA_DIR}/arch"] + arch_pkgs + ["--noconfirm"], capture_output=True, text=True)
        if result.returncode != 0:
            print(f"Pacstrap failed:\n{result.stdout}\n{result.stderr}")
            raise subprocess.CalledProcessError(result.returncode, result.args)
    except subprocess.CalledProcessError as e:
        print(f"Arch setup failed: {e}")
        sys.exit(1)
    
    try:
        print("Putting in the Debian layer...")
        result = subprocess.run(["debootstrap", "stable", f"{STRATA_DIR}/debian", "http://deb.debian.org/debian"], capture_output=True, text=True)
        if result.returncode != 0:
            print(f"Debootstrap failed:\n{result.stdout}\n{result.stderr}")
            raise subprocess.CalledProcessError(result.returncode, result.args)
        setup_debian_sources()
        print("Updating apt...")
        subprocess.run(["chroot", f"{STRATA_DIR}/debian", "apt", "update"], check=True)
        debian_pkgs = [pkg.strip() for pkg in debian_packages.split(",")] + ["bash", "sudo", "apt", "libapt-pkg6.0", "libmd0", "debconf", "dpkg"]
        print(f"Putting in Debian stuff: {debian_pkgs}")
        subprocess.run(["chroot", f"{STRATA_DIR}/debian", "apt", "install", "-y"] + debian_pkgs, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Debian setup failed: {e}")
        sys.exit(1)

def mount_fusion():
    print("Mixing the layers...")
    lower_dirs = f"{STRATA_DIR}/debian:{STRATA_DIR}/arch"
    try:
        result = subprocess.run([
            "mount", "-t", "overlay", "overlay",
            "-o", f"lowerdir={lower_dirs},upperdir={OVERLAY_DIR}/upper,workdir={OVERLAY_DIR}/work",
            FUSION_DIR
        ], capture_output=True, text=True, check=True)
        print(f"Mixing worked: {result.stdout}")
        if not os.path.exists(f"{FUSION_DIR}/bin/bash"):
            print(f"Oops, /bin/bash not found in {FUSION_DIR}")
            sys.exit(1)
    except subprocess.CalledProcessError as e:
        print(f"Mixing failed: {e}\nOutput: {e.stdout}\nError: {e.stderr}")
        sys.exit(1)

def mount_system_dirs():
    print("Connecting important folders...")
    for src, dest in [("/dev", f"{FUSION_DIR}/dev"), ("/dev/pts", f"{FUSION_DIR}/dev/pts"), 
                      ("/proc", f"{FUSION_DIR}/proc"), ("/sys", f"{FUSION_DIR}/sys"), 
                      ("/etc/resolv.conf", f"{FUSION_DIR}/etc/resolv.conf")]:
        subprocess.run(["mount", "--bind", src, dest], check=True)

def cleanup():
    print("Cleaning up...")
    for dest in [f"{FUSION_DIR}/etc/resolv.conf", f"{FUSION_DIR}/sys", f"{FUSION_DIR}/proc", f"{FUSION_DIR}/dev/pts", f"{FUSION_DIR}/dev"]:
        subprocess.run(["umount", dest], check=False)
    subprocess.run(["umount", FUSION_DIR], check=False)

@click.group()
def cli():
    check_root()

@cli.command()
def create():
    """Makes the DistroFusion layers"""
    arch_pkgs, debian_pkgs = read_config()
    setup_dirs()
    install_layers(arch_pkgs, debian_pkgs)

@cli.command()
def run():
    """Runs the mixed-up system"""
    mount_fusion()
    mount_system_dirs()
    print("Starting the system... To leave, press Ctrl+D or type 'exit'")
    chroot_cmd = ["/usr/bin/chroot", FUSION_DIR, "/bin/bash", "-c", 
                  f"export PATH=/usr/local/sbin:/usr/sbin:/sbin:/usr/local/bin:/usr/bin:/bin && "
                  f"export LD_LIBRARY_PATH={STRATA_DIR}/arch/usr/lib:{STRATA_DIR}/arch/lib:/usr/lib/x86_64-linux-gnu:/lib/x86_64-linux-gnu && "
                  "exec /bin/bash"]
    process = subprocess.Popen(chroot_cmd, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr)
    process.wait()
    cleanup()

@cli.command()
def clean():
    """Cleans up the system"""
    cleanup()

if __name__ == "__main__":
    cli()