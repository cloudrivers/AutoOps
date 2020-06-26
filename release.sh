#!/bin/bash
name=$(basename $(pwd))
rm -rf .aws-sam/build
sam build
aws s3 rm --recursive s3://$1/${name}
sam package --s3-bucket $1 --s3-prefix ${name} --output-template-file packaged.yaml
rm -rf ./artifacts/
aws s3 sync s3://$1/${name}/ ./artifacts/
sed -i '' "s/$1/<your S3 bucket>/g" packaged.yaml
