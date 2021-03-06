# ACM certificate expire notification

- State machine to check compliance of ACM certificates and it will send SNS notification when found a certificate is to expire.

    ![](../../doc/cert_compliance_check.asl.png)

## Prerequisites

The AWS Config rule to check compliance of ACM certificates should be deployed with CloudFormation. Please refer to [https://docs.aws.amazon.com/zh_cn/config/latest/developerguide/acm-certificate-expiration-check.html]

## Testing

1. ACM certificate expire notification

    ```
    # curl <APIGateway Endpoint>/cert-non-comliant -X POST -d '{"input": "{\"detail-type\": \"Config Rules Compliance Change\",\"source\": \"aws.config\",\"detail\": {\"resourceId\": \"arn:aws:acm:us-east-1:597377428377:certificate/4b67b0d4-5d0d-413d-8cde-da03be81726f\",\"newEvaluationResult\": {\"complianceType\": \"NON_COMPLIANT\",\"annotation\": \"Certificate will expire on 2021-08-31T12:00:00.000Z\"},\"resourceType\": \"AWS::ACM::Certificate\"}}","stateMachineArn":"arn:aws:states:us-east-1:597377428377:stateMachine:CertComplianceChk-spKuV2PclAL3"}'
    ```