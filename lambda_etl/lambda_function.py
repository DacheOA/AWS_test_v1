import boto3
import os

def lambda_handler(event, context):
    table_name = os.environ.get("TABLE_NAME")
    dynamodb = boto3.resource('dynamodb')
    #table = dynamodb.Table('ResultsTable')
    table = dynamodb.Table(table_name)

    # Insertar un ejemplo de datos
    table.put_item(
        Item={
            'user_id': '123',
            'transactions_count': 10,
            'total_amount': 250
        }
    )
    return{
        'statusCode': 200,
        'body': 'Datos insertados correctamente en DynamoDB'
    }