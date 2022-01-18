import boto3


def get_dynamo_db_client():
    # Instead of aws_access_key_id, aws_secret_access_key give your aws id and secret key
    return boto3.resource('dynamodb',
                          'us-east-2',
                          aws_access_key_id='<aws_access_key_id>',
                          aws_secret_access_key='<aws_secret_access_key>')


def get_dynamo_db_table(dynamo_db_client, table_name):
    return dynamo_db_client.Table(table_name)
