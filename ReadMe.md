Advanced eSim Automated Tool Manager
Overview
This Python-based tool automates the installation, updates, configuration, and dependency management for eSim, an open-source EDA tool (esim.fossee.in). It supports Ngspice (circuit simulator, version 45.2), KiCad (schematic/PCB design, version 9.0.4), and GHDL (VHDL simulator, version 4.1.0), addressing challenges like OS compatibility, version tracking, and eSim integration. The tool features a Tkinter GUI, dependency checking, PATH/environment variable configuration, and cross-platform support (macOS, Linux, Windows).
Developed for: eSim Semester Long Internship Autumn 2025 Submission Task 5Author: Sami KhanDate: September 10, 2025Repository: github.com/its-SamiKhan/FosseProject-eSim-tool-manager
Key Features

Graphical User Interface: Intuitive Tkinter GUI with buttons for installing, updating, and viewing tools, plus popup feedback.
Tool Installation: Automated installs via Homebrew (macOS), APT (Linux), or Chocolatey (Windows), with version tracking in tools.json.
Updates: Web scraping for latest versions (ngspice.sourceforge.io, kicad.org, ghdl.free.fr) and auto-upgrades.
Dependency Checker: Verifies required libraries (e.g., fftw for Ngspice) before installation.
Configuration Handling: Sets PATH and environment variables (e.g., NGSPICE_LIB) for seamless eSim integration.
Cross-Platform: Full macOS support, tested stubs for Linux (Ubuntu) and Windows.
Creative Addition: GHDL support for VHDL simulation in eSim.

Requirements Fulfilled
The tool meets 5 requirements from the task, plus creative enhancements:

Tool Installation Management: Auto-installs Ngspice, KiCad, GHDL with version checks.
Update and Upgrade System: Web-based version checks and upgrades with minimal input.
Configuration Handling: Configures PATH and tool-specific env vars (e.g., NGSPICE_LIB, GHDL_BIN).
Dependency Checker: Ensures dependencies are installed before proceeding.
User Interface: Advanced GUI with buttons, popups, and logging to tool_manager.log.

Setup Instructions
Follow these steps to set up the tool on macOS, Linux (Ubuntu), or Windows.
macOS (Sonoma/Sequoia)

Install Prerequisites:
Homebrew: /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
Python 3.12+: brew install python
Git: brew install git


Clone Repository:git clone https://github.com/its-SamiKhan/FosseProject-eSim-tool-manager.git
cd FosseProject-eSim-tool-manager


Set Up Virtual Environment:python3 -m venv tool_manager_env
source tool_manager_env/bin/activate
pip install requests beautifulsoup4



Linux (Ubuntu 22.04/24.04)

Install Prerequisites:sudo apt update && sudo apt upgrade
sudo apt install python3 python3-venv python3-tk git


Clone Repository:git clone https://github.com/its-SamiKhan/FosseProject-eSim-tool-manager.git
cd FosseProject-eSim-tool-manager


Set Up Virtual Environment:python3 -m venv tool_manager_env
source tool_manager_env/bin/activate
pip install requests beautifulsoup4



Windows (10/11)

Install Prerequisites:
Chocolatey: Run PowerShell as admin:Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))


Python 3.12+: Download from python.org, check "Add to PATH" during install.
Git: Download from git-scm.com.


Clone Repository:git clone https://github.com/its-SamiKhan/FosseProject-eSim-tool-manager.git
cd FosseProject-eSim-tool-manager


Set Up Virtual Environment:python -m venv tool_manager_env
tool_manager_env\Scripts\activate
pip install requests beautifulsoup4



Running the Tool

Activate virtual environment (see above).
Run the tool:python main.py  # macOS/Linux: python3 main.py


A GUI window opens with buttons:
Install Ngspice/KiCad/GHDL: Installs via package manager, checks dependencies, configures PATH/env.
Update Ngspice/KiCad/GHDL: Checks for updates, upgrades if needed.
View Tools: Shows installed versions in a popup (e.g., "Ngspice: 45.2").
Exit: Closes the GUI.


Notes:
macOS: Homebrew may prompt for password.
Linux: Sudo prompts for APT installs (run sudo python main.py for smoother flow).
Windows: Run PowerShell as admin for Chocolatey installs.
Internet required for update checks.
Logs saved to tool_manager.log, versions to tools.json.



Testing the Prototype
Test the tool to verify all features across platforms.
Test Steps

Start GUI: Run python main.py – GUI opens with buttons for Ngspice, KiCad, GHDL.
View Tools: Click "View Tools" – popup shows versions (e.g., "Ngspice: 45.2, KiCad: 9.0.4, GHDL: Not installed").
Install Ngspice: Click "Install Ngspice" – checks dependencies (e.g., fftw), installs via Homebrew/APT/Chocolatey, configures PATH/NGSPICE_LIB.
Verify: ngspice --version (expect "ngspice-45 plus...").


