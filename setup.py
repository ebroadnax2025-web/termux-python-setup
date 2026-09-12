from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="termux-python-dev",
    version="1.0.0",
    author="ebroadnax2025-web",
    description="Comprehensive Python development environment setup for Android/Termux",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ebroadnax2025-web/termux-python-setup",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Android",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
    ],
    python_requires=">=3.9",
    install_requires=[
        "requests>=2.28.0",
        "numpy>=1.24.0",
        "pandas>=1.5.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0",
            "black>=22.0",
            "flake8>=4.0",
        ],
        "data": [
            "matplotlib>=3.5.0",
            "scipy>=1.8.0",
        ],
    },
)
