import json, os
def lambda_handler(event, context):
    "Lambda function handler that processes incoming events and returns a response."
    print("Received event: " + json.dumps(event, indent=2))
    
    # Example processing
    message = 'Hello from Arnab Lambda!'
    
    # Return a response
    return {
        'statusCode': 200,
        'body': json.dumps({
            'message': message
        })
    }
