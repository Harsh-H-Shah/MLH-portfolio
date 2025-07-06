#!/bin/bash

set -e

PROJECT_DIR="/home/MLH-portfolio"
VENV_DIR="/home/MLH-portfolio/python3-virtualenv"

echo "🔁 Killing all existing tmux sessions..."
tmux kill-server || true

echo "📁 Changing directory to project..."
cd "$PROJECT_DIR"

echo "⬇️ Pulling latest code from GitHub main branch..."
git fetch
git reset origin/main --hard

echo "🐍 Activating virtual environment..."
source "$VENV_DIR/bin/activate"

echo "📦 Installing Python dependencies..."
pip install -r requirements.txt

echo "🖥️ Starting new detached tmux session with Flask server..."
tmux new-session -d -s flask-server "cd $PROJECT_DIR && source $VENV_DIR/bin/activate && flask run --host=0.0.0.0"

echo "✅ Site redeployed successfully!"
