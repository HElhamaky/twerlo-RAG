#!/bin/bash

echo "🚀 Deploying Docker build fix..."

# Add changes
git add Dockerfile

# Commit changes
git commit -m "fix: Add public directory verification in Docker build

- Add mkdir -p public to ensure directory exists
- Add verification steps to debug build issues
- Fix 'public directory not found' error in Render.com"

# Push to GitHub
git push origin main

echo "✅ Changes pushed to GitHub"
echo "🔄 Render.com will automatically rebuild with the fix" 