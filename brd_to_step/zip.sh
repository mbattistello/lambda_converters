#!/bin/sh

# Creates a zip file that can be deployed as an AWS Lambda function

zip -r9 brd_to_step_lambda.zip \
aws_s3.py \
conversion_error.py \
handler.py \
step_to_stl.py \
brd_to_step.py \
lib \
OCC/*.py \
OCC/*.so
