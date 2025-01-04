"""
Module for configuring and providing the application logger.
"""

import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("p2p_utility")

