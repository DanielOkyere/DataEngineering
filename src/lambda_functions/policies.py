import json

import boto3
from src.Configuration import configurations
from os import path
from src.Utilities import utils

config = configurations.Configurations()


def lambda_client():
    aws_lambda = boto3.client("lambda", region_name="eu-central-1")
    """ :type : pyboto3.lambda """
    return aws_lambda


def iam_client():
    iam = boto3.client("iam")
    """:type : pyboto3.iam """
    return iam


def create_access_policy_for_lambda():
    s3_access_policy = {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Action": [
                    "s3:*",
                    "logs:CreateLogGroup",
                    "logs:CreateLogStream",
                    "logs:PutLogEvents",
                ],
                "Effect": "Allow",
                "Resource": "*",
            }
        ],
    }

    return iam_client().create_policy(
        PolicyName="lambdaS3AccessPolicy",
        PolicyDocument=json.dumps(s3_access_policy),
        Description="Allows lambda function to access s3 resources",
    )


def create_execution_role_for_lambda():
    lambda_execution_assumption_role = {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Principal": {"Service": "lambda.amazonaws.com"},
                "Action": "sts:AssumeRole",
            }
        ],
    }

    return iam_client().create_role(
        RoleName=f"{config.LAMBDA_ROLE}",
        AssumeRolePolicyDocument=json.dumps(lambda_execution_assumption_role),
        Description="Gives necessary permissions for lambda to be executed",
    )


def attach_access_policy_to_role():
    return iam_client().attach_role_policy(
        RoleName=config.LAMBDA_ROLE, PolicyArn=config.LAMBDA_ACCESS_POLICY_ARN
    )


def deploy_lambda_function(function_name, runtime, handler, role_arn, source_folder):
    Utils = utils.Utils()
    folder_path = path.join(path.dirname(path.abspath(__file__)), source_folder)
    print(folder_path)
    zip_file = Utils.make_zip_file_bytes(path=folder_path)

    return lambda_client().create_function(
        FunctionName=function_name,
        Runtime=runtime,
        Role=role_arn,
        Handler=handler,
        Code={
            "ZipFile": zip_file,
        },
        Timeout=config.LAMBDA_TIMEOUT,
        MemorySize=config.LAMBDA_MEMORY,
        Publish=False,
    )


def invoke_lambda_function(function_name):
    return lambda_client().invoke(FunctionName=function_name)