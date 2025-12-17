#!/usr/bin/env python3
import subprocess
import sys
import os

def setup_nginx(domain):
    config_path = f"/etc/nginx/sites-available/{domain}"
    enabled_link = f"/etc/nginx/sites-enabled/{domain}"

    config_content = f"""server {{
    listen 80;
    server_name {domain};

    location / {{
        proxy_pass http://localhost:3000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }}
}}
"""

    try:
        print(f"Creating Nginx config for {domain}...")
        with open(config_path, 'w') as f:
            f.write(config_content)

        print("Enabling site...")
        if os.path.exists(enabled_link):
            subprocess.run(['sudo', 'rm', enabled_link], check=True)
        subprocess.run(['sudo', 'ln', '-s', config_path, enabled_link], check=True)

        print("Testing Nginx configuration...")
        subprocess.run(['sudo', 'nginx', '-t'], check=True)

        print("Restarting Nginx...")
        subprocess.run(['sudo', 'systemctl', 'restart', 'nginx'], check=True)

        print(f"Nginx setup for {domain} completed.")
    except subprocess.CalledProcessError as e:
        print(f"Error during setup: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 setup_nginx.py <domain>")
        sys.exit(1)

    domain = sys.argv[1]
    setup_nginx(domain)