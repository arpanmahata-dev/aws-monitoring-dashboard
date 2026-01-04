terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = "ap-south-1"
}

# S3 Bucket for metrics storage
resource "aws_s3_bucket" "metrics_bucket" {
  bucket = "aws-monitoring-metrics-${random_id.bucket_suffix.hex}"

  tags = {
    Name = "Monitoring Metrics Bucket"
  }
}

resource "random_id" "bucket_suffix" {
  byte_length = 4
}

# IAM Role for Lambda
resource "aws_iam_role" "lambda_role" {
  name = "monitoring_lambda_role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Action = "sts:AssumeRole"
      Effect = "Allow"
      Principal = {
        Service = "lambda.amazonaws.com"
      }
    }]
  })
}

# IAM Policy for Lambda
resource "aws_iam_role_policy" "lambda_policy" {
  name = "monitoring_lambda_policy"
  role = aws_iam_role.lambda_role.id

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect = "Allow"
        Action = [
          "ec2:DescribeInstances",
          "s3:ListAllMyBuckets",
          "s3:PutObject",
          "cloudwatch:GetMetricStatistics",
          "logs:CreateLogGroup",
          "logs:CreateLogStream",
          "logs:PutLogEvents"
        ]
        Resource = "*"
      }
    ]
  })
}

# Lambda Function
resource "aws_lambda_function" "metrics_collector" {
  filename         = "lambda_function.zip"
  function_name    = "metrics_collector"
  role            = aws_iam_role.lambda_role.arn
  handler         = "collector.lambda_handler"
  runtime         = "python3.11"
  timeout         = 60

  environment {
    variables = {
      BUCKET_NAME = aws_s3_bucket.metrics_bucket.id
    }
  }
}

# EventBridge Rule (runs every 15 minutes)
resource "aws_cloudwatch_event_rule" "metrics_schedule" {
  name                = "metrics_collection_schedule"
  description         = "Trigger metrics collection every 15 minutes"
  schedule_expression = "rate(15 minutes)"
}

resource "aws_cloudwatch_event_target" "lambda_target" {
  rule      = aws_cloudwatch_event_rule.metrics_schedule.name
  target_id = "metrics_collector"
  arn       = aws_lambda_function.metrics_collector.arn
}

resource "aws_lambda_permission" "allow_eventbridge" {
  statement_id  = "AllowExecutionFromEventBridge"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.metrics_collector.function_name
  principal     = "events.amazonaws.com"
  source_arn    = aws_cloudwatch_event_rule.metrics_schedule.arn
}

# Outputs
output "bucket_name" {
  value = aws_s3_bucket.metrics_bucket.id
}

output "lambda_function_name" {
  value = aws_lambda_function.metrics_collector.function_name
}