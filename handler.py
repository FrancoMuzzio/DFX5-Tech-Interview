import json
import boto3
import uuid
from datetime import datetime
import os

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

def create_note(event, context):
    try:
        body = json.loads(event.get('body', '{}'))
        texto_nota = body.get('texto', '') 
        
        item = {
            'id': str(uuid.uuid4()),
            'texto': texto_nota
        }
        
        table.put_item(Item=item)
        
        return {
            'statusCode': 201,
            'body': json.dumps({'note': item})
        }
        
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }

def get_note(event, context):
    try:
        note_id = event['pathParameters']['id']
        response = table.get_item(Key={'id': note_id})
        
        if 'Item' not in response:
            return {
                'statusCode': 404,
                'body': json.dumps({'error': 'Nota no encontrada'})
            }
        
        return {
            'statusCode': 200,
            'body': json.dumps({'note': response['Item']})
        }
        
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }