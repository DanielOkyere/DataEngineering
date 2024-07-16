import boto3


TOPIC_NAME = "awesome-sns"
TOPIC_ARN = "arn:aws:sns:eu-central-1:590183934493:awesome-sns"


def sns_client():
    sns = boto3.client("sns", region_name="eu-central-1")
    """ :type : pyboto3.sns"""
    return sns


def create_topic(topic_name):
    return sns_client().create_topic(Name=topic_name)


def get_topics():
    return sns_client().list_topics()


def get_topic_attributes(arn_string):
    return sns_client().get_topic_attributes(TopicArn=arn_string)


def update_topic_attributes(arn_string, name):
    return sns_client().set_topic_attributes(
        TopicArn=arn_string,
        AttributeName="DisplayName",
        AttributeValue=f"{name}-updated",
    )


def delete_topic(arn_string):
    return sns_client().delete_topic(TopicArn=arn_string)


def create_email_subscription(topic_arn, email_address):
    return sns_client().subscribe(
        TopicArn=topic_arn,
        Protocol="email",
        Endpoint=email_address,
    )


def create_sms_subscription(topic_arn, phone_number):
    return sns_client().subscribe(
        TopicArn=topic_arn,
        Protocol="sms",
        Endpoint=f"+2330{phone_number}",
    )


def create_sqs_queue_subscription(topic_arn, sqs_queue_arn):
    return sns_client().subscribe(
        TopicArn=topic_arn,
        Protocol="sqs",
        Endpoint=sqs_queue_arn,
    )


def get_topic_subscriptions(topic_arn):
    return sns_client().list_subscriptions_by_topic(TopicArn=topic_arn)


if __name__ == "__main__":
    create_topic(TOPIC_NAME)
    # print(get_topics())
    # print(get_topic_attributes(TOPIC_ARN))
    # print(update_topic_attributes(TOPIC_ARN, TOPIC_NAME))
    # delete_topic(TOPIC_ARN)
    # create_email_subscription(TOPIC_ARN, 'daniel.kwame.okyere101@gmail.com')
    # create_sms_subscription(TOPIC_ARN, '549502748')
    # create_sqs_queue_subscription(
    #     TOPIC_ARN, "arn:aws:sqs:eu-central-1:590183934493:awesome_sqs"
    # )
    print(get_topic_subscriptions(TOPIC_ARN))
