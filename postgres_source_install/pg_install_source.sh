#!/usr/bin/bash

version=$1

# Add user
sudo useradd -d /home/payal -m -p postgres postgres
echo "user postgres added"

# Downloading requested postgres $1 source code to user home/downloads
wget https://ftp.postgresql.org/pub/source/v${version}/postgresql-${version}.tar.gz
tar -xvzf postgresql-${version}.tar.gz
echo "Source extracted"

# Install dependencies
sudo apt-get install zlib1g-dev
sudo apt-get install libreadline-dev
echo "Installed dependencies"

# Configure
cd postgresql-${version}
./configure
echo "Configured. Installing..."

# Make world
sudo make world
sudo make install-world
echo "Postgres installed"

# Creating data directory
sudo mkdir -p /usr/local/pgsql/data
sudo chown -R postgres:postgres /usr/local/pgsql/data
echo "Data directory created and owned by postgres"

# Initiliaze data directory
sudo su -c "/usr/local/pgsql/bin/initdb -D /usr/local/pgsql/data" postgres
echo "Data directory initialized"

# Start postgres
sudo su -c "/usr/local/pgsql/bin/pg_ctl -D /usr/local/pgsql/data start" postgres
echo "Database started"
