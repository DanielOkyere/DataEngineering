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


def create_sqs_queue(queue_name):
    return sqs_client().create_queue(QueueName=queue_name)


def create_fifo_sqs_queue(queue_name):
    return sqs_client().create_queue(
        QueueName=queue_name,
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


def send_message_to_queue(queue_url, msg_attributes, msg_body):
    return sqs_client().send_message(
        QueueUrl=queue_url,
        MessageAttributes=msg_attributes,
        MessageBody=msg_body
    )


def send_batch_messages_to_queue(queue_url):
    return sqs_client().send_message_batch(
        QueueUrl=queue_url,
        Entries=[
            {
                'Id': 'FirstMessage',
                'MessageBody': 'This is a 1st message of batch'
            },
            {
                'Id': 'SecondMessage',
                'MessageBody': 'This is a 2nd message of batch'
            },
            {
                'Id': 'ThirdMessage',
                'MessageBody': 'This is a 3rd message of batch'
            },
            {
                'Id': 'FourthMessage',
                'MessageBody': 'This is a 4th message of batch'
            }
        ]
    )

def poll_queue_for_message():
    return sqs_client().receive_message(
        QueueUrl="https://sqs.eu-central-1.amazonaws.com/590183934493/awesome_sqs",
        MaxNumberOfMessages=10,
    )

if __name__ == '__main__':
    # send_batch_messages_to_queue("https://sqs.eu-central-1.amazonaws.com/590183934493/awesome_sqs")
    print(poll_queue_for_message())