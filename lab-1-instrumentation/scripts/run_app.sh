#!/bin/bash

# Exit when any command fails
set -e

# Function to check if a command exists
command_exists () {
    command -v "$1" >/dev/null 2>&1
}

# Step 1: Check if Poetry is installed
if command_exists poetry; then
    echo "Poetry is already installed."
else
    echo "Poetry is not installed. Installing Poetry..."
    curl -sSL https://install.python-poetry.org | python3 -
    # Add Poetry to PATH
    export PATH="$HOME/.local/bin:$PATH"
    echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
    source ~/.bashrc
fi

# Step 2: Update project dependencies
echo "Updating project dependencies..."
poetry update

# Step 3: Install any missing dependencies
echo "Installing missing dependencies..."
poetry install

# Step 4: Run the application
echo "Starting the application..."
poetry run python app.py

echo "Application has started successfully!"
