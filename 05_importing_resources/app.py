#!/usr/bin/env python3
import aws_cdk as cdk
from stacks.importing_resources_stack import ImportingResourcesStack
from dotenv import load_dotenv
import os

load_dotenv()

aws_account = os.getenv('AWS_ACCOUNT', 'unknown')
aws_region = os.getenv('AWS_REGION', 'unknown')

app = cdk.App()
ImportingResourcesStack(app, "ImportingResourcesStack",
    env=cdk.Environment(account=aws_account, region=aws_region),
)

app.synth()
