"""
Utility functions for Termux environment verification and system information
"""

import subprocess
import sys
from typing import Dict, Optional, Tuple


def check_installation(command: str) -> bool:
    """
    Check if a command is installed
    
    Args:
        command: Command name to check
    
    Returns:
        True if command is available, False otherwise
    """
    try:
        result = subprocess.run(
            ["which", command],
            capture_output=True,
            text=True,
            timeout=5
        )
        return result.returncode == 0
    except Exception:
        return False


def verify_python() -> Dict[str, str]:
    """
    Verify Python installation and get version info
    
    Returns:
        Dictionary with Python version information
    """
    return {
        "executable": sys.executable,
        "version": sys.version,
        "version_info": f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}",
        "platform": sys.platform,
    }


def get_python_version() -> Tuple[int, int, int]:
    """Get Python version as tuple (major, minor, micro)"""
    return (sys.version_info.major, sys.version_info.minor, sys.version_info.micro)


def get_pip_version() -> Optional[str]:
    """Get pip version"""
    try:
        result = subprocess.run(
            [sys.executable, "-m", "pip", "--version"],
            capture_output=True,
            text=True,
            timeout=10
        )
        if result.returncode == 0:
            return result.stdout.strip()
    except Exception:
        pass
    return None


def get_git_version() -> Optional[str]:
    """Get git version"""
    try:
        result = subprocess.run(
            ["git", "--version"],
            capture_output=True,
            text=True,
            timeout=10
        )
        if result.returncode == 0:
            return result.stdout.strip()
    except Exception:
        pass
    return None


def get_system_info() -> Dict[str, any]:
    """
    Get comprehensive system information
    
    Returns:
        Dictionary with system and Python environment information
    """
    info = {
        "python": verify_python(),
        "pip_version": get_pip_version(),
        "git_installed": check_installation("git"),
        "git_version": get_git_version(),
        "curl_installed": check_installation("curl"),
        "wget_installed": check_installation("wget"),
        "nano_installed": check_installation("nano"),
        "vim_installed": check_installation("vim"),
    }
    return info


def list_installed_python_packages() -> Dict[str, str]:
    """List installed Python packages and their versions"""
    try:
        result = subprocess.run(
            [sys.executable, "-m", "pip", "list", "--format=json"],
            capture_output=True,
            text=True,
            timeout=30
        )
        if result.returncode == 0:
            import json
            packages = json.loads(result.stdout)
            return {pkg["name"]: pkg["version"] for pkg in packages}
    except Exception:
        pass
    return {}


def verify_environment_complete() -> Dict[str, bool]:
    """
    Verify that all essential tools are installed
    
    Returns:
        Dictionary with verification status of each tool
    """
    essential_tools = {
        "python": check_installation("python"),
        "pip": check_installation("pip"),
        "git": check_installation("git"),
        "curl": check_installation("curl"),
        "wget": check_installation("wget"),
    }
    return essential_tools


def print_system_report():
    """Print a formatted system information report"""
    info = get_system_info()
    
    print("\n" + "="*50)
    print("SYSTEM INFORMATION REPORT")
    print("="*50)
    
    print("\nPython Environment:")
    for key, value in info["python"].items():
        print(f"  {key}: {value}")
    
    print("\nPackage Managers:")
    print(f"  pip: {info['pip_version'] or 'Not found'}")
    print(f"  git: {info['git_version'] or 'Not found'}")
    
    print("\nInstalled Tools:")
    tools = ["curl_installed", "wget_installed", "nano_installed", "vim_installed"]
    for tool in tools:
        status = "✓ Installed" if info[tool] else "✗ Not found"
        tool_name = tool.replace("_installed", "")
        print(f"  {tool_name}: {status}")
    
    print("\n" + "="*50 + "\n")
