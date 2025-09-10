import requests
from bs4 import BeautifulSoup
from installer import install_tool  # Reuse install for upgrade
from utils import get_installed_version, logging

def check_for_update(tool):
    """Check latest version from web. Returns latest if update needed, else None."""
    current = get_installed_version(tool)
    if not current:
        return "Not installed"
    
    latest = None
    try:
        if tool == 'ngspice':
            url = 'https://ngspice.sourceforge.io/download.html'
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            # Parse: Look for "ngspice-45.2" in text (adjust selector if site changes)
            text = soup.get_text()
            if 'ngspice-45.2' in text:  # From research
                latest = '45.2'
            # Alternative: Find release link
            release_link = soup.find('a', href=lambda h: h and 'ngspice-45' in h)
            if release_link:
                latest = release_link.text.split('-')[1] if '-' in release_link.text else None
        elif tool == 'kicad':
            url = 'https://www.kicad.org/download/'
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            # Parse: Look for "9.0.4" in stable release section
            text = soup.get_text()
            if '9.0.4' in text and 'stable' in text.lower():
                latest = '9.0.4'
            # Alternative: Find h2 or div with version
            version_elem = soup.find('strong', string=lambda s: s and '9.0' in s)
            if version_elem:
                latest = version_elem.text.strip()
        
        if latest and current != latest:
            logging.info(f"Update available for {tool}: {current} -> {latest}")
            return latest
        else:
            logging.info(f"{tool} is up to date: {current}")
            return None
    except Exception as e:
        logging.error(f"Update check failed for {tool}: {e} (check internet/site changes)")
        return None

def upgrade_tool(tool, os_type):
    """Upgrade if update available. Uses install logic."""
    latest = check_for_update(tool)
    if latest and latest != "Not installed":
        print(f"Upgrading {tool} to {latest}...")
        # For macOS, brew upgrade reinstalls latest
        if os_type == 'macos':
            subprocess.run(['brew', 'upgrade', tool if tool != 'kicad' else f'--cask {tool}'], check=True)
        # Similar for Linux/Windows stubs
        new_version = get_installed_version(tool)
        logging.info(f"{tool} upgraded to {new_version}")
        return True
    else:
        print(f"No update for {tool}")
        return False

if __name__ == "__main__":
    # Test: python updater.py
    os_type = detect_os()
    upgrade_tool('ngspice', os_type)