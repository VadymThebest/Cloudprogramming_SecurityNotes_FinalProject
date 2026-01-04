import json
import pytest
from lambda_function import lambda_handler 

def test_unsupported_method():
    event = {'httpMethod': 'PATCH'}
    response = lambda_handler(event, None)
    assert response['statusCode'] == 400
    assert "Unsupported method" in response['body']

def test_missing_delete_id():
    event = {
        'httpMethod': 'DELETE',
        'queryStringParameters': {}
    }
    response = lambda_handler(event, None)
    assert response['statusCode'] == 400
    assert "Missing id" in response['body']