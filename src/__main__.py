#!/usr/bin/env python3

""" Keepr-CLI 

Keepr is a local password management application.
It allows users to store, organize, and secure credentials without any internet connection. 
The project is developed primarily in Python.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This version of Keepr is command line only.
"""

import argparse
import logging
try:  # Python 2.7+
    from logging.config import dictConfig
except ImportError as error:
    raise(f"Unable to import the module needed for logging. Check that your Python version is 2.7 or later.\n{error}")

from __init__ import __version__


def argparse_setup() -> argparse.Namespace:
    """argparse_setup Configures the argparse module.

    This function create and configuration an `argparse.ArgumentParser` object to manage the program's launch arguments.

    Returns:
        argparse.Namespace -- An object containing the parsed arguments.
    """
    
    parser = argparse.ArgumentParser(description=f"Keepr-CLI ({__version__})")
    parser.add_argument("-v", "--version", action="version", version=f"Keepr-CLI - {__version__}")
    parser.add_argument("-u", "--update", action="store_true", help="update the program to the latest version")
    parser.add_argument("--skip-check", nargs="+", choices=["os", "env", "packages", "all"], help="pass the program launch checks")
    parser.add_argument("--debug", action="store_true", help="enable debug output")
    args = parser.parse_args()
    
    return parser, args


def main():
    parser, args = argparse_setup
    
    with open("./configs/logging.yaml" , "r") as file:
        config_file = yaml
    

if __name__ == '__main__':
    main()
    