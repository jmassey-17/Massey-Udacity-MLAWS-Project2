

import json
import base64
import boto3

# Fill this in with the name of your deployed model
ENDPOINT ='image-classification-2024-10-29-08-00-59-869'

def lambda_handler(event, context):

    # Decode the image data
    image = base64.b64decode(event['body']['image_data'])
    
    # Define content
    content_type = "image/png"
    
    # Initialize SageMaker runtime client
    sagemaker_runtime = boto3.client("sagemaker-runtime")

    # Make prediction 
    inferences = sagemaker_runtime.invoke_endpoint(
        EndpointName=ENDPOINT,
        ContentType=content_type,
        Body=image
    )

    # upload inferences 
    event["inferences"] = json.loads(inferences['Body'].read().decode('utf-8'))
    return {
        'statusCode': 200,
        'body': event
    }

