# AutoOps

This project contains useful operational processes represented as a state machines with AWS StepFunctions. 

## How to deploy 
1. With SAM CLI installed
```
# sam build
# sam deploy --guided
```
2. Without SAM CLI, use CloudFormation template directly
    - Create a S3 bucket and prefix "AutoOps"
    - Upload the files in artifacts/ to s3://bucket-name/AutoOps. You need to replace "bucket-name" with your own S3 bucket name in following commands.
    ```
    # aws s3 sync ./artifacts s3://bucket-name/AutoOps
    ```
    - Modify the file packaged.yaml
        - Linux:
        ```
        # sed -i 's/<your S3 bucket>/bucket-name/g' packaged.yaml
        ```
        - MacOS:
        ```
        sed -i '' 's/<your S3 bucket>/bucket-name/g' packaged.yaml
        ```
    - Run CloudFormation with packaged.yaml