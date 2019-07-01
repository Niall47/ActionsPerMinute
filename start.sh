#!/bin/bash

iterm -e "python3 keyboard.py" 
python3 reset.py &
python3 server.py 
