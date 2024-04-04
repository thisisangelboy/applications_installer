import os
import requests
import subprocess
import re
import winreg
from bs4 import BeautifulSoup

print("Applications Installer by Ratel Systems")
print()  # Add an empty line

# Define the list of applications
applications = [
    "Python",
    "Visual Studio Code",
    "Wireshark",
    "Firefox",
    "Google Chrome",
    "VLC Media Player",
    "VMware Workstation Pro"
]

# Display the list of applications
print("Please select the applications you want to install:")
print()  # Add an empty line
print("0. Full Installation")
for i, app in enumerate(applications, start=1):
    print(f"{i}. {app}")

# Get user input for application selection
print()  # Add an empty line
user_input = input("Enter the application numbers separated by commas or spaces (e.g., 1, 2, 3):\n")

# Parse user input
selected_apps = []
if "0" in user_input:
    selected_apps = list(range(1, len(applications) + 1))
else:
    selected_apps = [int(num) for num in re.findall(r'\d+', user_input)]

print("Installation in progress...")

# Install selected applications
for app_num in selected_apps:
    if app_num == 1:  # Python
        # Get the latest stable Python version
        python_url = "https://www.python.org/downloads/"
        response = requests.get(python_url)
        match = re.search(r'Download Python (\d\.\d+\.\d+)', response.text)
        if match:
            python_version = match.group(1)
        else:
            raise ValueError("Failed to retrieve the latest Python version.")

        # Create the Python installer URL for Windows x64
        python_installer_url = f"https://www.python.org/ftp/python/{python_version}/python-{python_version}-amd64.exe"

        # Download the latest Python installer for Windows x64
        python_installer_path = "python_installer.exe"
        response = requests.get(python_installer_url)
        with open(python_installer_path, "wb") as file:
            file.write(response.content)

        # Install Python silently in English and add Python to PATH
        python_install_command = f"{python_installer_path} /quiet InstallAllUsers=1 PrependPath=1 Include_test=0 Include_doc=0 Include_launcher=0 Include_tcltk=0 /L=1033"
        subprocess.run(python_install_command, shell=True)

        # Clean up the Python installer file
        os.remove(python_installer_path)

        print(f"Python {python_version} installation completed successfully.")

    elif app_num == 2:  # Visual Studio Code
        # Download the latest stable Visual Studio Code installer for Windows x64
        vscode_installer_url = "https://code.visualstudio.com/sha/download?build=stable&os=win32-x64"
        vscode_installer_path = "vscode_installer.exe"
        response = requests.get(vscode_installer_url)
        with open(vscode_installer_path, "wb") as file:
            file.write(response.content)

        # Install Visual Studio Code silently in English
        vscode_install_command = f"{vscode_installer_path} /verysilent /norestart /mergetasks=!runcode /LANG=en-US"
        subprocess.run(vscode_install_command, shell=True)

        # Clean up the Visual Studio Code installer file
        os.remove(vscode_installer_path)

        print("Visual Studio Code installation completed successfully.")

    elif app_num == 3:  # Wireshark
        # Download the latest stable Wireshark installer for Windows x64
        wireshark_installer_url = "https://2.na.dl.wireshark.org/win64/Wireshark-latest-x64.exe"
        wireshark_installer_path = "wireshark_installer.exe"
        response = requests.get(wireshark_installer_url)
        with open(wireshark_installer_path, "wb") as file:
            file.write(response.content)

        # Install Wireshark silently in English
        wireshark_install_command = [
            wireshark_installer_path,
            "/S",
            "/quicklaunchicon=no",
            "/desktopicon=no",
            "/D=C:\\Program Files\\Wireshark",
            "/L=English"
        ]
        subprocess.run(wireshark_install_command, shell=True)

        # Clean up the Wireshark installer file
        os.remove(wireshark_installer_path)

        print("Wireshark installation completed successfully.")

        # Add Wireshark to the system PATH
        wireshark_path = "C:\\Program Files\\Wireshark"
        reg_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, "SYSTEM\\CurrentControlSet\\Control\\Session Manager\\Environment", 0, winreg.KEY_ALL_ACCESS)
        path_value, _ = winreg.QueryValueEx(reg_key, "Path")
        new_path_value = f"{path_value};{wireshark_path}"
        winreg.SetValueEx(reg_key, "Path", 0, winreg.REG_EXPAND_SZ, new_path_value)
        winreg.CloseKey(reg_key)

        print("Wireshark added to the system PATH.")

    elif app_num == 4:  # Firefox
        # Download the latest stable Firefox installer for Windows x64
        firefox_installer_url = "https://download.mozilla.org/?product=firefox-latest-ssl&os=win64&lang=en-US"
        firefox_installer_path = "firefox_installer.exe"
        response = requests.get(firefox_installer_url)
        with open(firefox_installer_path, "wb") as file:
            file.write(response.content)

        # Install Firefox silently in English
        firefox_install_command = f"{firefox_installer_path} /S"
        subprocess.run(firefox_install_command, shell=True)

        # Clean up the Firefox installer file
        os.remove(firefox_installer_path)

        print("Firefox installation completed successfully.")

    elif app_num == 5:  # Google Chrome
        # Download the latest stable Google Chrome installer for Windows x64
        chrome_installer_url = "https://dl.google.com/chrome/install/latest/chrome_installer.exe"
        chrome_installer_path = "chrome_installer.exe"
        response = requests.get(chrome_installer_url)
        with open(chrome_installer_path, "wb") as file:
            file.write(response.content)

        # Install Google Chrome silently in English
        chrome_install_command = f"{chrome_installer_path} /silent /install"
        subprocess.run(chrome_install_command, shell=True)

        # Clean up the Google Chrome installer file
        os.remove(chrome_installer_path)

        print("Google Chrome installation completed successfully.")

    elif app_num == 6:  # VLC Media Player
        # Get the latest stable VLC Media Player installer URL for Windows x64
        vlc_url = "https://get.videolan.org/vlc/last/win64/"
        response = requests.get(vlc_url)
        soup = BeautifulSoup(response.text, "html.parser")
        vlc_installer_url = vlc_url + soup.find("a", href=re.compile(r"\.exe$"))["href"]

        # Download the latest stable VLC Media Player installer for Windows x64
        vlc_installer_path = "vlc_installer.exe"
        response = requests.get(vlc_installer_url)
        with open(vlc_installer_path, "wb") as file:
            file.write(response.content)

        # Install VLC Media Player silently in English
        vlc_install_command = f"{vlc_installer_path} /S"
        subprocess.run(vlc_install_command, shell=True)

        # Clean up the VLC Media Player installer file
        os.remove(vlc_installer_path)

        print("VLC Media Player installation completed successfully.")

    elif app_num == 7:  # VMware Workstation Pro
        # Download the latest stable VMware Workstation Pro installer for Windows
        vmware_installer_url = "https://download3.vmware.com/software/WKST-1751-WIN/VMware-workstation-full-17.5.1-23298084.exe"
        vmware_installer_path = "vmware_installer.exe"
        response = requests.get(vmware_installer_url)
        with open(vmware_installer_path, "wb") as file:
            file.write(response.content)

        # Install VMware Workstation Pro silently with enhanced keyboard driver and disable anonymous data collection
        vmware_install_command = f"{vmware_installer_path} /s /v\"/qn EULAS_AGREED=1 INSTALLENHANCEDKEYBOARD=1 DATACOLLECTION=0\""
        subprocess.run(vmware_install_command, shell=True)

        # Clean up the VMware Workstation Pro installer file
        os.remove(vmware_installer_path)

        print("VMware Workstation Pro installation completed successfully.")

print("All selected applications have been installed successfully.")