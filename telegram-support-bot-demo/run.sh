#!/bin/bash

set -e

echo "STARTING TELEGRAM SUPPORT BOT"

pip install -r requirements.txt

python3 main.py
