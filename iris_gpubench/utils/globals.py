"""
Global configuration and constants for the iris-gpubench package.

This module defines global variables that are shared across the package, 
including directories, timeout settings, and logging configuration.

Attributes:
    RESULTS_DIR (str): Path to the directory where results will be stored.
    TIMEOUT_SECONDS (int): Default timeout duration in seconds for operations.
    LOGGER (logging.Logger): Configured logger instance for the package.
"""

import os
from .logging_utils import setup_logging

# Path to the directory where results will be stored
RESULTS_DIR = './iris-gpubench-results'
# Ensure the results directory exists
os.makedirs(RESULTS_DIR, exist_ok=True)

# Default timeout duration in seconds
TIMEOUT_SECONDS = 30

# Time in seconds between readings
MONITOR_INTERVAL = 5

# Initialize the logger with the specified configuration
LOGGER = setup_logging(RESULTS_DIR)

# Default Carbon Forecast Region
DEFAULT_REGION = "South England"
