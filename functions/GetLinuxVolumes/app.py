import time
import boto3

def lambda_handler(event, context):
    print(f'Input: {event}')
    client = boto3.client('ssm')
    response = client.send_command(
        InstanceIds=[
            event.get('InstanceId'),
        ],
        DocumentName='ListLinuxDisks',
        DocumentVersion='$DEFAULT',
        DocumentHash='6e15838ece6609e01f463cef3668188038967af8747c12de7789e6a6cbdc4943',
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
            if line.startswith('/dev/'):
                event['Volumes'].append({
                    'device': line.split()[0].lstrip('/dev/'), 
                    'path': line.split()[5]
                })
        return event
    raise Exception('SSM Command failed') 
