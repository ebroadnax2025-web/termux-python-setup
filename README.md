# Termux Python Development Setup

A comprehensive Python package and Bash setup script for creating a complete Python development environment on Android/Termux without requiring root access.

## Features

✅ **Automatic Package Management**
- Update and upgrade system packages
- Install essential development tools (Python, Git, build tools)
- Install common Python packages
- Pip upgrade and management

✅ **No Root Required**
- Works entirely within Termux environment
- No elevated privileges needed
- Fully compatible with Android

✅ **Complete Python Ecosystem**
- Python 3.9+
- pip package manager
- Virtual environment support
- Popular data science libraries (NumPy, Pandas, Matplotlib)
- Testing and code quality tools (pytest, black, flake8)

✅ **System Information**
- Verify Python installation
- Check system tools availability
- List installed packages
- Generate system reports

## Quick Start

### Option 1: Using the Bash Script (Recommended)

```bash
# Clone the repository
git clone https://github.com/ebroadnax2025-web/termux-python-setup.git
cd termux-python-setup

# Make the setup script executable
chmod +x setup.sh

# Run the setup script
bash setup.sh
```

### Option 2: Using Python Package

```bash
# Clone and install
git clone https://github.com/ebroadnax2025-web/termux-python-setup.git
cd termux-python-setup

# Install the package
pip install -e .

# Use in Python
python
>>> from termux_python_dev import TermuxEnvironment
>>> env = TermuxEnvironment()
>>> env.setup_environment()
```

### Option 3: Manual Setup (Advanced)

```bash
# Update packages
pkg update
pkg upgrade

# Install essential tools
pkg install -y python python-pip git curl wget

# Upgrade pip
python -m pip install --upgrade pip

# Install common packages
pip install requests numpy pandas matplotlib pytest black flake8
```

## Usage Examples

### Python Package API

```python
from termux_python_dev import TermuxEnvironment, get_system_info

# Initialize environment
env = TermuxEnvironment()

# Setup complete environment
env.setup_environment()

# Check status
status = env.get_status()
print(f"Successes: {status['total_successes']}")
print(f"Errors: {status['total_errors']}")

# Get system information
info = get_system_info()
print(info)
```

### Package Manager

```python
from termux_python_dev.core import PackageManager

pm = PackageManager()

# Update packages
pm.update()

# Install packages
packages = ["git", "curl", "wget"]
results = pm.install(packages)

# Install Python packages
py_packages = ["requests", "numpy"]
results = pm.pip_install(py_packages)
```

### System Verification

```python
from termux_python_dev.utils import (
    check_installation,
    verify_python,
    get_system_info,
    print_system_report
)

# Check if a command is installed
is_git_installed = check_installation("git")

# Verify Python
python_info = verify_python()

# Get comprehensive system info
sys_info = get_system_info()

# Print formatted report
print_system_report()
```

## Installation Options

### From Source

```bash
git clone https://github.com/ebroadnax2025-web/termux-python-setup.git
cd termux-python-setup
pip install -e .
```

### With Development Tools

```bash
git clone https://github.com/ebroadnax2025-web/termux-python-setup.git
cd termux-python-setup
pip install -e ".[dev]"
```

### With Data Science Tools

```bash
git clone https://github.com/ebroadnax2025-web/termux-python-setup.git
cd termux-python-setup
pip install -e ".[data]"
```

### Everything

```bash
pip install -e ".[all]"
```

## Project Structure

```
termux-python-setup/
├── setup.sh                      # Main Bash setup script
├── setup.py                      # Package installation config
├── pyproject.toml                # Modern Python package config
├── README.md                     # This file
├── .gitignore                    # Git ignore rules
├── requirements.txt              # Python dependencies
├── termux_python_dev/
│   ├── __init__.py              # Package initialization
│   ├── core.py                  # Core environment & package management
│   └── utils.py                 # Utility functions
└── tests/
    ├── __init__.py
    └── test_utils.py            # Unit tests
```

## Included Packages

### System Tools
- `python` - Python 3.9+
- `python-pip` - Package installer
- `git` - Version control
- `curl` - HTTP client
- `wget` - File downloader
- `nano` - Text editor
- `vim` - Advanced text editor
- `build-essential` - Build tools
- `clang` - C/C++ compiler
- `pkg-config` - Library metadata
- `libffi-dev` - Foreign function interface
- `openssl-dev` - SSL/TLS library

### Python Packages
- `requests` - HTTP library
- `numpy` - Numerical computing
- `pandas` - Data analysis
- `matplotlib` - Plotting library
- `pytest` - Testing framework
- `black` - Code formatter
- `flake8` - Linter
- `ipython` - Interactive shell
- `jupyter` - Notebook environment

## Virtual Environment

Create and use virtual environments:

```bash
# Create virtual environment
python -m venv my_project

# Activate environment
source my_project/bin/activate

# Deactivate environment
deactivate
```

## Troubleshooting

### Permission Denied on setup.sh

```bash
chmod +x setup.sh
bash setup.sh
```

### Package Installation Fails

```bash
# Update package lists first
pkg update

# Try again
pkg install -y package_name
```

### Python Not Found

```bash
# Install Python explicitly
pkg install -y python

# Check installation
python --version
which python
```

### Pip Not Working

```bash
# Reinstall pip
python -m pip install --upgrade pip

# Or use the Python installer
pkg install -y python-pip
```

## Requirements

- **Android Device** with Termux installed
- **Termux App** (free on Google Play Store)
- **Internet Connection** for downloading packages
- **~2GB Storage Space** for all tools and packages

## System Requirements

- Python 3.9+
- Bash shell
- Termux environment

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for bugs and feature requests.

## License

This project is licensed under the MIT License - see LICENSE file for details.

## Author

**ebroadnax2025-web**

## Support

For issues, questions, or suggestions, please open an issue on GitHub:
[Issues](https://github.com/ebroadnax2025-web/termux-python-setup/issues)

## Changelog

### Version 1.0.0
- Initial release
- Complete Bash setup script
- Python package with environment management
- System verification utilities
- Comprehensive documentation

---

**Happy coding on Android!** 🚀
