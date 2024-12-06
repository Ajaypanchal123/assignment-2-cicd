import aws_cdk as core
import aws_cdk.assertions as assertions

from cdk_assignment2.cdk_assignment2_stack import CdkAssignment2Stack

# example tests. To run these tests, uncomment this file along with the example
# resource in cdk_assignment2/cdk_assignment2_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = CdkAssignment2Stack(app, "cdk-assignment2")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
