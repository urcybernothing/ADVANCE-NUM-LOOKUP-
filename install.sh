#!/bin/bash
# ============================================================
#   ADVANCE-NUM-LOOKUP - Installer
#   Made by ANURAG X NOTHING
#   Telegram: https://t.me/anonymousanurix
# ============================================================

RED='\033[0;31m'
GREEN='\033[0;32m'
CYAN='\033[0;36m'
YELLOW='\033[1;33m'
NC='\033[0m'

clear
echo -e "${RED}"
echo "  ============================================"
echo "       ADVANCE-NUM-LOOKUP - INSTALLER         "
echo "  ============================================"
echo -e "${NC}"

echo -e "${CYAN}[*] Installing required packages...${NC}"

if command -v pip3 &> /dev/null; then
    PIP="pip3"
elif command -v pip &> /dev/null; then
    PIP="pip"
else
    echo -e "${RED}[!] pip not found. Install python first.${NC}"
    exit 1
fi

$PIP install --upgrade pip > /dev/null 2>&1
$PIP install -r requirements.txt

if [ $? -eq 0 ]; then
    echo -e "${GREEN}[OK] All packages installed.${NC}"
else
    echo -e "${RED}[!] Install failed. Try: pip install -r requirements.txt${NC}"
    exit 1
fi

chmod +x anurix.py 2>/dev/null

echo ""
echo -e "${GREEN}[OK] Setup complete.${NC}"
echo -e "${YELLOW}[*] To start the tool, run:${NC}"
echo -e "${CYAN}    python anurix.py${NC}"
echo ""
echo -e "${RED}[!] Join: https://t.me/anonymousanurix${NC}"
echo ""
