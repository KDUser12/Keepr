# (c) 2025 YourLabXYZ.
# Licensed under MIT License.

import os
import subprocess
import sys

import logging
logger = logging.getLogger("main")


def install_requirements(file_path="requirements.txt", enable_logging=False):
    """
    Installs all packages listed in a requirements.txt file.

    :param file_path: Path to the requirements.txt file (default is "requirements.txt").
    :param enable_logging: Enable logging (default is False).
    """

    file_path = os.path.abspath(file_path)

    # Check if the file exists and is valid
    if not os.path.isfile(file_path):
        message = f"The {file_path} file was not found."
        logger.error(message) if enable_logging else print(message)
        raise FileNotFoundError(message)

    try:
        # Run the pip install -r requirements.txt command
        result = subprocess.run(
            [sys.executable, "-m", "pip", "install", "-r", file_path],
            check=True,  # Raises CalledProcessError if the command fails
            capture_output=True,  # Captures stdout and stderr for debugging/logging
            text=True  # Decodes stdout/stderr as text
        )

        success_message = "Successfully installed dependencies."
        logger.info(success_message) if enable_logging else print(success_message)

        # Optionally log the output for debugging
        if enable_logging:
            logger.debug("Command output:\n%s", result.stdout)

    except subprocess.CalledProcessError as error:
        # Handle installation errors
        error_message = (f"An error occurred while installing dependencies: "
                         f"{error.stderr or 'Unknown error'}")
        logger.error(error_message) if enable_logging else print(error_message)
        raise EnvironmentError(error_message) from error

# Example usage (disabled to prevent immediate execution)
# install_requirements("requirements.txt")


def install_modules(module, enable_logging=False):
    """
    Installs a specific version of a Python module using subprocess.

    :param module: The name of the module to install.
    :param enable_logging: Enable logging (default is False).
    """


    try:
        # Run the pip install {module} command
        result = subprocess.run(
            [sys.executable, "-m", "pip", "install", module],
            check=True,  # Raises CalledProcessError if the command fails
            capture_output=True,  # Captures stdout and stderr for debugging/logging
            text=True  # Decodes stdout/stderr as text
        )

        success_message = "Successfully installed module."
        logger.info(success_message) if enable_logging else print(success_message)

        # Optionally log the output for debugging
        if enable_logging:
            logger.debug("Command output:\n%s", result.stdout)

        return True

    except subprocess.CalledProcessError as error:
        # Handle installation errors
        error_message = (f"An error occurred while installing module: "
                         f"{error.stderr or 'Unknown error'}")
        logger.error(error_message) if enable_logging else print(error_message)
        raise EnvironmentError(error_message) from error

# Example usage (disabled to prevent immediate execution)
# install_module("pypixz")
