import boto3

def lambda_handler(event, context):
    print(f'Input: {event}')
    client = boto3.client('ssm')
    response = client.send_command(
        InstanceIds=[
            event.get('InstanceId'),
        ],
        DocumentName='GrowLinuxXfs',
        DocumentVersion='$DEFAULT',
        DocumentHash='be60146f389d7b6323427db49eea63ad66b767a2c2ba291552cc8b74d3bf823c',
        DocumentHashType='Sha256',
        TimeoutSeconds=30,
        Comment='Increase volume size because available space is low',
        Parameters={
            'DeviceName': [event['DeviceName']],
            'PartitionNum': [event['PartitionNum']],
            'MountPoint': [event['MountPoint']]
        }
    )
    return event 
