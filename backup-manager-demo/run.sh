#!/bin/bash

set -e

echo "BACKUP MANAGER DEMO"

python3 main.py

echo ""
echo "REPORT:"
echo ""

cat report.txt

echo ""
echo "BACKUPS:"
ls -la backups
