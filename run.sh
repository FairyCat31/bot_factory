#!/bin/bash

poetry env activate
export PYTHONPATH=$(pwd)
poetry run python app/scripts/main.py -launch_bot --name=Test --debug_mode=False --advanced_logging=False

read -p "Press any key..."
