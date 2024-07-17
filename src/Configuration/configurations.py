#! /bin/python3

from os import getenv
from dataclasses import dataclass


"""
Configurations
"""


@dataclass
class Configurations:
    """All configs for queues and notifications"""

    TOPIC_NAME: str = getenv("TOPIC_NAME")
    TOPIC_ARN: str = getenv("TOPIC_ARN")
    QUEUE_NAME: str = getenv("QUEUE_NAME")
    FIFO_QUEUE_NAME: str = getenv("FIFO_QUEUE_NAME")
    FIFO_QUEUE_URL: str = getenv("FIFO_QUEUE_URL")
    DEAD_QUEUE_NAME: str = getenv("DEAD_QUEUE_NAME")
    MAIN_QUEUE_NAME: str = getenv("MAIN_QUEUE_NAME")
    MAIN_QUEUE_URL: str = getenv("MAIN_QUEUE_URL")

    LAMBDA_ROLE = "Lambda_Execution_Role"
    LAMBDA_ACCESS_POLICY_ARN = "arn:aws:iam::590183934493:policy/lambdaS3AccessPolicy"
    LAMBDA_ROLE_ARN = "arn:aws:iam::590183934493:role/Lambda_Execution_Role"
    LAMBDA_TIMEOUT = 10
    LAMBDA_MEMORY = 128
    LAMBDA_HANDLER = 'lambda_function.handler'

    PYTHON_36_RUNTIME = "python3.6"
    PYTHON_LAMBDA_NAME = 'PythonLambdaFunction'

