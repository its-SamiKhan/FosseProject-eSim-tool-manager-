import os
from utils import detect_os, load_tools, save_tools
from installer import install_tool
from updater import upgrade_tool

def main():
    os_type = detect_os()
    if not os_type:
        print("Unsupported OS. Exiting.")
        return
    
    tools = load_tools()
    
    while True:
        print("\n=== eSim Automated Tool Manager ===")
        print("1. Install Ngspice")
        print("2. Install KiCad")
        print("3. Check/Update Ngspice")
        print("4. Check/Update KiCad")
        print("5. View Installed Tools")
        print("6. Exit")
        choice = input("Enter choice (1-6): ").strip()
        
        if choice == '1':
            if install_tool('ngspice', os_type):
                tools['ngspice'] = get_installed_version('ngspice')  # From utils
                save_tools(tools)
        elif choice == '2':
            if install_tool('kicad', os_type):
                tools['kicad'] = get_installed_version('kicad')
                save_tools(tools)
        elif choice == '3':
            upgrade_tool('ngspice', os_type)
            tools['ngspice'] = get_installed_version('ngspice')
            save_tools(tools)
        elif choice == '4':
            upgrade_tool('kicad', os_type)
            tools['kicad'] = get_installed_version('kicad')
            save_tools(tools)
        elif choice == '5':
            print("Installed Tools:")
            for tool, version in tools.items():
                print(f"  {tool}: {version or 'Not installed'}")
        elif choice == '6':
            print("Exiting. Check tool_manager.log for logs.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()