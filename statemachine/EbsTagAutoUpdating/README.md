# EBS Tag Update

This state machine update EBS tags with EC2 tags  when EC2 instances starts.

## Testing

1. EBS tag updating 

    ```
    # curl <APIGateway Endpoint>/ebs_tag_update -X POST -d '{"input": "{\"detail-type\": \"EC2 Instance State-change Notification\", \"source\": \"aws.ec2\", \"detail\": {\"instance-id\": \"<Your EC2 Instance ID for test>\", \"state\": \"running\"}}","stateMachineArn": "<EC2 disk alarm auto-creating state machine ARN>"}'
    ```

    The environment variable of lambda "CreateEbsTagsFromEc2" defines which tags will bill polulated from EC2 to EBS, defaultly two tags "Name" and "Project" are included.
