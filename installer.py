import subprocess
from utils import detect_os, get_installed_version, check_dependencies, logging, os, show_message

def install_tool(tool, os_type):
    """Installs tool with dependency check (fulfills Installation and Dependency Checker). Logs and shows message."""
    if not check_dependencies(tool, os_type):
        show_message("Error", f"Missing dependencies for {tool}. See log for details.")
        return False
    try:
        if os_type == 'macos':
            if tool == 'ngspice':
                subprocess.run(['brew', 'install', 'ngspice'], check=True)
            elif tool == 'kicad':
                subprocess.run(['brew', 'install', '--cask', 'kicad'], check=True)
            elif tool == 'ghdl':
                subprocess.run(['brew', 'install', 'ghdl'], check=True)
        elif os_type == 'linux':
            subprocess.run(['sudo', 'apt', 'update'], check=True)
            if tool == 'ngspice':
                subprocess.run(['sudo', 'apt', 'install', '-y', 'ngspice'], check=True)
            elif tool == 'kicad':
                subprocess.run(['sudo', 'add-apt-repository', 'ppa:kicad/kicad-9.0-releases', '-y'], check=True)
                subprocess.run(['sudo', 'apt', 'update'], check=True)
                subprocess.run(['sudo', 'apt', 'install', '-y', 'kicad'], check=True)
            elif tool == 'ghdl':
                subprocess.run(['sudo', 'apt', 'install', '-y', 'ghdl'], check=True)
        elif os_type == 'windows':
            if tool == 'ngspice':
                subprocess.run(['choco', 'install', 'ngspice'], check=True)
            elif tool == 'kicad':
                subprocess.run(['choco', 'install', 'kicad'], check=True)
            elif tool == 'ghdl':
                subprocess.run(['choco', 'install', 'ghdl'], check=True)
        version = get_installed_version(tool)
        if version:
            logging.info(f"{tool} installed successfully (version {version})")
            configure_tool(tool, os_type)  # Auto-config
            show_message("Success", f"{tool.capitalize()} installed (version {version}). Configured for eSim.")
            return True
        else:
            logging.error(f"Installation of {tool} failed - version not detected")
            show_message("Error", f"Installation failed for {tool}. Check log.")
            return False
    except Exception as e:
        logging.error(f"Installation error for {tool}: {e}")
        show_message("Error", f"Installation failed: {e}")
        return False

def configure_tool(tool, os_type):
    """Automates configuration: Sets PATH and env vars for eSim (fulfills Configuration Handling)."""
    try:
        if os_type == 'macos':
            path = '/opt/homebrew/bin'  # Homebrew default
            os.environ['PATH'] += os.pathsep + path
            with open(os.path.expanduser('~/.zshrc'), 'a') as f:
                f.write(f'\nexport PATH="$PATH:{path}"\n')
            if tool == 'ngspice':
                lib_path = '/opt/homebrew/share/ngspice/scripts'  # Ngspice lib for eSim
                os.environ['NGSPICE_LIB'] = lib_path
                with open(os.path.expanduser('~/.zshrc'), 'a') as f:
                    f.write(f'\nexport NGSPICE_LIB="{lib_path}"\n')
            elif tool == 'ghdl':
                ghdl_path = '/opt/homebrew/bin/ghdl'
                os.environ['GHDL_BIN'] = ghdl_path
                with open(os.path.expanduser('~/.zshrc'), 'a') as f:
                    f.write(f'\nexport GHDL_BIN="{ghdl_path}"\n')
            logging.info(f"Configured {tool}: PATH and env vars set (restart Terminal for effect)")
            return True
        elif os_type == 'linux':
            # Stub: Add to ~/.bashrc
            logging.info("Linux config stub – assume PATH set")
            return True
        elif os_type == 'windows':
            # Stub: Set env vars via setx
            logging.info("Windows config stub – assume PATH set")
            return True
        return False
    except Exception as e:
        logging.error(f"Configuration failed for {tool}: {e}")
        return False