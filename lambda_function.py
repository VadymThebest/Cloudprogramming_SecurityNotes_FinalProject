import boto3
import json
import uuid
from boto3.dynamodb.conditions import Key

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('NotesTable')

def lambda_handler(event, context):
    print(f"Received event: {json.dumps(event)}")
    
    try:
        method = event.get('httpMethod')
        user_id = "vadym_user_1" 
        
        if method == 'POST':
            body = json.loads(event.get('body', '{}'))
            note_content = body.get('content', 'Пустая заметка')
            item = {
                'userId': user_id,
                'noteId': str(uuid.uuid4()),
                'content': note_content
            }
            table.put_item(Item=item)
            return response(201, item)
            
        elif method == 'GET':
            result = table.query(
                KeyConditionExpression=Key('userId').eq(user_id)
            )
            return response(200, result.get('Items', []))
            
        elif method == 'DELETE':
            path_params = event.get('pathParameters') or {}
            note_id = path_params.get('id')
            
            if not note_id:
                query_params = event.get('queryStringParameters') or {}
                note_id = query_params.get('id')

            if not note_id:
                return response(400, {"message": "Missing noteId"})

            table.delete_item(
                Key={
                    'userId': user_id,
                    'noteId': note_id
                }
            )
            return response(200, {"message": "Deleted successfully"})
            
        return response(400, {"message": "Unsupported method"})
        
    except Exception as e:
        print(f"Error: {str(e)}")
        return response(500, {"error": str(e)})

def response(status, body):
    return {
        'statusCode': status,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET,DELETE',
            'Access-Control-Allow-Headers': 'Content-Type,Authorization'
        },
        'body': json.dumps(body)
    }