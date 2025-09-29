import aws_cdk as core
import aws_cdk.assertions as assertions

from test_v1.test_v1_stack import TestV1Stack

# example tests. To run these tests, uncomment this file along with the example
# resource in test_v1/test_v1_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = TestV1Stack(app, "test-v1")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
