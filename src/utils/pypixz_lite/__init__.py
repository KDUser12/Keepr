# (c) 2025 YourLabXYZ.
# Licensed under MIT License.

""" PyPIxz LITE

PyPIxz LITE is a tool for installing packages for your python programs at launch by removing
various functionality that requires various other modules.
"""

from .install_packages import install_requirements, install_modules

__version__ = '1.0.0'
__all__ = [
    'install_requirements',
    'install_modules'
]
__author__ = 'YourLabXYZ - Organizations on GitHub'