Update Ngspice: Click "Update Ngspice" – scrapes ngspice.sourceforge.io, shows "up to date" or upgrades.
Install KiCad: Click "Install KiCad" – installs (5-10 mins on macOS), configures PATH.
Verify: kicad-cli version (expect "9.0.4") or open KiCad app.


Install/Update GHDL: Similar process, verify: ghdl --version (expect "4.1.0").
Edge Cases:
No internet: Update buttons show "Error: Update check failed".
Missing dependencies: Install fails with popup (e.g., "Missing fftw").
Already installed: Package manager skips (e.g., "ngspice 45.2 already installed").


Verify Outputs:
Check tools.json: {"ngspice": "45.2", "kicad": "9.0.4", "ghdl": "4.1.0"}.
Check tool_manager.log: Logs installs, updates, errors.



Platform-Specific Testing



Platform
Command
Notes



macOS
python3 main.py
Fully tested, Homebrew seamless, no sudo needed.


Linux
sudo python3 main.py
APT requires sudo, KiCad needs PPA. Test in Ubuntu VM.


Windows
python main.py
Run as admin for Chocolatey. Test paths (e.g., C:\Program Files\Ngspice\bin).


Troubleshooting

macOS:
Brew errors: Run brew doctor or brew update.
Path issues: Verify /opt/homebrew/bin in echo $PATH.


Linux:
Sudo fails: Ensure sudo access (sudo -l).
PPA errors: Check ppa:kicad/kicad-9.0-releases or use manual install from kicad.org.


Windows:
Choco fails: Run PowerShell as admin, verify Chocolatey (choco --version).
Path issues: Check echo %PATH% for C:\Program Files\Ngspice\bin.


General:
Version parse fails: Add print(output) in utils.py:get_installed_version, share output.
Scraping fails: Add print(response.text[:500]) in updater.py:check_for_update, share output for new selectors.
GUI crash: Ensure Tkinter (python3 -c "import tkinter"), reinstall Python if needed.



Limitations

macOS: Fully tested, robust.
Linux/Windows: APT/Chocolatey stubs work but need full testing (use VMs: Ubuntu 24.04, Windows 11).
Web Scraping: Fragile if sites change (e.g., ngspice.sourceforge.io layout). Hardcoded fallbacks used (45.2, 9.0.4, 4.1.0).
GUI: Basic Tkinter interface, no progress bars for long installs (e.g., KiCad).
Dependencies: Windows checker is a stub; full implementation requires Chocolatey dependency parsing.

Code Structure

main.py: Tkinter GUI with buttons for install/update/view/exit.
utils.py: OS detection, version parsing, dependency checks, JSON/logging, GUI popups.
installer.py: Installs via package managers, configures PATH/env, checks deps.
updater.py: Web scraping for updates, upgrades tools.
requirements.txt: Lists requests, beautifulsoup4.
Data Files:
tools.json: Stores installed versions.
tool_manager.log: Logs actions/errors.


Docs: docs/design.md details architecture and testing.

Folder Structure:
Fosse project/
├── README.md          # Setup, run, test instructions
├── .gitignore         # Ignores venv, JSON, logs
├── requirements.txt   # Python dependencies
├── main.py            # GUI entry point
├── installer.py       # Installation and config
├── updater.py         # Update checks and upgrades
├── utils.py           # Helpers and dependency checks
├── tools.json         # Generated: Version storage
├── tool_manager.log   # Generated: Action logs
└── docs/
    └── design.md      # Architecture and testing details

Contributing

Fork the repo on GitHub.
Report bugs via GitHub issues.
For eSim integration, extend installer.py:configure_tool (e.g., add more env vars).

Submission

Push to private GitHub repo: https://github.com/its-SamiKhan/FosseProject-eSim-tool-manager.
Add collaborator: Eyantra698Sumanto (GitHub Settings > Collaborators).
Export docs/design.md to PDF (VS Code: Markdown PDF extension or online tool).
Email to contact-esim@fossee.in:
Subject: eSim Semester Long Internship Autumn 2025 Submission Task 5
Body: "Advanced eSim Tool Manager with GUI, dependency checker, configuration handling, GHDL support, and cross-platform compatibility (macOS/Linux/Windows). Repository: https://github.com/its-SamiKhan/FosseProject-eSim-tool-manager. Design document attached."
Attachment: design.pdf



License
MIT License (or as specified by eSim project requirements).
References

eSim: esim.fossee.in
Ngspice: ngspice.sourceforge.io
KiCad: kicad.org
GHDL: ghdl.free.fr

