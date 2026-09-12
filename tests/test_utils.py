"""
Unit tests for Termux Python development utilities
"""

import pytest
from termux_python_dev.utils import (
    check_installation,
    verify_python,
    get_python_version,
    verify_environment_complete,
)


class TestUtils:
    """Test utility functions"""
    
    def test_check_installation(self):
        """Test checking installation of a command"""
        # Python should be installed in Termux environment
        assert isinstance(check_installation("python"), bool)
    
    def test_verify_python(self):
        """Test Python verification"""
        info = verify_python()
        assert isinstance(info, dict)
        assert "executable" in info
        assert "version" in info
        assert "version_info" in info
        assert "platform" in info
    
    def test_get_python_version(self):
        """Test getting Python version tuple"""
        version = get_python_version()
        assert isinstance(version, tuple)
        assert len(version) == 3
        assert all(isinstance(x, int) for x in version)
        assert version[0] >= 3  # Python 3+
        assert version[1] >= 9  # Python 3.9+
    
    def test_verify_environment_complete(self):
        """Test environment verification"""
        result = verify_environment_complete()
        assert isinstance(result, dict)
        assert "python" in result
        assert "pip" in result
        assert "git" in result
        # All results should be boolean
        for key, value in result.items():
            assert isinstance(value, bool)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
