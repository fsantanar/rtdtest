#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Author: Felipe Santana Rojas
# Date: 2023-06-07
# Filename: utilities.py
# License: MIT License
import heapq
import logging
import logging.handlers
import os
import platform
import re
import subprocess
import time
import urllib.request

import numpy as np
import yaml
from tqdm import tqdm

def load_configuration(config_file, config_mode):
    """
    Load configuration from a YAML file based on the specified mode.

    Args:
        config_file (str): The path to the configuration file.
        config_mode (str): The mode to select from the configuration file.

    Returns:
        dict or None: The configuration dictionary for the given mode, or None if an error occurs.
    """
    try:
        with open(config_file, 'r') as f:
            config_dict = yaml.safe_load(f)[config_mode]
        return config_dict
    except KeyError:
        print(f"Error: '{config_mode}' key not found in the configuration file '{config_file}'.")
    except FileNotFoundError:
        print(f"Error: Configuration file '{config_file}' not found.")
    except IsADirectoryError:
        print(f"Error: '{config_file}' is a directory, not a file.")
    except PermissionError:
        print(f"Error: Permission denied while accessing the configuration file '{config_file}'.")
    except Exception as e:
        print(f"Error: An unexpected error occurred while loading the configuration file: {e}")

    return None

def run_command(command):
    """
    Run a command in the shell and capture the output.

    Args:
        command (str): The command to run.

    Returns:
        CompletedProcess: The result of running the command.
    """
    return subprocess.run(command, shell=True, capture_output=True, text=True)


def print_message(message, new_line=True):
    """ Print a message in green color."""
    if new_line:
        print(bcolors.OKGREEN + message + bcolors.ENDC)
    else:
        print(bcolors.OKGREEN + message + bcolors.ENDC, end='')

