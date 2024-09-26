#!/bin/bash

source env/bin/activate
python3 app/scripts/main.py -launch_bot --name=Test --debug_mode=True

read -p "Press any key..."
