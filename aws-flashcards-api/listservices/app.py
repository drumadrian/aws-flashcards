# References: 
# https://us-west-2.console.aws.amazon.com/lambda/home?region=us-west-2#/create/app?applicationId=arn:aws:serverlessrepo:us-east-1:387304072572:applications/amazon-elasticsearch-service-with-cognito
# https://github.com/chankh/ddb-elasticsearch

import json
import os
import logging
from elasticsearch import Elasticsearch, RequestsHttpConnection
from aws_requests_auth.aws_auth import AWSRequestsAuth

logger = logging.Logger
es_host = os.getenv('ELASTICSEARCH_URL')
es_index = os.getenv('ELASTICSEARCH_INDEX')
key_name = os.getenv('KEY_NAME')
access_key = os.getenv('AWS_ACCESS_KEY_ID')
secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY')
session_token = os.getenv('AWS_SESSION_TOKEN')
region = os.getenv('AWS_REGION')

# Establish connection to ElasticSearch
auth = AWSRequestsAuth(aws_access_key=access_key,
                       aws_secret_access_key=secret_access_key,
                       aws_token=session_token,
                       aws_host=es_host,
                       aws_region=region,
                       aws_service='es')

es = Elasticsearch(host=es_host,
                   port=443,
                   use_ssl=True,
                   connection_class=RequestsHttpConnection,
                   http_auth=auth)

logger.info(es.info())





def lambda_handler(event, context):
    """Lambda Function entrypoint handler

    :event: DynamoDB Stream event
    :context: Lambda context
    :returns: Number of records processed

    """
    # processed = 0
    # for record in event['Records']:
    #     ddb_record = record['dynamodb']
    #     logger.debug(record['eventID'] + " " + record['eventName'])
    #     # print("DynamoDB Record: " + json.dumps(ddb_record, indent=2))
    #     key = str(ddb_record['Keys'][key_name]['S'])
    #     if record['eventName'] == 'REMOVE':
    #         logger.debug("Deleting record: " + key)
    #         res = es.delete(index=es_index, doc_type='event', id=key)
    #     else:
    #         image = ddb_record['NewImage']
    #         res = es.index(index=es_index, doc_type='event',
    #                        id=key, body=image)

    #         logger.debug(res)
    #     processed = processed + 1

    # logger.info('Successfully processed {} records'.format(processed))
    # return processed


    """Sample pure Lambda function

    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

        Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict

        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """

    # try:
    #     ip = requests.get("http://checkip.amazonaws.com/")
    # except requests.RequestException as e:
    #     # Send some context about this error to Lambda Logs
    #     print(e)

    #     raise e

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world listservices",
            # "location": ip.text.replace("\n", "")
        }),
    }



