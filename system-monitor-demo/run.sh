#!/bin/bash

set -e

echo "SYSTEM MONITOR DEMO"

python3 main.py

echo ""
echo "REPORT:"
echo ""

cat report.txt
