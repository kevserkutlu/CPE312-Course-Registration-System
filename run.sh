#!/bin/bash

# Course Registration System - Fullstack Application Runner
# This script starts the entire application with all necessary components

set -e  # Exit on any error

echo "=================================================="
echo "🎓 Course Registration System"
echo "=================================================="
echo ""

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Get the script directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

echo -e "${BLUE}📁 Working Directory:${NC} $SCRIPT_DIR"
echo ""

# Check if virtual environment exists
if [ ! -d ".venv" ]; then
    echo -e "${YELLOW}⚠️  Virtual environment not found. Creating...${NC}"
    python3 -m venv .venv
    echo -e "${GREEN}✅ Virtual environment created${NC}"
fi

echo ""
echo -e "${BLUE}🔧 Activating virtual environment...${NC}"
source .venv/bin/activate

echo -e "${GREEN}✅ Virtual environment activated${NC}"
echo ""

# Install/update dependencies
echo -e "${BLUE}📦 Installing dependencies...${NC}"
pip install -q -r requirements.txt 2>/dev/null || {
    echo -e "${YELLOW}⚠️  requirements.txt not found or pip install failed${NC}"
    echo -e "${BLUE}Installing Flask and SQLAlchemy...${NC}"
    pip install -q flask sqlalchemy psycopg2-binary
}
echo -e "${GREEN}✅ Dependencies installed${NC}"
echo ""

# Check if PostgreSQL is running (optional warning)
if ! command -v psql &> /dev/null; then
    echo -e "${YELLOW}⚠️  psql not found. Make sure PostgreSQL is running.${NC}"
    echo ""
fi

# Start the Flask web server
echo -e "${BLUE}🚀 Starting Flask web server...${NC}"
echo ""
echo -e "${GREEN}════════════════════════════════════════════════${NC}"
echo -e "${GREEN}✅ Application is starting!${NC}"
echo -e "${GREEN}════════════════════════════════════════════════${NC}"
echo ""
echo -e "${YELLOW}📍 Web Interface: ${GREEN}http://localhost:5001${NC}"
echo ""
echo -e "${YELLOW}Press CTRL+C to stop the server${NC}"
echo ""

# Run the Flask application
python3 web.py
