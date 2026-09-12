"""
Core module for Termux environment management
Provides classes for managing packages and environment setup
"""

import subprocess
import sys
from typing import List, Dict, Optional


class PackageManager:
    """Manage Termux packages"""
    
    def __init__(self):
        self.errors = []
        self.successes = []
    
    def update(self) -> bool:
        """Update package lists"""
        try:
            result = subprocess.run(
                ["pkg", "update", "-y"],
                capture_output=True,
                text=True,
                timeout=300
            )
            if result.returncode == 0:
                self.successes.append("Package lists updated")
                return True
            else:
                self.errors.append(f"Update failed: {result.stderr}")
                return False
        except Exception as e:
            self.errors.append(f"Update error: {str(e)}")
            return False
    
    def upgrade(self) -> bool:
        """Upgrade all packages"""
        try:
            result = subprocess.run(
                ["pkg", "upgrade", "-y"],
                capture_output=True,
                text=True,
                timeout=300
            )
            if result.returncode == 0:
                self.successes.append("Packages upgraded successfully")
                return True
            else:
                self.errors.append(f"Upgrade failed: {result.stderr}")
                return False
        except Exception as e:
            self.errors.append(f"Upgrade error: {str(e)}")
            return False
    
    def install(self, packages: List[str]) -> Dict[str, bool]:
        """Install multiple packages"""
        results = {}
        for package in packages:
            try:
                result = subprocess.run(
                    ["pkg", "install", "-y", package],
                    capture_output=True,
                    text=True,
                    timeout=300
                )
                if result.returncode == 0:
                    results[package] = True
                    self.successes.append(f"Installed {package}")
                else:
                    results[package] = False
                    self.errors.append(f"Failed to install {package}")
            except Exception as e:
                results[package] = False
                self.errors.append(f"Error installing {package}: {str(e)}")
        return results
    
    def pip_upgrade(self) -> bool:
        """Upgrade pip"""
        try:
            result = subprocess.run(
                [sys.executable, "-m", "pip", "install", "--upgrade", "pip"],
                capture_output=True,
                text=True,
                timeout=300
            )
            if result.returncode == 0:
                self.successes.append("pip upgraded successfully")
                return True
            else:
                self.errors.append(f"pip upgrade failed: {result.stderr}")
                return False
        except Exception as e:
            self.errors.append(f"pip upgrade error: {str(e)}")
            return False
    
    def pip_install(self, packages: List[str]) -> Dict[str, bool]:
        """Install Python packages via pip"""
        results = {}
        for package in packages:
            try:
                result = subprocess.run(
                    [sys.executable, "-m", "pip", "install", "--quiet", package],
                    capture_output=True,
                    text=True,
                    timeout=300
                )
                if result.returncode == 0:
                    results[package] = True
                    self.successes.append(f"Installed Python package: {package}")
                else:
                    results[package] = False
                    self.errors.append(f"Failed to install Python package {package}")
            except Exception as e:
                results[package] = False
                self.errors.append(f"Error installing {package}: {str(e)}")
        return results


class TermuxEnvironment:
    """Manage Termux Python development environment"""
    
    def __init__(self):
        self.package_manager = PackageManager()
        self.system_packages = [
            "python",
            "python-pip",
            "git",
            "curl",
            "wget",
            "nano",
            "vim",
            "build-essential",
            "clang",
            "pkg-config",
            "libffi-dev",
            "openssl-dev",
        ]
        self.python_packages = [
            "requests",
            "numpy",
            "pandas",
            "matplotlib",
            "pytest",
            "black",
            "flake8",
            "ipython",
            "jupyter",
        ]
    
    def setup_environment(self, install_python_packages: bool = True) -> bool:
        """Complete environment setup"""
        print("Setting up Termux Python development environment...")
        
        # Update packages
        if not self.package_manager.update():
            print("Warning: Package update failed")
        
        # Upgrade packages
        if not self.package_manager.upgrade():
            print("Warning: Package upgrade failed")
        
        # Install system packages
        print(f"Installing {len(self.system_packages)} system packages...")
        self.package_manager.install(self.system_packages)
        
        # Upgrade pip
        if not self.package_manager.pip_upgrade():
            print("Warning: pip upgrade failed")
        
        # Install Python packages
        if install_python_packages:
            print(f"Installing {len(self.python_packages)} Python packages...")
            self.package_manager.pip_install(self.python_packages)
        
        return len(self.package_manager.errors) == 0
    
    def get_status(self) -> Dict:
        """Get environment setup status"""
        return {
            "successes": self.package_manager.successes,
            "errors": self.package_manager.errors,
            "total_successes": len(self.package_manager.successes),
            "total_errors": len(self.package_manager.errors),
        }
