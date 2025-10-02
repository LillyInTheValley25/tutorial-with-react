#!/bin/bash

# Create and activate virtual environment
echo "Creating virtual environment..."
python3 -m venv venv
source venv/bin/activate

# Install Django dependencies
echo "Installing Django dependencies..."
pip install -r requirements.txt

# Run Django migrations
echo "Running Django migrations..."
cd backend
python manage.py migrate

# Start Django development server
echo "Starting Django development server on port 8000..."
python manage.py runserver 8000
