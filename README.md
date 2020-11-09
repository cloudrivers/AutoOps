# AutoOps

This project contains useful operational processes represented as state machines with AWS StepFunctions. 

- ![EBS Auto Scale](EBSScaling/README.md)
- ![EC2 Alarm Create](EC2AlarmCreating/README.md)
- ![Distributin Tag Update](DistributionAutoTag/README.md)
- ![EBS Tag Update](EbsTagAutoUpdating/README.md)

## How to deploy

0. Pick up state machines and generate the CloudFormation template
    ```
    # git clone 
    # cd 
    # python3 ./gen_template.py statemachine/<state machine name>/ statemachine/<state machine name>/ ...
    ```

1. With SAM CLI installed
    ```
    # sam build
    # sam deploy --guided
    ```
2. Without SAM CLI, use CloudFormation template directly
    - Create a S3 bucket and prefix "AutoOps"
    - Upload the files in artifacts/ to s3://your-bucket-name/AutoOps. You need to replace "your-bucket-name" with your own S3 bucket name in following commands.
    ```
    # aws s3 sync ./artifacts s3://your-bucket-name/AutoOps
    ```
    - Modify the CloudFormation template packaged.yaml
        - Linux:
        ```
        # sed -i 's/<your S3 bucket>/your-bucket-name/g' packaged.yaml
        ```
        - MacOS:
        ```
        # sed -i '' 's/<your S3 bucket>/your-bucket-name/g' packaged.yaml
        ```
    - Run CloudFormation with packaged.yaml

## How to try

The state machines, who represent operational process, should be triggered by CloudWatch events. 

For testing or manually starting, a private API is also created so you can start execution of state machines by REST requests. If you want to do this, please create a VPC endpoint to Api Gateway service and modify the Resource Policy of the API to allow your VPC to invoke. 

**Please be noted that you should apply other security service such as IAM authorization to protect this API.**








