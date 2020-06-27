# AutoOps

This project contains useful operational processes represented as state machines with AWS StepFunctions. Currently, it is used for auto creating EBS usage alarm for EC2 instances and auto scaling EBS and file system on it.

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
    - Modify the CloudFormation template packaged.yaml
        - Linux:
        ```
        # sed -i 's/<your S3 bucket>/bucket-name/g' packaged.yaml
        ```
        - MacOS:
        ```
        # sed -i '' 's/<your S3 bucket>/bucket-name/g' packaged.yaml
        ```
    - Run CloudFormation with packaged.yaml, the outputs of CloudFormation includes:
    1. EC2 disk alarm auto-creating state machine ARN
    2. EBS auto-scaling state machine ARN
    3. APIGateway Endpoint to start start machines' execution

## Test by API invokation

0. Prerequisites

    For monitor the disk usage, you need to install and config CloudWatch agent in your EC2 instances.

1. EC2 disk arlam auto-creating
    ```
    # curl <APIGateway Endpoint>/ec2_alarm_create -X POST -d '{"input": "{\"detail-type\": \"EC2 Instance State-change Notification\", \"source\": \"aws.ec2\", \"detail\": {\"instance-id\": \"<Your EC2 Instance ID for test>\", \"state\": \"running\"}}","stateMachineArn": "<EC2 disk alarm auto-creating state machine ARN>"}'
    ```

    For Linux instance, CloudWatch event rules will be created for each ebs attached to this instance. The alarm threshold is 80% be default. If you want to change the threshold, please update Environment of Lambda function CreateLinuxDiskAlarms.

    For Windows instance, CloudWatch event rules will be created for each ebs attached to this instance. The alarm threshold is 20% be default. If you want to change the threshold, please update Environment of Lambda function CreateWindowsDiskAlarms.

2. EBS auto-scaling on Linux

    ```
    # curl <APIGateway Endpoint>/ebs_scale -X POST -d '{"input": "{\"detail-type\": \"CloudWatch Alarm State Change\",\"source\": \"aws.cloudwatch\",\"detail\": {\"alarmName\": \"DiskSpace\",\"state\": {\"value\": \"ALARM\"},\"configuration\": {\"metrics\": [{\"metricStat\": {\"metric\": {\"namespace\": \"CWAgent\",\"name\": \"disk_used_percent\",\"dimensions\": {\"path\": \"<The mount point of device>\",\"InstanceId\": \"<Your EC2 Instance ID for test>\",\"device\": \"<The device name in OS>\",\"fstype\": \"xfs\"}}}}]}}}","stateMachineArn": "<EBS auto-scaling state machine ARN>"}'
    ```

3. EBS auto-scaling on Windows

    ```
    curl https://z552xr3101.execute-api.us-east-1.amazonaws.com/Prod/ebs_scale -X POST -d '{"input": "{\"detail-type\": \"CloudWatch Alarm State Change\",\"source\": \"aws.cloudwatch\",\"detail\": {\"alarmName\": \"DiskSpace\",\"state\": {\"value\": \"ALARM\"},\"configuration\": {\"metrics\": [{\"metricStat\": {\"metric\": {\"namespace\": \"CWAgent\",\"name\": \"LogicalDisk % Free Space\",\"dimensions\": {\"instance\": \"<The Drive Letter>:\",\"InstanceId\": \"<Your EC2 Instance ID for test>\"}}}}]}}}","stateMachineArn": "<EBS auto-scaling state machine ARN>"}'
    ```

