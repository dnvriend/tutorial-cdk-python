import aws_cdk as cdk
from aws_cdk import Stack
from constructs import Construct

class DataSourcesStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Equivalent to data "aws_caller_identity" "current" {}
        account_id = cdk.Aws.ACCOUNT_ID

        # Equivalent to data "aws_region" "current" {}
        region = cdk.Aws.REGION

        # You can now use these variables in your stack
        cdk.CfnOutput(self, "AccountId", value=account_id)
        cdk.CfnOutput(self, "Region", value=region)
