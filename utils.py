import subprocess
import platform
import os
import json
import logging

# Set up logging to file (tool_manager.log) and console
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('tool_manager.log'),
        logging.StreamHandler()  # Also print to console
    ]
)

TOOLS_JSON = 'tools.json'

def detect_os():
    """Detect OS: 'macos' for Darwin (macOS), 'linux', or 'windows'."""
    sys = platform.system()
    if sys == 'Darwin':
        return 'macos'
    elif sys == 'Linux':
        return 'linux'
    elif sys == 'Windows':
        return 'windows'
    else:
        logging.warning(f"Unsupported OS: {sys}")
        return None

def get_installed_version(tool):
    """Get installed version using subprocess. Returns None if not installed."""
    try:
        if tool == 'ngspice':
            output = subprocess.check_output(['ngspice', '--version']).decode('utf-8')
            # Parse version: e.g., "ngspice-45 plus..." -> "45"
            version = output.split('ngspice-')[1].split()[0] if 'ngspice-' in output else None
        elif tool == 'kicad':
            # For Homebrew KiCad, use kicad-cli; fallback for manual install
            try:
                output = subprocess.check_output(['kicad-cli', 'version']).decode('utf-8')
                version = output.strip().split()[-1]  # e.g., "9.0.4"
            except FileNotFoundError:
                # Fallback: Try app path (manual install)
                app_path = '/Applications/KiCad/KiCad.app/Contents/MacOS/kicad-cli'
                if os.path.exists(app_path):
                    output = subprocess.check_output([app_path, 'version']).decode('utf-8')
                    version = output.strip().split()[-1]
                else:
                    version = None
        logging.info(f"Found {tool} version: {version}")
        return version
    except (FileNotFoundError, subprocess.CalledProcessError, IndexError) as e:
        logging.warning(f"Could not get {tool} version: {e}")
        return None

def load_tools():
    """Load installed tools from JSON file."""
    if os.path.exists(TOOLS_JSON):
        with open(TOOLS_JSON, 'r') as f:
            return json.load(f)
    return {}

def save_tools(tools):
    """Save tools dict to JSON file."""
    with open(TOOLS_JSON, 'w') as f:
        json.dump(tools, f, indent=4)
    logging.info("Saved tools to JSON")