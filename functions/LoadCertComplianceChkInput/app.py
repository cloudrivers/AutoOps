import json
import string
import datetime

def lambda_handler(event, context):
    print(f'Input: {json.dumps(event)}')
    resourceId = event.get('detail').get('resourceId')
    annotation = event.get('detail').get('newEvaluationResult').get('annotation')
    compliance_details = {
        'resourceId': resourceId,
        'annotation': annotation
    }
    return compliance_details
