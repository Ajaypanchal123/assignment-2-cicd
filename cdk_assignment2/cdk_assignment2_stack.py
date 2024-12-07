from aws_cdk import (
    RemovalPolicy,
    Stack,
    aws_s3 as s3,
    aws_lambda as _lambda,
    aws_dynamodb as dynamodb,
    aws_apigateway as apigateway
) 
from constructs import Construct
class CdkAssignment2Stack(Stack):

    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Define an S3 bucket
        s3_bucket = s3.Bucket(self, "PunitDariraAssignment2Bucket",
                              versioned=True,
                              removal_policy=RemovalPolicy.DESTROY)

        # Define a Lambda function
        lambda_function = _lambda.Function(self, "PunitDariraAssignment2Lambda",
                                           runtime=_lambda.Runtime.NODEJS_LATEST,
                                           handler="index.handler",
                                           code=_lambda.Code.from_inline(
                                               "exports.handler = async function(event) { "
                                               "console.log('Lambda invoked!'); "
                                               "return { statusCode: 200, body: 'Hello, World!' }; "
                                               "}"
                                           ))

        # Define a DynamoDB table
        dynamo_table = dynamodb.Table(self, "PunitDariraAssignment2Table",
                                      partition_key=dynamodb.Attribute(
                                          name="id",
                                          type=dynamodb.AttributeType.STRING),
                                          removal_policy=RemovalPolicy.DESTROY)

        # Define an API Gateway to trigger the Lambda function
        api = apigateway.LambdaRestApi(self, "MyApi",
                                       handler=lambda_function)