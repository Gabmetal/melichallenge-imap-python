#!/bin/bash
echo 'Install Deps'
pip install --no-cache-dir -r ./requirements.txt
echo 'Start App'
python main.py