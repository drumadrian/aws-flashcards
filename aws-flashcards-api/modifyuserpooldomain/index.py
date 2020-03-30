from __future__ import print_function
from crhelper import CfnResource
import logging
import json
import boto3

logger = logging.getLogger(__name__)
helper = CfnResource(json_logging=False, log_level='DEBUG', boto_level='CRITICAL')
# https://pypi.org/project/crhelper/

try:
    client = boto3.client('cognito-idp')
    pass
except Exception as e:
    helper.init_failure(e)

def lambda_handler(event, context):
    print(json.dumps(event))
    helper(event, context)

@helper.create
def create(event, context):
    user_pool_id = event['ResourceProperties']['UserPoolId']
    domain = event['ResourceProperties']['Domain']
    client.create_user_pool_domain(
        UserPoolId=user_pool_id,
        Domain=domain,
    )

@helper.update
def update(event, context):
    user_pool_id = event['ResourceProperties']['UserPoolId']
    domain = event['ResourceProperties']['Domain']
    old_user_pool_id = event['OldResourceProperties']['UserPoolId']
    old_domain = event['OldResourceProperties']['Domain']
    client.delete_user_pool_domain(
        UserPoolId=old_user_pool_id,
        Domain=old_domain,
    )
    client.create_user_pool_domain(
        UserPoolId=user_pool_id,
        Domain=domain,
    )

@helper.delete
def delete(event, context):
    user_pool_id = event['ResourceProperties']['UserPoolId']
    domain = event['ResourceProperties']['Domain']
    client.delete_user_pool_domain(
        UserPoolId=user_pool_id,
        Domain=domain,
    )
