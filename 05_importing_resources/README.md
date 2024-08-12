# importing resources aka. state management

CDK does not have state management like Terraform for example. In Terraform state can be managed in full detail and you can write your own tools around it if you need fine grained control. For CDK - which is ClouddFormation (CFN) under the hood - there is no such thing. State is managed by the CFN service, and the only way to interact with it is using the CDK and defining resources and resource properties.

## Import a resource manually (into state)

The workflow is:

- create the cdk resource in your stack, make sure to define the `removal_policy=RemovalPolicy.RETAIN`, which is a good thing to do for resources that you want to keep around (eg. if you want to remove it from state)
- check the diff with `cdk diff` and make sure there are no pending changes
- Run the `cdk import`
- The resource is now imported into CFN state.

## Remove a resource manually (from state)

- comment out the resource in your stack. Make sure you have configured the `removal_policy=RemovalPolicy.RETAIN` because that way the resource will be kept in state.
- run `cdk diff` and make sure there are no pending changes, CDK should mark the resource as 'orphan'.
- run `cdk deploy` to change the state.
  
As a performance indication, orphan a single bucket takes ~30 seconds.

## Import multiple resources into state 

When we want to import multiple resources into state, we need to use the `cdk import -r --record-resource-mappings` flag, that will generate a mapping of existing physical resources to CDK resources to be imported as Not that no actual import operation will be performed. This is only for generating the mapping file.

Afterwards the `-m, --resource-mapping` can be used to import the resources into state.

The resulting resource-mapping.json file should long like this (which is different than the documentation) and use CloudFormation Logical IDs instead of CDK identifiers:

You can see the IDS with `cdk synth`:

```json
{
  "examplebucketid1B46CD85": {
    "BucketName": "12345-my-bucket"
  },
  "exampletableid08FD40D3": {
    "TableName": "12345-my-table"
  }
}
```

The documentation states something like this, BUT THAT DOES NOT WORK, as these are CDK identifiers and not CFN identifiers.

```json
{
  "ImportingResourcesStack/example_bucket_id/Resource": {
    "BucketName": "12345-my-bucket"
  },
  "ImportingResourcesStack/example_table_id/Resource": {
    "TableName": "12345-my-table"
  }
}
```

It will use these identifiers though to point to the CDK resource. This is conceptually different as in Terraform you will use the Terraform paths to import.

---
