#!/usr/bin/env bash
# A bash script that sets up nginx for deployment of static content

# Upadate dependencies
sudo apt update

# Install nginx
if ! nginx -v > /dev/null 2>&1; then
    sudo apt-get install -y nginx
fi

# Check nginx status, start nginx service
sudo service nginx status || sudo service nginx start

# create directories if it doesn’t already exist
# -p flag avoids error if folder already exists
mkdir -p "/data/web_static/shared/"
mkdir -p "/data/web_static/releases/test/"

# Create HTML file with static content.
echo  "Welcome to Ej Farms" > "/data/web_static/releases/test/index.html"

# Create a symbolic link /data/web_static/current 
# linking to /data/web_static/releases/test/
ln -sf "/data/web_static/releases/test/" "/data/web_static/current"

# Granting ownership and permissions
sudo chown -R ubuntu:ubuntu "/data/"

# Update nginx config to serve /data/web_static/current/
sudo tee /etc/nginx/sites-available/hbnb_static > /dev/null <<EOF
server {
    listen 80;
    server_name egbuniwefarms.tech;

    location /hbnb_static/ {
        alias /data/web_static/current/;
        autoindex on;
    }
}
EOF

# Link configuration file to sites-enabled if not installed
if [ ! -L /etc/nginx/sites-enabled/hbnb_static ]; then
    sudo ln -s "/etc/nginx/sites-available/hbnb_static" "/etc/nginx/sites-enabled/"
fi

# Restart nginx
sudo service nginx restart