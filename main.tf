provider "aws" {
  region     = "us-east-1"
  access_key = "HARDCODED_ACCESS_KEY"
  secret_key = "HARDCODED_SECRET_KEY"
}

resource "aws_s3_bucket" "bad_bucket" {
  bucket = "my-public-bucket"
  acl    = "public-read"
}
