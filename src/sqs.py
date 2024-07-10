import boto3
import json

QUEUE_NAME = "MY-TEST-QUEUE"
FIFO_QUEUE_NAME = "MY-TEST-FIFO-QUEUE.fifo"
FIFO_QUEUE_URL = "https://sqs.eu-central-1.amazonaws.com/590183934493/MY-TEST-FIFO-QUEUE.fifo"
DEAD_LETTER_QUEUE_NAME = 'DEAD-letter-queue-for-main'
MAIN_QUEUE_NAME = 'MAIN-QUEUE'
MAIN_QUEUE_URL = "https://sqs.eu-central-1.amazonaws.com/590183934493/MAIN-QUEUE"


def sqs_client():
    sqs = boto3.client('sqs', region_name='eu-central-1')
    """:type : pyboto3.sqs"""
    return sqs


def create_sqs_queue():
    return sqs_client().create_queue(QueueName=QUEUE_NAME)


def create_fifo_sqs_queue():
    return sqs_client().create_queue(
        QueueName=FIFO_QUEUE_NAME,
        Attributes={
            'FifoQueue': 'true'
        }
    )


def create_queue_for_dead_letter():
    return sqs_client().create_queue(
        QueueName=DEAD_LETTER_QUEUE_NAME,
    )


def create_main_queue_for_dead_letter():
    redrive_policy = {
        "deadLetterTargetArn": "arn:aws:sqs:eu-central-1:590183934493:DEAD-letter-queue-for-main",
        "maxReceiveCount": 3,
    }
    return sqs_client().create_queue(
        QueueName=MAIN_QUEUE_NAME,
        Attributes={
            "DelaySeconds": "0",
            "MaximumMessageSize": "262144",
            "VisibilityTimeout": "30",
            "MessageRetentionPeriod": "345680",
            "ReceiveMessageWaitTimeSeconds": "0",
            "RedrivePolicy": json.dumps(redrive_policy)
        }
    )


def find_queue():
    return sqs_client().list_queues(QueueNamePrefix=QUEUE_NAME)


def list_queues():
    return sqs_client().list_queues()


def get_queue_attributes(queue_url):
    return sqs_client().get_queue_attributes(
        QueueUrl=queue_url,
        AttributeNames=['All']
    )


def update_queue_attributes(queue_url, attributes):
    return sqs_client().set_queue_attributes(
        QueueUrl=queue_url,
        Attributes=attributes
    )


def delete_queue_attributes(queue_url):
    return sqs_client().delete_queue(QueueUrl=queue_url)

if __name__ == '__main__':
    print(
        delete_queue_attributes(MAIN_QUEUE_URL)
    )
