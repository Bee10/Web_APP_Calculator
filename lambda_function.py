import json

def lambda_handler(event, context):
    base = float(event["base"])
    exponent = float(event["exponent"])

    result = base ** exponent

    return {
        "statusCode": 200,
        "body": json.dumps({
            "result": result
        })
    }