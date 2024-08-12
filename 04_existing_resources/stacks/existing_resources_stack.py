import aws_cdk as cdk
from aws_cdk import Stack
from constructs import Construct
from aws_cdk import aws_ec2 as ec2

class ExistingResourcesStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here
        # Equivalent to data "aws_vpc" "vpc" { id = local.vpc_id }
        vpc: ec2.Vpc = ec2.Vpc.from_lookup(self, "VPC", vpc_id="vpc-3b95065c")

        # Equivalent to data "aws_subnet" "subnet_private_*" blocks
        # to make this work, see: https://dev.to/ellismichael/aws-using-existing-subnets-with-availability-zones-in-cdk-with-typescript-e7h
        subnet_private_1a = ec2.Subnet.from_subnet_id(self, "SubnetPublic1a", subnet_id="subnet-ac8667e5")

        print(subnet_private_1a.availability_zone)

        # cdk.CfnOutput(self, "VpcId", value=vpc.vpc_id)
        # # cdk.CfnOutput(self, "VpcCidrBlock", value=vpc.vpc_cidr_block)
        # cdk.CfnOutput(self, "SubnetPrivate1aId", value=subnet_private_1a.subnet_id)
        # cdk.CfnOutput(self, "SubnetPrivate1aCidrBlock", value=subnet_private_1a.ipv4_cidr_block)
