# CDK Bootstrapping
Welcome to the first chapter of the CDK tutorial. There is no way around it so lets dive right in, by saying that YOU WILL HAVE TO BOOTSTRAP ANY CDK ENVIRONMENT by using the `cdk bootstrap` command. This is because every environment is independent. So lets say you have an aws account '12345' in us-east-1, then you'll have to bootstrap it once. Then other stacks can make use of these resources. If you run `cdk bootstrap` again then they'll say `Environment aws://12345/us-east-1 bootstrapped (no changes).` 

**TL;DR**
You will HAVE TO bootstrap EVERY CDK environment, there is no way around it. Either live with it, or use another tool.

## What is bootstrapping?
Now that we have that out of the way, what is bootstrapping actually? Well, bootstrapping prepares your AWS environment by provisioning specific AWS resources in your environment that are used by the AWS CDK. These resources are commonly referred to as your bootstrap resources. They include the following:

- Amazon Simple Storage Service (Amazon S3) bucket – Used to store your CDK project files, such as AWS Lambda function code and assets.
- Amazon Elastic Container Registry (Amazon ECR) repository – Used primarily to store Docker images.
- AWS Identity and Access Management (IAM) roles – Configured to grant permissions needed by the AWS CDK to perform deployments. For more information about the IAM roles created during bootstrapping,

## IAM roles created during bootstrapping
By default, bootstrapping provisions the following AWS Identity and Access Management (IAM) roles in your environment:

- CloudFormationExecutionRole: This IAM role is a CloudFormation service role that grants CloudFormation permission to perform stack deployments on your behalf. This role gives CloudFormation permission to perform AWS API calls in your account, including deploying stacks.

By using a service role, the permissions provisioned for the service role determine what actions can be performed on your CloudFormation resources. Without this service role, the security credentials you provide with the CDK CLI would determine what CloudFormation is allowed to do.

- DeploymentActionRole: This IAM role grants permission to perform deployments into your environment. It is assumed by the CDK CLI during deployments. By using a role for deployments, you can perform cross-account deployments since the role can be assumed by AWS identities in a different account.

- FilePublishingRole: This IAM role grants permission to perform actions against the bootstrapped Amazon Simple Storage Service (Amazon S3) bucket, including uploading and deleting assets. It is assumed by the CDK CLI during deployments.

- ImagePublishingRole: This IAM role grants permission to perform actions against the bootstrapped Amazon Elastic Container Registry (Amazon ECR) repository. It is assumed by the CDK CLI during deployments.

- LookupRole: This IAM role grants readOnly permission to look up context values from the AWS environment. It is assumed by the CDK CLI when performing tasks such as template synthesis and deployments.

## Resource IDs created during bootstrapping
When you deploy the default bootstrap template, physical IDs for bootstrap resources are created using the following structure: cdk-qualifier-description-account-ID-Region.

- Qualifier – A nine character unique string value of hnb659fds. The actual value has no significance.
- Description – A short description of the resource. For example, container-assets.
- Account ID – The AWS account ID of the environment.
- Region – The AWS Region of the environment.

The following is an example physical ID of the Amazon S3 staging bucket created during bootstrapping: cdk-hnb659fds-assets-012345678910-us-west-1.

## Cleaning up

```shell
cdk destroy
aws s3 rm --recursive s3://$(aws s3 ls | grep cdktoolkit | cut -d' ' -f3) # empty the cdktoolkit staging bucket
aws cloudformation delete-stack --stack-name CDKToolkit
```

## Resources

- https://github.com/aws/aws-cdk-rfcs/issues/64
- https://github.com/aws/aws-cdk/issues/986
- 