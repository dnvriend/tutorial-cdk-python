#!/usr/bin/env python3
import aws_cdk as cdk
from stacks.existing_resources_stack import ExistingResourcesStack
from dotenv import load_dotenv
import os

load_dotenv()

aws_account = os.getenv('AWS_ACCOUNT', 'unknown')
aws_region = os.getenv('AWS_REGION', 'unknown')

app = cdk.App()
ExistingResourcesStack(app, "ExistingResourcesStack",
   env=cdk.Environment(account=aws_account, region=aws_region),
)

app.synth()
