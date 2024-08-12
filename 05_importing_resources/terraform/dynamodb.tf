resource "aws_dynamodb_table" "example" {
  name           = "${data.aws_caller_identity.current.account_id}-my-table"
  billing_mode   = "PAY_PER_REQUEST"
  hash_key       = "SessionId"

  attribute {
    name = "SessionId"
    type = "S"
  }
}
