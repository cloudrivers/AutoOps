import os
import json
import boto3

def lambda_handler(event, context):
    print(f'Input: {event}')
    client = ec2 = boto3.client('cloudwatch')
    for volume in event['Volumes']:   
        response = client.put_metric_alarm(
            AlarmName=f'DiskSpace-{event["InstanceId"]}-{volume["path"]}',
            ActionsEnabled=False,
            MetricName='disk_used_percent',
            Namespace='CWAgent',
            Statistic='Average',
            Dimensions=[{
                'Name': 'InstanceId',
                'Value': event['InstanceId']
            },{
                'Name': 'path',
                'Value': volume['path']
            },{
                'Name': 'ImageId',
                'Value': event['ImageId']
            },{
                'Name': 'InstanceType',
                'Value': event['InstanceType']
            },{
                'Name': 'device',
                'Value': volume['device']
            },{
                'Name': 'fstype',
                'Value': 'xfs'
            }],
            Period=60,
            EvaluationPeriods=1,
            DatapointsToAlarm=1,
            Threshold=int(os.getenv('USAGE_THRESHOLD', '80')),
            ComparisonOperator='GreaterThanOrEqualToThreshold',
            TreatMissingData='missing',
            Tags=[]
        )
    print(f'Response: {response}')
    return event
