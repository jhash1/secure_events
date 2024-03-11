import boto3
import json
import requests

def lambda_handler(event, context):
    ec2_client = boto3.client('ec2')
    body = event['body']
    body_json = json.loads(body)
    # print(body_json, "john1")
    # print(body_json['detail'],"john2")
    instance_id = data['detail']['requestParameters']['instancesSet']['items'][0]['instanceId']
    print("Instance ID:", instance_id)
    
    
