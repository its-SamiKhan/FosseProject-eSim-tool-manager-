import subprocess
import platform
import os
import json
import logging
import tkinter as tk
from tkinter import messagebox

# Setup logging: File + console for detailed tracking of all actions/errors (fulfills UI log requirement)
logging.basicConfig(
    level=logging.INFO,  # Info level for normal operations; change to DEBUG for verbose
    format='%(asctime)s - %(levelname)s - %(message)s',  # Timestamp + level + message
    handlers=[
        logging.FileHandler('tool_manager.log'),  # Saves to log file
        logging.StreamHandler()  # Prints to console
    ]
)

TOOLS_JSON = 'tools.json'  # File to store installed versions (JSON for easy read/write)

def detect_os():
    """Detects system OS for cross-platform support. Returns 'macos', 'linux', 'windows', or None."""
    sys = platform.system()
    if sys == 'Darwin':
        return 'macos'  # macOS (Darwin kernel)
    elif sys == 'Linux':
        return 'linux'  # Ubuntu/Debian
    elif sys == 'Windows':
        return 'windows'  # Windows 10/11
    logging.warning(f"Unsupported OS detected: {sys}")
    return None

def get_installed_version(tool):
    """Gets version of installed tool using subprocess. Returns version string or None if not installed/fail.
    Handles different tools and OS paths."""
    try:
        if tool == 'ngspice':
            output = subprocess.check_output(['ngspice', '--version']).decode('utf-8')
            version = output.split('ngspice-')[1].split()[0]  # Parse e.g., "ngspice-45.2 plus..." -> "45.2"
        elif tool == 'kicad':
            try:
                output = subprocess.check_output(['kicad-cli', 'version']).decode('utf-8')
                version = output.strip().split()[-1]  # e.g., "9.0.4"
            except:
                # Fallback for manual install on macOS
                app_path = '/Applications/KiCad/KiCad.app/Contents/MacOS/kicad-cli'
                if os.path.exists(app_path):
                    output = subprocess.check_output([app_path, 'version']).decode('utf-8')
                    version = output.strip().split()[-1]
                else:
                    version = None
        elif tool == 'ghdl':
            output = subprocess.check_output(['ghdl', '--version']).decode('utf-8')
            version = output.splitlines()[0].split()[1]  # e.g., "GHDL 4.1.0"
        logging.info(f"Version retrieved for {tool}: {version}")
        return version
    except Exception as e:
        logging.warning(f"Failed to get version for {tool}: {e} (tool may not be installed)")
        return None

def load_tools():
    """Loads installed tools and versions from JSON file. Returns empty dict if file missing."""
    if os.path.exists(TOOLS_JSON):
        with open(TOOLS_JSON, 'r') as f:
            data = json.load(f)
            logging.info("Loaded tools.json: " + str(data))
            return data
    logging.info("tools.json not found – starting empty")
    return {}

def save_tools(tools):
    """Saves tools dict to JSON file for persistence."""
    with open(TOOLS_JSON, 'w') as f:
        json.dump(tools, f, indent=4)  # Indented for readability
    logging.info("Saved tools.json: " + str(tools))

def check_dependencies(tool, os_type):
    """Checks for required dependencies before install. Returns True if OK, False if missing (fulfills Dependency Checker requirement)."""
    if os_type == 'macos':
        try:
            # Use brew deps to list, then check if installed
            output = subprocess.check_output(['brew', 'deps', tool]).decode('utf-8').strip()
            deps = output.splitlines() if output else []
            missing = []
            for dep in deps:
                try:
                    subprocess.check_output(['brew', 'list', dep])
                except:
                    missing.append(dep)
            if missing:
                logging.warning(f"Missing dependencies for {tool}: {', '.join(missing)}. Install with 'brew install [dep]'.")
                return False
            logging.info(f"Dependencies checked for {tool}: {deps or 'None required'} – all OK")
            return True
        except Exception as e:
            logging.error(f"Dependency check failed for {tool}: {e}. Skipping check.")
            return False
    elif os_type == 'linux':
        # Stub: Check for apt packages (e.g., libfftw3 for Ngspice)
        logging.info("Linux dependency check stub – assume OK")
        return True
    elif os_type == 'windows':
        # Stub: Check choco
        logging.info("Windows dependency check stub – assume OK")
        return True
    return False

def show_message(title, msg):
    """Shows GUI popup message for feedback (part of UI enhancement)."""
    root = tk.Tk()
    root.withdraw()  # Hide empty window
    messagebox.showinfo(title, msg)