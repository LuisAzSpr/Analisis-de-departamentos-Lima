import boto3
import json

runtime = boto3.client("sagemaker-runtime")

def lambda_handler(event, context):
    body = json.loads(event['body'])

    payload = (
        "latitud,dormitorios,longitud,banos,area,distrito,antiguedad_categoria\n"
        f"{body['latitud']},{body['dormitorios']},{body['longitud']},{body['banos']},{body['area']},{body['distrito']},{body['antiguedad_categoria']}"
    )

    response = runtime.invoke_endpoint(
        EndpointName="xgb-endpoint-v4",
        ContentType="text/csv",
        Accept="text/csv",
        Body=payload
    )

    result = response["Body"].read().decode("utf-8")

    return {
        "statusCode": 200,
        "body": json.dumps({"prediction": result})
    }
