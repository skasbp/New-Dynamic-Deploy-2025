#!/usr/bin/env python3
import subprocess
import sys

def install_nginx():
    try:
        print("Updating package list...")
        subprocess.run(['sudo', 'apt', 'update'], check=True)

        print("Installing Nginx...")
        subprocess.run(['sudo', 'apt', 'install', '-y', 'nginx'], check=True)

        print("Starting Nginx service...")
        subprocess.run(['sudo', 'systemctl', 'start', 'nginx'], check=True)
        subprocess.run(['sudo', 'systemctl', 'enable', 'nginx'], check=True)

        print("Nginx installation completed.")
    except subprocess.CalledProcessError as e:
        print(f"Error during installation: {e}")
        sys.exit(1)

if __name__ == "__main__":
    install_nginx()