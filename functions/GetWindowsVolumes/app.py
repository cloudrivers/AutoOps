import time
import boto3

def lambda_handler(event, context):
    print(f'Input: {event}')
    client = boto3.client('ssm')
    response = client.send_command(
        InstanceIds=[
            event.get('InstanceId'),
        ],
        DocumentName='ListWindowsDisks',
        DocumentVersion='$DEFAULT',
        DocumentHash='55d0e2cfa241ee3a53629453c9e61d48373aca810eee7ff57d2aba301ea2b4e8',
        DocumentHashType='Sha256',
        TimeoutSeconds=30,
        Comment='Increase volume size because available space is low',
        Parameters={}
    )
    print(f'Response: {response}')
    commandId = response.get('Command').get('CommandId')
    time.sleep(10)
    invokation_status = 'InProgress'
    response = None
    while invokation_status == 'InProgress':
        response = client.get_command_invocation(
            CommandId=commandId,
            InstanceId=event.get('InstanceId')
        )
        print(f'Response: {response}')
        invokation_status = response.get('Status')
        time.sleep(10)
    if invokation_status == 'Success':
        output = response.get('StandardOutputContent')
        if len(output) == 24000:
            raise Exception('Too long output')
        event['Volumes'] = []
        for line in output.split('\n'):
            if line.split() and len(line.split()[2]) == 1:
                event['Volumes'].append(
                    {'instance': line.split()[2].upper()}
                )
        return event
    raise Exception('SSM Command failed') 
