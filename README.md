# Cloud Automation Express Demo

A simple Express.js application that serves static files with a beautiful home page.

## Features

- Express.js web server
- Static file serving
- Bootstrap 5 UI
- Docker containerization

## Local Development

### Prerequisites
- Node.js 18+
- npm

### Installation
```bash
npm install
```

### Running
```bash
npm start
```

The application will be available at `http://localhost:3000`

## Docker Deployment

### Using Docker Compose (Recommended)

```bash
# Build and run the application
docker-compose up -d

# View logs
docker-compose logs -f

# Stop the application
docker-compose down
```

### Using Docker directly

```bash
# Build the image
docker build -t ca-demo-express .

# Run the container
docker run -p 3000:3000 --name ca-demo-express ca-demo-express

# Run in background
docker run -d -p 3000:3000 --name ca-demo-express ca-demo-express
```

### Docker Commands

```bash
# Check container status
docker ps

# View container logs
docker logs ca-demo-express

# Stop container
docker stop ca-demo-express

# Remove container
docker rm ca-demo-express

# Remove image
docker rmi ca-demo-express
```

## Environment Variables

- `PORT`: Server port (default: 3000)
- `NODE_ENV`: Environment (default: development)

## Health Check

The application includes a health check endpoint that can be used by Docker and orchestration tools.

## AWS EC2 Deployment

### Prerequisites
- AWS Account with EC2 access
- SSH key pair for EC2 instance access
- Basic knowledge of AWS console or AWS CLI

### Step 1: Launch EC2 Instance

1. **Log in to AWS Console** and navigate to EC2 service
2. **Click "Launch Instance"**
3. **Choose AMI**: Amazon Linux 2 or Ubuntu Server (latest LTS)
4. **Instance Type**: t2.micro (free tier) or t3.small for better performance
5. **Configure Security Group**:
   - Add rule: HTTP (port 80) from 0.0.0.0/0
   - Add rule: SSH (port 22) from your IP or 0.0.0.0/0
   - Add rule: Custom TCP (port 3000) from 0.0.0.0/0 (for direct access)
6. **Launch the instance** and note the Public IP/DNS

### Step 2: Connect to EC2 Instance

```bash
# Connect using SSH (replace with your key and instance details)
ssh -i your-key.pem ec2-user@your-instance-public-ip

# For Ubuntu instances, use:
ssh -i your-key.pem ubuntu@your-instance-public-ip
```

### Step 3: Install Docker on EC2

```bash
# Update system packages
sudo yum update -y  # For Amazon Linux
# OR for Ubuntu:
sudo apt update && sudo apt upgrade -y

# Install Docker
sudo yum install -y docker  # Amazon Linux
# OR for Ubuntu:
sudo apt install -y docker.io

# Start and enable Docker service
sudo systemctl start docker
sudo systemctl enable docker

# Add current user to docker group (optional)
sudo usermod -aG docker $USER
# Logout and login again for group changes to take effect
```

### Step 4: Install Git and Clone Repository

```bash
# Install Git
sudo yum install -y git  # Amazon Linux
# OR for Ubuntu:
sudo apt install -y git

# Clone the repository
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name/ca_demo_express
```

### Step 5: Run the Application

```bash
# Build and run with Docker Compose
sudo docker-compose up -d

# OR run directly with Docker
sudo docker build -t ca-demo-express .
sudo docker run -d -p 3000:3000 --name ca-demo-express ca-demo-express
```

### Step 6: Configure Nginx (Optional - for production)

```bash
# Install Nginx
sudo yum install -y nginx  # Amazon Linux
# OR for Ubuntu:
sudo apt install -y nginx

# Create Nginx configuration
sudo tee /etc/nginx/conf.d/ca_demo_express.conf > /dev/null <<EOF
server {
    listen 80;
    server_name your-instance-public-ip;

    location / {
        proxy_pass http://localhost:3000;
        proxy_set_header Host \$host;
        proxy_set_header X-Real-IP \$remote_addr;
        proxy_set_header X-Forwarded-For \$proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto \$scheme;
    }
}
EOF

# Start Nginx
sudo systemctl start nginx
sudo systemctl enable nginx
```

### Step 7: Access Your Application

- **Direct access**: http://your-instance-public-ip:3000
- **Through Nginx**: http://your-instance-public-ip (if configured)

### Monitoring and Management

```bash
# Check container status
sudo docker-compose ps

# View application logs
sudo docker-compose logs -f

# Stop the application
sudo docker-compose down

# Update the application
git pull
sudo docker-compose up -d --build
```

### Troubleshooting

- **Port not accessible**: Check security group rules in AWS console
- **Container not starting**: Check logs with `docker-compose logs`
- **Permission denied**: Make sure Docker is running and user has permissions
- **Memory issues**: Consider upgrading instance type for production use

### Cost Optimization

- Use t2.micro for development/testing (free tier eligible)
- Stop instances when not in use
- Consider spot instances for non-critical workloads
- Set up auto-scaling for production applications

## Project Structure

```
ca_demo_express/
├── app.js                 # Main Express application
├── package.json           # Node.js dependencies
├── public/                # Static files
├── Dockerfile             # Docker image definition
├── docker-compose.yml     # Docker Compose configuration
├── .dockerignore          # Docker ignore file
├── nginx/                 # Nginx configuration
└── README.md             # This file
```

## API Endpoints

- `GET /`: Serves the home page

## Technologies Used

- **Runtime**: Node.js 18 Alpine
- **Framework**: Express.js
- **Frontend**: Bootstrap 5
- **Container**: Docker
- **Orchestration**: Docker Compose