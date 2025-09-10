import subprocess
from utils import detect_os, get_installed_version, logging

def install_tool(tool, os_type):
    """Install tool using package manager. Logs success/error."""
    if os_type is None:
        print("Unsupported OS")
        return False
    
    try:
        if os_type == 'macos':
            if tool == 'ngspice':
                subprocess.run(['brew', 'install', 'ngspice'], check=True)
            elif tool == 'kicad':
                subprocess.run(['brew', 'install', '--cask', 'kicad'], check=True)
        elif os_type == 'linux':
            # Stub for Ubuntu: Requires sudo
            if tool == 'ngspice':
                subprocess.run(['sudo', 'apt', 'update'], check=True)
                subprocess.run(['sudo', 'apt', 'install', '-y', 'ngspice'], check=True)
            elif tool == 'kicad':
                subprocess.run(['sudo', 'add-apt-repository', 'ppa:kicad/kicad-9.0-releases', '-y'], check=True)
                subprocess.run(['sudo', 'apt', 'update'], check=True)
                subprocess.run(['sudo', 'apt', 'install', '-y', 'kicad'], check=True)
        elif os_type == 'windows':
            # Stub for Chocolatey
            print("Windows support: Install Chocolatey first, then choco install ngspice/kicad")
            return False
        
        # Verify install
        version = get_installed_version(tool)
        if version:
            logging.info(f"{tool} installed successfully (version {version})")
            print(f"{tool} installed: {version}")
            return True
        else:
            logging.error(f"Installation of {tool} failed - version not detected")
            return False
    except subprocess.CalledProcessError as e:
        logging.error(f"Installation error for {tool}: {e}")
        print(f"Installation failed: {e}. Check Homebrew (macOS) or sudo (Linux).")
        return False
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        return False

if __name__ == "__main__":
    # Test: python installer.py
    os_type = detect_os()
    install_tool('ngspice', os_type)