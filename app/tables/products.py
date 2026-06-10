import os
import boto3
from dotenv import load_dotenv

load_dotenv()
<<<<<<< HEAD
dynamodb = boto3.resource('dynamodb', region_name=os.environ.get("REGION_NAME"))
=======

dynamodb = boto3.resource(
	"dynamodb",
	region_name=os.environ.get("AWS_DEFAULT_REGION", "us-west-2"),
)
>>>>>>> f2bc22a (Changed us-east-1 to us-west-2)
products_table = dynamodb.Table(name=os.environ.get("TABLE_NAME"))
