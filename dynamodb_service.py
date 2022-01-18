import boto3
from boto3.dynamodb.conditions import Key
import aws_config


# Getting single item using table reference
def get_single_item_using_table():
    dynamo_db_client = aws_config.get_dynamo_db_client()
    # getting dynamodb table reference by giving dynamodb client and table name
    dynamo_db_table = aws_config.get_dynamo_db_table(dynamo_db_client, 'Transactions')
    retrieved_item = dynamo_db_table.get_item(
        Key={
            'transaction-id': 't1',
            'date': '2021-03-01'
        }
    )
    print(retrieved_item['Item'])


# Querying items using table reference
def get_multiple_item_using_table():
    dynamo_db_client = aws_config.get_dynamo_db_client()
    dynamo_db_table = aws_config.get_dynamo_db_table(dynamo_db_client, 'Transactions')
    # Key is a key attribute in Table
    retrieved_item = dynamo_db_table.query(
        KeyConditionExpression=Key('transaction-id').eq('t1') & Key('date').eq('2021-03-01')
    )
    # Example of scanning table using table reference
    # Attr is an attribute in Table
    # table.scan(
    #     FilterExpression=Attr('date').eq('2021-03-01')
    # )
    print(retrieved_item['Items'])


if __name__ == '__main__':
    get_single_item_using_table()
    get_multiple_item_using_table()
