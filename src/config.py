#! /bin/python3

from os import getenv
from dataclasses import dataclass


"""
Configurations
"""


@dataclass
class Config:
    """All configs for queues and notifications"""

    TOPIC_NAME: str = getenv("TOPIC_NAME")
    TOPIC_ARN: str = getenv("TOPIC_ARN")
    QUEUE_NAME: str = getenv("QUEUE_NAME")
    FIFO_QUEUE_NAME: str = getenv("FIFO_QUEUE_NAME")
    FIFO_QUEUE_URL: str = getenv("FIFO_QUEUE_URL")
    DEAD_QUEUE_NAME: str = getenv("DEAD_QUEUE_NAME")
    MAIN_QUEUE_NAME: str = getenv("MAIN_QUEUE_NAME")
    MAIN_QUEUE_URL: str = getenv("MAIN_QUEUE_URL")
