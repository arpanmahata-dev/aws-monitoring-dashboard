import json
import boto3
from datetime import datetime, timedelta

cloudwatch = boto3.client('cloudwatch')
ec2 = boto3.client('ec2')
s3 = boto3.client('s3')

def lambda_handler(event, context):
    metrics = {
        'timestamp': datetime.now().isoformat(),
        'ec2_instances': get_ec2_metrics(),
        's3_buckets': get_s3_metrics(),
        'billing': get_billing_metrics()
    }
    
    # Store in S3
    s3.put_object(
        Bucket='your-monitoring-bucket',
        Key=f'metrics/{datetime.now().strftime("%Y-%m-%d-%H-%M")}.json',
        Body=json.dumps(metrics)
    )
    
    return {
        'statusCode': 200,
        'body': json.dumps('Metrics collected successfully')
    }

def get_ec2_metrics():
    instances = ec2.describe_instances()
    return {
        'total': len(instances['Reservations']),
        'running': sum(1 for r in instances['Reservations'] 
                      for i in r['Instances'] 
                      if i['State']['Name'] == 'running')
    }

def get_s3_metrics():
    buckets = s3.list_buckets()
    return {'total': len(buckets['Buckets'])}

def get_billing_metrics():
    end_time = datetime.now()
    start_time = end_time - timedelta(days=1)
    
    response = cloudwatch.get_metric_statistics(
        Namespace='AWS/Billing',
        MetricName='EstimatedCharges',
        Dimensions=[{'Name': 'Currency', 'Value': 'USD'}],
        StartTime=start_time,
        EndTime=end_time,
        Period=86400,
        Statistics=['Maximum']
    )
    
    if response['Datapoints']:
        return {'estimated_charges': response['Datapoints'][0]['Maximum']}
    return {'estimated_charges': 0}