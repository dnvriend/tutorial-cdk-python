import aws_cdk as cdk
from aws_cdk import Stack
from constructs import Construct
from aws_cdk import RemovalPolicy, aws_s3 as s3
from aws_cdk import aws_dynamodb as dynamodb

class ImportingResourcesStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        stack_context = cdk.Stack.of(self)

        s3.Bucket(self, 
            id="example_bucket_id",
            bucket_name=f"{stack_context.account}-my-bucket",
            # block_public_access=s3.BlockPublicAccess.BLOCK_ALL,
            # encryption=s3.BucketEncryption.S3_MANAGED,                        
            removal_policy=RemovalPolicy.RETAIN,
        )

        dynamodb.Table(self, 
            id="example_table_id",
            table_name=f"{stack_context.account}-my-table",
            partition_key=dynamodb.Attribute(name="id", type=dynamodb.AttributeType.STRING),
            billing_mode=dynamodb.BillingMode.PAY_PER_REQUEST,
            removal_policy=RemovalPolicy.RETAIN,
        )
