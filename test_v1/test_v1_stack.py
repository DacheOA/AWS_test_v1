from aws_cdk import (
    # Duration,
    Stack,
    # aws_sqs as sqs,
    aws_s3 as s3,
    aws_lambda as _lambda
)
from constructs import Construct

class TestV1Stack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Crear el S3 Bucket para cargar los CSVs
        self.data_bucket = s3.Bucket(self, "DataBucket")

        # Crear la función lambda para leer y procesar los CSVs que se encuentren en el S3
        self.etl_lambda = _lambda.Function(
            self, "ETLFunction",
            runtime= _lambda.Runtime.PYTHON_3_12,
            handler="lambda_function.lambda_handler",
            code=_lambda.Code.from_asset("lambda_etl")
        )


