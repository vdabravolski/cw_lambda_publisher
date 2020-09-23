import boto3
import time
import sys

NAMESPACE = "custom_namespace"
DIMENSION_NAME = "type"
DIMENSION_VALUE = "test"
AWS_REGION = "us-east-2"
client = boto3.client("cloudwatch", region_name=AWS_REGION)

toolbar_width = 40
sys.stdout.write("[%s]" % (" " * toolbar_width))
sys.stdout.flush()
sys.stdout.write("\b" * (toolbar_width+1)) # return to start of line, after '['


def put_custom_metric(metric_name, value, timestamp, progress_bar=False):
    try:
        client.put_metric_data(
            Namespace=NAMESPACE,
            MetricData=[
                {
                    'MetricName': metric_name,
                    'Dimensions': [
                        {
                            'Name': DIMENSION_NAME,
                            'Value': DIMENSION_VALUE
                        },
                    ],
                    'Timestamp': timestamp,
                    'Value': value,
                    'Unit': 'Seconds',
                    'StorageResolution': 1
                }])
        if progress_bar:
            sys.stdout.write(".")
            sys.stdout.flush()
        return True
    except Exception as e:
        print(f"Error while publishing  metric. {e}.")


def get_metric_statistics(metric_name, start_time, end_time, ext_stats=['p70']):
    response = client.get_metric_statistics(
        Namespace=NAMESPACE,
        MetricName=metric_name,
        Dimensions=[{
            'Name': DIMENSION_NAME,
            'Value': DIMENSION_VALUE
        }],
        StartTime=start_time,
        EndTime=end_time,
        Period=60,
        ExtendedStatistics=ext_stats 
    )

    return response