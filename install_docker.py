#!/usr/bin/env python3
import subprocess
import sys

def install_docker():
    try:
        print("Updating package list...")
        subprocess.run(['sudo', 'apt', 'update'], check=True)

        print("Installing Docker...")
        subprocess.run(['sudo', 'apt', 'install', '-y', 'docker.io'], check=True)

        print("Installing Docker Compose...")
        subprocess.run(['sudo', 'apt', 'install', '-y', 'docker-compose'], check=True)

        print("Starting Docker service...")
        subprocess.run(['sudo', 'systemctl', 'start', 'docker'], check=True)
        subprocess.run(['sudo', 'systemctl', 'enable', 'docker'], check=True)

        print("Adding user to docker group...")
        subprocess.run(['sudo', 'usermod', '-aG', 'docker', '$USER'], check=True)

        print("Docker and Docker Compose installation completed.")
    except subprocess.CalledProcessError as e:
        print(f"Error during installation: {e}")
        sys.exit(1)

if __name__ == "__main__":
    install_docker()