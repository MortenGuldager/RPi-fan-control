#!/bin/bash
sudo aptitude -y install python3-venv
sudo -k
python3 -m venv venv
venv/bin/pip install gpiozero RPi.GPIO