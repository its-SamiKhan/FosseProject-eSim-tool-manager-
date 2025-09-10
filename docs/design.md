# Automated Tool Manager for eSim

## Introduction
This tool automates managing external tools for eSim (esim.fossee.in), an open-source EDA tool by FOSSEE. It handles installation, updates, and basic config for tools like Ngspice (simulation) and KiCad (PCB design), reducing manual effort for compatibility and versions.

The prototype is Python-based, targeting macOS with Homebrew, and includes stubs for Linux/Windows. It meets at least two requirements: Tool Installation Management and Update System.

Author: [Your Name]
Date: September 10, 2025
OS Focus: macOS (Darwin via platform.system()).
Tools Researched: Ngspice (latest: 45.2), KiCad (latest: 9.0.4).

## Requirements Met
- **Tool Installation Management**: Auto-installs via OS-specific commands (macOS: brew install ngspice; verifies with --version; handles macOS/Linux/Windows compatibility).
- **Update and Upgrade System**: Checks latest versions online (requests + BeautifulSoup); upgrades with brew upgrade; minimal user input.
- **User Interface**: CLI menu (text-based in Terminal) to view tools/versions/updates; logs actions to tool_manager.log.
- Optional: Cross-platform support (full for macOS via Homebrew; apt/Chocolatey stubs); logging for errors.

Unmet (prototype scope): Full configuration (e.g., eSim paths), dependency checker.

## Architecture Overview
Modular design with 4 Python files. Entry point: main.py (CLI menu).
Flow:
- Start: Detect OS (utils.py).
- Load state from tools.json (os/json).
- Menu loop: User chooses action (install/update/view).
- Execute: Call installer/updater; log (logging); save state.
- Error handling: Try-except in all modules; user feedback.

Simple Flowchart (text):
User Runs main.py
|
v
utils.detect_os() --> If macOS: Use brew
|
v
Load tools.json
|
v
CLI Menu: 1. Install, 2. Update, 3. View, 4. Exit
|
+-- Install: installer.install_tool() --> subprocess.run(['brew', 'install', 'ngspice']) --> utils.get_installed_version() --> Save JSON + Log
|
+-- Update: updater.check_for_update() --> requests.get(url) --> BeautifulSoup parse --> If newer: brew upgrade --> Update JSON + Log
|
+-- View: Print tools.json contents


Assumptions: Homebrew installed; internet for updates. Limitations: Web scraping fragile if sites change; no GUI (CLI meets reqs).

## Module Breakdown
Use separate files for modularity (easy to expand).

- **main.py**: CLI entry (while loop for menu). Imports others; handles JSON load/save (json/os). Calls detect_os, install_tool, check_for_update. Example code snippet:

def main():
os_type = detect_os()
tools = load_json()
while True:
print("Menu: 1 Install Ngspice...")
choice = input()
if choice == '1':
install_tool('ngspice', os_type)
etc.


- **installer.py**: Installation logic. OS-specific subprocess calls (e.g., macOS: brew install; Linux: apt install). Verifies post-install with get_version.

- **updater.py**: Update logic. Web fetch (requests.get), parse (BeautifulSoup.find for "stable release"), compare versions, call installer for upgrade.

- **utils.py**: Helpers. detect_os (platform.system()), get_installed_version (subprocess.check_output('--version')), logging.setup (logging.basicConfig to file).

Data Files:
- tools.json: {"ngspice": "45.2", "kicad": "9.0.4"}
- tool_manager.log: Timestamped logs (e.g., "INFO: Installed ngspice").

Libraries: Built-in (subprocess, platform, os, json, logging); External (requests, beautifulsoup4 from requirements.txt).

## Component Interactions
- main.py central: Calls utils for OS/version; installer for actions; updater for checks. Example: Update flow = main → updater.check (requests/BS4) → if update, installer.upgrade (subprocess) → utils.log + main.save_json.
- Error Flow: Try-except in each function (e.g., FileNotFoundError if tool not installed); print "Error: [msg]"; log.error.
- Integration: Homebrew for macOS streamlines; stubs for apt (Linux), choco (Windows).

## Evaluation Fit
- Functionality: Automates install/update.
- Design: Modular, easy to use CLI.
- Documentation: This doc + code comments.
- Code Quality: Readable functions, best practices (try-except).
- Creativity: macOS adaptation with web scraping.

## Assumptions and Limitations
- Assumes Python 3.12+, Homebrew on macOS.
- Limitations: Manual version parsing may fail on output changes; no advanced config (e.g., eSim path setting with os.environ).
- Testing: On macOS only for prototype.

## Future Work
- Add GUI (Tkinter buttons).
- Dependency checks (subprocess for brew deps).
- Full eSim integration (set environment variables).

References: eSim (esim.fossee.in), Ngspice docs, KiCad download page, Python subprocess docs.