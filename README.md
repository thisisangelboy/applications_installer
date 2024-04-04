# Applications Installer

Applications Installer is a Python script that automates the installation of popular applications on Windows x64 systems. It provides a convenient way to install multiple applications with a single command, saving time and effort.

## Features

- Installs the latest stable versions of the following applications:
  - Python
  - Visual Studio Code
  - Wireshark
  - Firefox
  - Google Chrome
  - VLC Media Player
  - VMware Workstation Pro
- Allows users to select specific applications to install or perform a full installation of all applications
- Silently installs applications in the English language, regardless of the system's language settings
- Automatically adds installed applications to the system PATH when necessary
- Provides a user-friendly command-line interface for easy interaction

## Prerequisites

- Windows x64 operating system
- Internet connection to download the application installers
- Administrator privileges to install applications

## Usage

### Using the Python Script (`appinstaller.py`)

1. Make sure you have Python installed on your system.
2. Install the required dependencies by running the following command:
   ```
   pip install requests beautifulsoup4
   ```
3. Download the `appinstaller.py` script from the repository.
4. Open a command prompt or terminal with administrator privileges.
5. Navigate to the directory where the script is located.
6. Run the script using the following command:
   ```
   python appinstaller.py
   ```
7. Follow the on-screen instructions to select the applications you want to install.
8. The script will download and install the selected applications automatically.

### Using the Standalone Executable (`appinstaller.exe`)

1. Download the `appinstaller.exe` file from the repository.
2. Right-click on the `appinstaller.exe` file and select "Run as administrator" to run the installer with administrator privileges.
3. Follow the on-screen instructions to select the applications you want to install.
4. The installer will download and install the selected applications automatically.

## Configuration

- The script installs applications silently in the English language by default. If you want to modify the installation language or other installation parameters, you can edit the respective installation commands in the script.
- The script adds Wireshark to the system PATH by default. If you don't want this behavior, you can remove or comment out the relevant code block in the script.

## Troubleshooting

- If you encounter any issues during the installation process, please check your internet connection and ensure that you have sufficient permissions to install applications on your system.
- If an application fails to install, you can try running the script again with administrator privileges.

## Contributing

Contributions to the Applications Installer project are welcome! If you find any bugs, have suggestions for improvements, or want to add support for additional applications, please open an issue or submit a pull request on the GitHub repository.

## License

This project is licensed under the [MIT License](LICENSE).

## Disclaimer

The Applications Installer script is provided as-is without any warranty. Use it at your own risk. The authors and contributors of this script are not responsible for any damage or loss caused by the use of this script.

Please note that the installation of third-party applications is subject to their respective licenses and terms of use. Make sure to review and agree to the licenses of the applications before installing them using this script.
