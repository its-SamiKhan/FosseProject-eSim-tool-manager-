# Advanced eSim Automated Tool Manager

## Overview

This Python-based tool automates installation, updates, configuration, and dependency management for [eSim](https://esim.fossee.in), an open-source EDA tool.  
**Supported tools:**  
- **Ngspice** (circuit simulator, v45.2)  
- **KiCad** (schematic/PCB design, v9.0.4)  
- **GHDL** (VHDL simulator, v4.1.0)  

Addresses OS compatibility, version tracking, and eSim integration.  
Features a Tkinter GUI, dependency checking, PATH/environment variable configuration, and cross-platform support (macOS, Linux, Windows).

**Developed for:** eSim Semester Long Internship Autumn 2025 Submission Task 5  
**Author:** Sami Khan  
**Date:** September 10, 2025  
**Repository:** [github.com/its-SamiKhan/FosseProject-eSim-tool-manager](https://github.com/its-SamiKhan/FosseProject-eSim-tool-manager)

---

## Key Features

- **Graphical User Interface:** Tkinter GUI with install/update/view buttons and popup feedback.
- **Tool Installation:** Automated via Homebrew (macOS), APT (Linux), Chocolatey (Windows), version tracking in `tools.json`.
- **Updates:** Web scraping for latest versions and auto-upgrades.
- **Dependency Checker:** Verifies required libraries (e.g., fftw for Ngspice).
- **Configuration Handling:** Sets PATH and environment variables for eSim integration.
- **Cross-Platform:** Full macOS support, tested stubs for Linux and Windows.
- **Creative Addition:** GHDL support for VHDL simulation in eSim.

---

## Requirements Fulfilled

- **Tool Installation Management:** Auto-installs Ngspice, KiCad, GHDL with version checks.
- **Update and Upgrade System:** Web-based version checks and upgrades.
- **Configuration Handling:** Configures PATH and tool-specific env vars.
- **Dependency Checker:** Ensures dependencies are installed before proceeding.
- **User Interface:** Advanced GUI with buttons, popups, and logging.

---

## Setup Instructions

### macOS (Sonoma/Sequoia)

1. **Install Prerequisites:**
    ```sh
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    brew install python
    brew install git
    ```
2. **Clone Repository:**
    ```sh
    git clone https://github.com/its-SamiKhan/FosseProject-eSim-tool-manager.git
    cd FosseProject-eSim-tool-manager
    ```
3. **Set Up Virtual Environment:**
    ```sh
    python3 -m venv tool_manager_env
    source tool_manager_env/bin/activate
    pip install requests beautifulsoup4
    ```

---

### Linux (Ubuntu 22.04/24.04)

1. **Install Prerequisites:**
    ```sh
    sudo apt update && sudo apt upgrade
    sudo apt install python3 python3-venv python3-tk git
    ```
2. **Clone Repository:**
    ```sh
    git clone https://github.com/its-SamiKhan/FosseProject-eSim-tool-manager.git
    cd FosseProject-eSim-tool-manager
    ```
3. **Set Up Virtual Environment:**
    ```sh
    python3 -m venv tool_manager_env
    source tool_manager_env/bin/activate
    pip install requests beautifulsoup4
    ```

---

### Windows (10/11)

1. **Install Prerequisites:**
    - **Chocolatey:**  
      Run PowerShell as admin:
      ```powershell
      Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
      ```
    - **Python 3.12+:** Download from [python.org](https://python.org), check "Add to PATH" during install.
    - **Git:** Download from [git-scm.com](https://git-scm.com).

2. **Clone Repository:**
    ```powershell
    git clone https://github.com/its-SamiKhan/FosseProject-eSim-tool-manager.git
    cd FosseProject-eSim-tool-manager
    ```
3. **Set Up Virtual Environment:**
    ```powershell
    python -m venv tool_manager_env
    tool_manager_env\Scripts\activate
    pip install requests beautifulsoup4
    ```

---

## Running the Tool

1. **Activate virtual environment** (see above).
2. **Run the tool:**
    ```sh
    python main.py  # macOS/Linux: python3 main.py
    ```

**GUI window features:**
- **Install Ngspice/KiCad/GHDL:** Installs via package manager, checks dependencies, configures PATH/env.
- **Update Ngspice/KiCad/GHDL:** Checks for updates, upgrades if needed.
- **View Tools:** Shows installed versions in a popup.
- **Exit:** Closes the GUI.

**Notes:**
- macOS: Homebrew may prompt for password.
- Linux: Sudo prompts for APT installs (run `sudo python main.py` for smoother flow).
- Windows: Run PowerShell as admin for Chocolatey installs.
- Internet required for update checks.
- Logs saved to `tool_manager.log`, versions to `tools.json`.

---

## Testing the Prototype

### Test Steps

1. **Start GUI:** Run `python main.py`.
2. **View Tools:** Click "View Tools" – popup shows versions.
3. **Install Ngspice:** Click "Install Ngspice" – checks dependencies, installs, configures PATH/NGSPICE_LIB.
4. **Verify:** Run `ngspice --version`.
5. **Update Ngspice:** Click "Update Ngspice".
6. **Install KiCad:** Click "Install KiCad", verify with `kicad-cli version`.
7. **Install/Update GHDL:** Similar process, verify with `ghdl --version`.

**Edge Cases:**
- No internet: Update buttons show error.
- Missing dependencies: Install fails with popup.
- Already installed: Package manager skips.

**Verify Outputs:**
- Check `tools.json`:  
  ```json
  {"ngspice": "45.2", "kicad": "9.0.4", "ghdl": "4.1.0"}
  ```
- Check `tool_manager.log`: Logs installs, updates, errors.

---

## Platform-Specific Testing

| Platform | Command            | Notes                                         |
|----------|--------------------|-----------------------------------------------|
| macOS    | python3 main.py    | Fully tested, Homebrew seamless, no sudo.     |
| Linux    | sudo python3 main.py| APT requires sudo, KiCad needs PPA.           |
| Windows  | python main.py     | Run as admin for Chocolatey. Test paths.      |

---

## Troubleshooting

**macOS:**
- Brew errors: `brew doctor` or `brew update`
- Path issues: Verify `/opt/homebrew/bin` in `echo $PATH`

**Linux:**
- Sudo fails: Ensure sudo access (`sudo -l`)
- PPA errors: Check `ppa:kicad/kicad-9.0-releases`

**Windows:**
- Choco fails: Run PowerShell as admin, verify Chocolatey (`choco --version`)
- Path issues: Check `echo %PATH%` for Ngspice bin

**General:**
- Version parse fails: Add `print(output)` in `utils.py:get_installed_version`
- Scraping fails: Add `print(response.text[:500])` in `updater.py:check_for_update`
- GUI crash: Ensure Tkinter (`python3 -c "import tkinter"`)

---

## Limitations

- macOS: Fully tested, robust.
- Linux/Windows: Stubs work, need full testing (use VMs).
- Web Scraping: Fragile if sites change; hardcoded fallbacks used.
- GUI: Basic Tkinter, no progress bars for long installs.
- Dependencies: Windows checker is a stub.

---

## Code Structure

- `main.py`: Tkinter GUI entry point
- `utils.py`: OS detection, version parsing, dependency checks, JSON/logging, GUI popups
- `installer.py`: Installation/config, PATH/env, dependency checks
- `updater.py`: Web scraping for updates, upgrades tools
- `requirements.txt`: Python dependencies
- **Data Files:**
    - `tools.json`: Installed versions
    - `tool_manager.log`: Action logs

**Docs:**  
`docs/design.md` details architecture and testing.

---

## Folder Structure

```
Fosse project/
├── README.md
├── .gitignore
├── requirements.txt
├── main.py
├── installer.py
├── updater.py
├── utils.py
├── tools.json
├── tool_manager.log
└── docs/
    └── design.md
```

---

## Contributing

- Fork the repo on GitHub.
- Report bugs via GitHub issues.
- For eSim integration, extend `installer.py:configure_tool`.

---

## Submission

- Push to private GitHub repo: [repo link](https://github.com/its-SamiKhan/FosseProject-eSim-tool-manager)
- Add collaborator: `Eyantra698Sumanto`
- Export `docs/design.md` to PDF
- Email to `contact-esim@fossee.in`:
    - **Subject:** eSim Semester Long Internship Autumn 2025 Submission Task 5
    - **Body:**  
      "Advanced eSim Tool Manager with GUI, dependency checker, configuration handling, GHDL support, and cross-platform compatibility (macOS/Linux/Windows). Repository: [repo link]. Design document attached."
    - **Attachment:** `design.pdf`

---

## License

MIT License (or as specified by eSim project requirements).

---

## References

- [eSim](https://esim.fossee.in)
- [Ngspice](https://ngspice.sourceforge.io)
- [KiCad](https://kicad.org)
-