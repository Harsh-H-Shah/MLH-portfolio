#!/bin/bash
set -e

# Update these paths to match your setup
PROJECT_DIR="$HOME/MLH-portfolio"
VENV_DIR="$PROJECT_DIR/python3-virtualenv"

echo "📁 Changing directory to project..."
cd "$PROJECT_DIR"

echo "⬇️ Pulling latest code from GitHub main branch..."
git fetch
git reset origin/main --hard

echo "🐍 Activating virtual environment..."
source "$VENV_DIR/bin/activate"

echo "📦 Installing Python dependencies..."
pip install -r requirements.txt

echo "🔁 Restarting systemd myportfolio service..."
sudo systemctl restart myportfolio

echo "✅ Redeployment complete. Site should now be live."
