import boto3


def sns_client():
    sns = boto3.client("sns", region_name="eu-central-1")
    """:type sns: boto3.client"""
    return sns


def create_topic(topic_name: str):
    return sns_client().create_topic(Name=topic_name)


if __name__ == "__main__":
    create_topic("Awesome test topic")
