output "bucket_name" {
  value = aws_s3_bucket.example.bucket
}

output "table_name" {
  value = aws_dynamodb_table.example.name
}

output "account_id" {
  value = data.aws_caller_identity.current.account_id
}
