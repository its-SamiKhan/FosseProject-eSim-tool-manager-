# eSim Automated Tool Manager

## Overview
This Python-based tool automates the installation, updates, and management of external dependencies for eSim, an open-source EDA tool (esim.fossee.in). It focuses on Ngspice (circuit simulator, latest version: 45.2) and KiCad (schematic/PCB design, latest version: 9.0.4), addressing manual setup challenges like compatibility and versions on macOS (via Homebrew), with stubs for Linux/Windows.

**Requirements Met**:
- Tool Installation Management: Auto-installs with version checks (e.g., `brew install ngspice`).
- Update and Upgrade System: Web-based version checks and upgrades (e.g., `brew upgrade`).
- User Interface: Simple CLI menu for actions, views versions/updates, logs to `tool_manager.log`.

Prototype developed for eSim Semester Long Internship Autumn 2025 Submission Task 5. Author: [Your Name]. Date: September 10, 2025.

## Setup
1. **Prerequisites** (macOS):
   - Homebrew: Install from [brew.sh](https://brew.sh) if missing (`/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`).
   - Python 3.12+: `brew install python`.
   - Git: `brew install git`.

2. **Clone the Repo**:

https://github.com/its-SamiKhan/FosseProject-eSim-tool-manager-



3. **Virtual Environment**:
python3 -m venv tool_manager_env
source tool_manager_env/bin/activate  # On macOS/Linux; Windows: tool_manager_env\Scripts\activate
pip install -r requirements.txt  # Installs requests, beautifulsoup4


## Run the Tool
With venv activated: python main.py


- Menu appears with 6 options:
  1. Install Ngspice
  2. Install KiCad
  3. Check/Update Ngspice
  4. Check/Update KiCad
  5. View Installed Tools (shows versions from tools.json)
  6. Exit
- Example: Choose 1 – installs Ngspice via Homebrew (enter password if prompted). Choose 5 – views "ngspice: 45.2".

**Notes**:
- Installs/updates require admin privileges (password for brew/sudo).
- Updates check official sites (ngspice.sourceforge.io, kicad.org); may need internet.
- Logs: View `tool_manager.log` for actions/errors.

## Testing the Prototype
1. **View Tools**: Choose 5 – lists versions (initially "Not installed").
2. **Install Ngspice**: Choose 1 – runs `brew install ngspice`. Verify: `ngspice --version` (expect "ngspice-45 plus...").
3. **View Again**: Choose 5 – shows "ngspice: 45.2".
4. **Update Ngspice**: Choose 3 – checks web; if up-to-date, "Ngspice is up to date". If newer, upgrades.
5. **Install KiCad**: Choose 2 – `brew install --cask kicad` (5-10 mins). Verify: Open KiCad in Spotlight; `kicad-cli version` (expect "9.0.4").
6. **Update KiCad**: Choose 4 – similar to Ngspice.
7. **Edge Cases**:
   - No internet: Updates log "failed" (no crash).
   - Invalid choice: "Invalid choice. Try again."
   - Uninstall for re-test: `brew uninstall ngspice --cask kicad`.

**Tested On**: macOS (Sonoma/Sequoia) with Homebrew. Linux/Windows stubs untested.

## Limitations
- Prototype: macOS-focused; full Linux/Windows needs testing (apt/Chocolatey).
- Web scraping: May break if sites change (e.g., version text moves) – hardcoded fallback possible.
- No GUI (CLI meets requirements); no full config/dependency checks (scope for future).
- Versions: Based on September 10, 2025 (Ngspice 45.2, KiCad 9.0.4).

## Code Structure
- `main.py`: CLI menu and integration.
- `installer.py`: OS-specific installs (subprocess for brew/apt).
- `updater.py`: Web checks (requests/BeautifulSoup) and upgrades.
- `utils.py`: OS detect (platform), version get, JSON/log handling.
- Data: `tools.json` (versions), `tool_manager.log` (actions).

Comments in code explain functions. See `docs/design.md` for architecture.

## Contributing/Issues
Fork on GitHub. Report bugs via issues. For eSim integration, extend config in installer.py (e.g., set PATH for eSim).

## License
MIT (or as per eSim project – open-source).

References: eSim docs, Ngspice/KiCad sites.




Fosse project/
├── README.md          # New: Instructions
├── .gitignore
├── requirements.txt
├── main.py
├── installer.py
├── updater.py
├── utils.py
├── tools.json         # Generated
├── tool_manager.log   # Generated
└── docs/
    └── design.md      # Updated