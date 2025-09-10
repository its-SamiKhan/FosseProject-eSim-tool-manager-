from utils import detect_os, load_tools, save_tools, show_message, get_installed_version  # Added get_installed_version
from installer import install_tool
from updater import upgrade_tool
import tkinter as tk
from tkinter import ttk

def create_gui(tools, os_type):
    root = tk.Tk()
    root.title("Advanced eSim Tool Manager")
    root.geometry("500x400")

    label = ttk.Label(root, text="Advanced eSim Tool Manager", font=("Arial", 16))
    label.pack(pady=10)

    def on_action(action, tool):
        if action == 'install':
            if install_tool(tool, os_type):
                tools[tool] = get_installed_version(tool)
                save_tools(tools)
        elif action == 'update':
            if upgrade_tool(tool, os_type):
                tools[tool] = get_installed_version(tool)
                save_tools(tools)

    def on_view():
        msg = "Installed Tools:\n"
        for tool, version in tools.items():
            msg += f"{tool.capitalize()}: {version or 'Not installed'}\n"
        show_message("Tools", msg)

    tools_list = ['ngspice', 'kicad', 'ghdl']
    for tool in tools_list:
        frame = ttk.Frame(root)
        frame.pack(pady=5)
        ttk.Label(frame, text=tool.capitalize()).pack(side=tk.LEFT, padx=5)
        ttk.Button(frame, text="Install", command=lambda t=tool: on_action('install', t)).pack(side=tk.LEFT, padx=5)
        ttk.Button(frame, text="Update", command=lambda t=tool: on_action('update', t)).pack(side=tk.LEFT, padx=5)

    ttk.Button(root, text="View Tools", command=on_view).pack(pady=10)
    ttk.Button(root, text="Exit", command=root.quit).pack(pady=5)

    root.mainloop()

def main():
    os_type = detect_os()
    if not os_type:
        show_message("Error", "Unsupported OS – macOS/Linux/Windows only")
        return
    tools = load_tools()
    create_gui(tools, os_type)

if __name__ == "__main__":
    main()