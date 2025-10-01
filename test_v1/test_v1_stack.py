from aws_cdk import (
    # Duration,
    Stack,
    # aws_sqs as sqs,
    aws_s3 as s3,
    aws_lambda as _lambda,
    aws_dynamodb as dynamodb,
)
from constructs import Construct

class TestV1Stack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Crear el S3 Bucket para cargar los CSVs
        data_bucket = s3.Bucket(self, "DataBucket")

        # Crear tabla en dynamoDB para guardar el contenido de los CSVs
        results_table = dynamodb.Table(
            self, "ResultsTable",
            partition_key=dynamodb.Attribute(
                name="user_id",
                type=dynamodb.AttributeType.STRING
            ),
            billing_mode=dynamodb.BillingMode.PAY_PER_REQUEST,
            #billing=dynamodb.Billing.on_demand(),
        )

        # Crear la función lambda para leer y procesar los CSVs que se encuentren en el S3
        etl_lambda = _lambda.Function(
            self, "ETLFunction",
            runtime= _lambda.Runtime.PYTHON_3_9,
            handler="lambda_function.lambda_handler",
            code=_lambda.Code.from_asset("lambda_etl"),
            environment={"TABLE_NAME": results_table.table_name},
        )

        # Dar permisos a lambda para escribir en dynamodb
        results_table.grant_write_data(etl_lambda)


