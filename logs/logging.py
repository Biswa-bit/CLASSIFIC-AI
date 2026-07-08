"""
=======================================================
CLASSIFIC-AI Logging Module
=======================================================

This module creates a centralized logging system for
the entire CLASSIFIC-AI framework.

Every module should import this logger instead of
creating its own logger.

=======================================================
"""

import logging
import os
from datetime import datetime


# Create logs directory if it does not exist
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)


# Log filename with timestamp
LOG_FILE = os.path.join(
    LOG_DIR,
    f"classific_ai_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
)


# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE),
        logging.StreamHandler()
    ]
)


# Create logger object
logger = logging.getLogger("CLASSIFIC-AI")
