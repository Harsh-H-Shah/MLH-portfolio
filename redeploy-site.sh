#!/bin/bash
set -e

PROJECT_DIR="../home/MLH-portfolio"

echo "📁 Changing directory to project..."
cd "$PROJECT_DIR"

echo "⬇️ Pulling latest code from GitHub main branch..."
git fetch
git reset origin/main --hard

echo "🛑 Stopping current containers..."
docker compose -f docker-compose.prod.yml down

echo "🐳 Building and starting containers..."
docker compose -f docker-compose.prod.yml up -d --build

echo "✅ Redeployment complete. Site should now be live."
