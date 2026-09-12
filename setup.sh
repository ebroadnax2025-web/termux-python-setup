#!/bin/bash

# Termux Python Development Environment Setup Script
# Automatically updates packages and installs development tools
# Compatible with Android/Termux without root access

echo "=========================================="
echo "Termux Python Development Setup"
echo "=========================================="
echo ""

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Function to print colored output
print_status() {
    echo -e "${GREEN}[✓]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[!]${NC} $1"
}

print_error() {
    echo -e "${RED}[✗]${NC} $1"
}

# Step 1: Update package manager
echo ""
print_warning "Step 1: Updating package lists..."
pkg update -y
if [ $? -eq 0 ]; then
    print_status "Package lists updated successfully"
else
    print_error "Failed to update package lists"
    exit 1
fi

# Step 2: Upgrade existing packages
echo ""
print_warning "Step 2: Upgrading existing packages..."
pkg upgrade -y
if [ $? -eq 0 ]; then
    print_status "Packages upgraded successfully"
else
    print_error "Failed to upgrade packages"
fi

# Step 3: Install essential development tools
echo ""
print_warning "Step 3: Installing essential development tools..."

PACKAGES=(
    "python"
    "python-pip"
    "git"
    "curl"
    "wget"
    "nano"
    "vim"
    "build-essential"
    "clang"
    "pkg-config"
    "libffi-dev"
    "openssl-dev"
)

for package in "${PACKAGES[@]}"; do
    echo "Installing $package..."
    pkg install -y "$package"
    if [ $? -eq 0 ]; then
        print_status "$package installed"
    else
        print_warning "Could not install $package (may already exist)"
    fi
done

# Step 4: Upgrade pip
echo ""
print_warning "Step 4: Upgrading pip..."
python -m pip install --upgrade pip
if [ $? -eq 0 ]; then
    print_status "pip upgraded successfully"
else
    print_error "Failed to upgrade pip"
fi

# Step 5: Install common Python packages
echo ""
print_warning "Step 5: Installing common Python packages..."

PY_PACKAGES=(
    "requests"
    "numpy"
    "pandas"
    "matplotlib"
    "pytest"
    "black"
    "flake8"
    "ipython"
    "jupyter"
)

for package in "${PY_PACKAGES[@]}"; do
    echo "Installing Python package: $package..."
    pip install "$package" --quiet
    if [ $? -eq 0 ]; then
        print_status "Python package $package installed"
    else
        print_warning "Could not install Python package $package"
    fi
done

# Step 6: Verify installations
echo ""
print_warning "Step 6: Verifying installations..."
echo ""

echo "Python version:"
python --version

echo "Pip version:"
pip --version

echo "Git version:"
git --version

# Step 7: Create project structure
echo ""
print_warning "Step 7: Creating Python project structure..."

PROJECT_DIR="$HOME/python-projects"
if [ ! -d "$PROJECT_DIR" ]; then
    mkdir -p "$PROJECT_DIR"
    print_status "Created project directory: $PROJECT_DIR"
else
    print_warning "Project directory already exists: $PROJECT_DIR"
fi

# Step 8: Create virtual environment template
echo ""
print_warning "Step 8: Setting up virtual environment..."

VENV_DIR="$PROJECT_DIR/venv"
if [ ! -d "$VENV_DIR" ]; then
    python -m venv "$VENV_DIR"
    print_status "Virtual environment created at $VENV_DIR"
else
    print_warning "Virtual environment already exists"
fi

# Final summary
echo ""
echo "=========================================="
echo -e "${GREEN}Setup Complete!${NC}"
echo "=========================================="
echo ""
echo "Quick start commands:"
echo "  1. Activate virtual environment:"
echo "     source $VENV_DIR/bin/activate"
echo ""
echo "  2. Create new Python project:"
echo "     mkdir $PROJECT_DIR/my-project && cd $PROJECT_DIR/my-project"
echo ""
echo "  3. Install packages:"
echo "     pip install <package-name>"
echo ""
echo "  4. Check for updates:"
echo "     pkg update && pkg upgrade"
echo ""
echo "=========================================="
