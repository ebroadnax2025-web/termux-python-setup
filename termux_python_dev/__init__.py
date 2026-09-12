"""
Termux Python Development Environment Package
Main module for Termux Python development tools and utilities
"""

__version__ = "1.0.0"
__author__ = "ebroadnax2025-web"
__email__ = "ebroadnax2025@gmail.com"
__description__ = "Python development environment setup for Android/Termux"

from .core import TermuxEnvironment, PackageManager
from .utils import check_installation, verify_python, get_system_info

__all__ = [
    "TermuxEnvironment",
    "PackageManager",
    "check_installation",
    "verify_python",
    "get_system_info",
]
