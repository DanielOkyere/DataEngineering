from src.lambda_functions import policies, functions
from src.Configuration import configurations
from sys import path

if __name__ == "__main__":
    """Main function to start application"""
    paths = "../src"
    path.append(paths)
    config = configurations.Configurations()
    # policy = policies.deploy_lambda_function(
    #     config.PYTHON_LAMBDA_NAME,
    #     config.PYTHON_36_RUNTIME,
    #     config.LAMBDA_HANDLER,
    #     config.LAMBDA_ROLE_ARN,
    #     ".",
    # )
    policy = policies.invoke_lambda_function(config.PYTHON_LAMBDA_NAME)
    print(policy['Payload'].read().decode())
