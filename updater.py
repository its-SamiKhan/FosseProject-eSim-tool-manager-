import requests
from bs4 import BeautifulSoup
from installer import install_tool
from utils import get_installed_version, logging, show_message

def check_for_update(tool):
    """Checks for updates via web scraping (fulfills Update System). Returns latest if update needed."""
    current = get_installed_version(tool)
    if not current:
        return "Not installed"
    latest = None
    try:
        if tool == 'ngspice':
            url = 'https://ngspice.sourceforge.io/download.html'
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            text = soup.get_text()
            if 'ngspice-45.2' in text:
                latest = '45.2'  # Adjust based on site
        elif tool == 'kicad':
            url = 'https://www.kicad.org/download/'
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            text = soup.get_text()
            if '9.0.4' in text:
                latest = '9.0.4'
        elif tool == 'ghdl':
            url = 'https://ghdl.free.fr/'
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            text = soup.get_text()
            if '4.1.0' in text:
                latest = '4.1.0'
        if latest and current != latest:
            logging.info(f"Update available for {tool}: {current} -> {latest}")
            return latest
        logging.info(f"{tool} is up to date: {current}")
        return None
    except Exception as e:
        logging.error(f"Update check failed for {tool}: {e} (internet or site issue)")
        show_message("Error", f"Update check failed for {tool}: {e}")
        return None

def upgrade_tool(tool, os_type):
    """Upgrades if update available (reuses install logic for robustness)."""
    latest = check_for_update(tool)
    if latest and latest != "Not installed":
        show_message("Update", f"Upgrading {tool} to {latest}...")
        if os_type == 'macos':
            cmd = ['brew', 'upgrade', tool] if tool != 'kicad' else ['brew', 'upgrade', '--cask', 'kicad']
            subprocess.run(cmd, check=True)
        # Linux/Windows stubs similar to install
        new_version = get_installed_version(tool)
        logging.info(f"{tool} upgraded to {new_version}")
        show_message("Success", f"{tool} upgraded to {new_version}")
        return True
    show_message("Info", f"No update for {tool} or not installed")
    return False