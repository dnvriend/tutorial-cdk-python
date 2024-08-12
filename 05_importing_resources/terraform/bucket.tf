resource "aws_s3_bucket" "example" {
  bucket = "${data.aws_caller_identity.current.account_id}-my-bucket"
}

resource "aws_s3_bucket_ownership_controls" "example" {
  bucket = aws_s3_bucket.example.id
  rule {
    object_ownership = "BucketOwnerPreferred"
  }
}

resource "aws_s3_bucket_acl" "example" {
  bucket = aws_s3_bucket.example.id
  acl    = "private"

  depends_on = [aws_s3_bucket_ownership_controls.example]
}
