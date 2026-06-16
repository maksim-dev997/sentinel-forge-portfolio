#!/bin/bash

set -e

echo "TASK QUEUE DEMO RUN"

python3 main.py

echo ""
echo "QUEUE:"
cat task_queue.txt

echo ""
echo "COMPLETED:"
cat completed_tasks.txt

echo ""
echo "FAILED:"
cat failed_tasks.txt
