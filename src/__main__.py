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
logger = logging.getLogger("main")

import yaml
from pathlib import Path

from __init__ import __version__
from utils._os import os_compatibility

current_file = Path(__file__).resolve()
keepr_path_default = current_file.parent


def get_keepr_path():
    global keepr_path_default
    return keepr_path_default


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


def logging_setup(args: argparse.Namespace) -> logging.Logger:
    """logging_setup Configure the logging system based on the passed arguments.

    This function initializes and adapts the behavior of the main logger based on the options and information provided.

    Arguments:
        args {argparse.Namespace} -- The parsed command line arguments.

    Returns:
        logging.Logger -- The configured logger instance.
    """
    
    if args.debug:
        logger.setLevel(logging.DEBUG)
    for handler in logger.handlers:
        if getattr(handler, "baseFilename", "").endswith("debug.log"):
            handler.addFilter(lambda record: record.levelno == logging.DEBUG)
    return logger


def check_compatibility(args: argparse.Namespace, parser: argparse.Namespace):
    checks = {
        "os": {
            "name": "OS", 
            "function": lambda: os_compatibility()
        }
    }
    
    skipped_checks = args.skip_check or []
    
    
    if "all" in skipped_checks:
        if skipped_checks and (len(skipped_checks) > 1 or skipped_checks[0] != "all"):
            parser.error("The 'all' argument must be the first and only choice after '--skip-check'.")
        return True

    for object, data in checks.items():
        if object not in skipped_checks:
            logger.debug(f"Running {data['name']} compatibility check...")
            data['function']()
        else:
            logger.warning(f"Skipping {data['name']} compatibility check.")        
    

def initialize():
    parser, args = argparse_setup()
    keepr_path_default = get_keepr_path()
    
    with open(f"{keepr_path_default}/configs/logging.yaml" , "r") as file:
        config_file = yaml.safe_load(file)
        dictConfig(config_file)
    logger = logging_setup(args)
    
    check_compatibility(args, parser)
    

def main():
    initialize()
    

if __name__ == '__main__':
    main()
    