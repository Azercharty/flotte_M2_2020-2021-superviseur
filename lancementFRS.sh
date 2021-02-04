#!/bin/bash
# type:launcher
# date: 2021

echo "Activation de la Flotte"

#sudo service mysql stop
#sudo service mosquito stop
sudo docker-compose up -d

cd /workspace
cd /Superviseur
python main.py
