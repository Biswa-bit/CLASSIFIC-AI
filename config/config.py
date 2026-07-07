"""
====================================================
CLASSIFIC-AI Configuration File
====================================================
Central configuration settings for the entire project.
Every module should import values from this file instead
of hardcoding them.
====================================================
"""

# --------------------------------------------------
# Project Information
# --------------------------------------------------

PROJECT_NAME = "CLASSIFIC-AI"
VERSION = "1.0.0"
AUTHOR = "Biswadip Choudhury"

# --------------------------------------------------
# Machine Learning Settings
# --------------------------------------------------

RANDOM_STATE = 42
TEST_SIZE = 0.20

# --------------------------------------------------
# Folder Locations
# --------------------------------------------------

DATASET_FOLDER = "datasets"
MODEL_FOLDER = "models"
REPORT_FOLDER = "reports"
LOG_FOLDER = "logs"

# --------------------------------------------------
# Streamlit Settings
# --------------------------------------------------

APP_TITLE = "CLASSIFIC-AI"
