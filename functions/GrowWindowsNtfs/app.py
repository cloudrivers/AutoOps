import boto3

def lambda_handler(event, context):
    print(f'Input: {event}')
    client = boto3.client('ssm')
    response = client.send_command(
        InstanceIds=[
            event.get('InstanceId'),
        ],
        DocumentName='GrowWindowsNtfs',
        DocumentVersion='$DEFAULT',
        DocumentHash='4686f975b3b3dfdf2ce0ce3f93b3b73ec5a72cad66fc2c0217521b24f71cc6c3',
        DocumentHashType='Sha256',
        TimeoutSeconds=30,
        Comment='Increase volume size because available space is low',
        Parameters={
            'DriveLetter': [event['DriveLetter']]
        }
    )
    return event 
