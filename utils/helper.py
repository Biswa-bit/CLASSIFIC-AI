"""
====================================================
CLASSIFIC-AI Helper Functions
====================================================
Common helper functions used across the project.
====================================================
"""

import os
from datetime import datetime


def create_folder(folder_path):
    """
    Create a folder if it does not already exist.
    """
    os.makedirs(folder_path, exist_ok=True)


def current_timestamp():
    """
    Return current date and time.
    """
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def print_banner(title):
    """
    Display a formatted banner.
    """
    print("=" * 60)
    print(title)
    print("=" * 60)
    