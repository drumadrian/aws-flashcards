from __future__ import print_function
import logging
import os

allowed_domains = os.environ.get('ALLOWED_DOMAINS')
logger = logging.getLogger(__name__)

def lambda_handler(event, context):
    email = event['request']['userAttributes']['email']
    domain = email.split('@')[1]
    if allowed_domains == '*':
        pass
    elif domain in allowed_domains.split(','):
        pass
    else:
        raise Exception('@{0} is not allowed to regiter.'.format(domain))
    # Return to Amazon Cognito
    return event