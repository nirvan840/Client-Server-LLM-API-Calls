#!/bin/bash

# Run server.py in a new Command Prompt window
start cmd /k "python server.py"

# Wait for the server to start up
sleep 5

# Run main.py in the current terminal
python main.py

# Keep the terminal open
read -p "Press any key to exit..."
