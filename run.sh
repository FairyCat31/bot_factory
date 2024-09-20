#!/bin/bash

source env/bin/activate
python3 app/scripts/main.py -launch_bot --name=Test

read -p "Press any key..."
