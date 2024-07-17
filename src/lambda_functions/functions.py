import os


def handler(event, context):
    # return {"statusCode": 200, "message": "Hello From python lambda function"}

    env_var = (os.getenv('ENV_VAR_TEST'))
    return {"statusCode": 200, "message": env_var}
