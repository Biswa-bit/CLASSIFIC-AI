"""
==========================================================
CLASSIFIC-AI Project Constants
==========================================================

This file contains all project-wide constant values.

Instead of hardcoding values throughout the project,
every module should import values from this file.

Author : Biswadip Choudhury
Version: 1.0.0
==========================================================
"""

# ==========================================================
# Project Information
# ==========================================================

PROJECT_NAME = "CLASSIFIC-AI"

VERSION = "1.0.0"

AUTHOR = "Biswadip Choudhury"


# ==========================================================
# Machine Learning Defaults
# ==========================================================

DEFAULT_TEST_SIZE = 0.20

DEFAULT_RANDOM_STATE = 42

DEFAULT_CV = 5

DEFAULT_SCORING = "accuracy"


# ==========================================================
# Folder Names
# ==========================================================

DATASET_FOLDER = "datasets"

MODEL_FOLDER = "models"

LOG_FOLDER = "logs"

EXPERIMENT_FOLDER = "experiments"

DEPLOYMENT_FOLDER = "deployment"

REPORT_FOLDER = "reports"

MODEL_REGISTRY_FOLDER = "model_registry"

KNOWLEDGE_REPOSITORY_FOLDER = "knowledge_repository"


# ==========================================================
# Supported File Types
# ==========================================================

SUPPORTED_FILE_TYPES = [
    ".csv",
    ".xlsx",
    ".xls"
]


# ==========================================================
# Missing Value Threshold
# ==========================================================

MAX_MISSING_PERCENTAGE = 80


# ==========================================================
# Logging
# ==========================================================

LOG_LEVEL = "INFO"

LOG_FILE_PREFIX = "classific_ai"


# ==========================================================
# Random Seed
# ==========================================================

SEED = 42

