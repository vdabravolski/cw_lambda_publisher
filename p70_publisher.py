import boto3
import datetime
import utils
from dateutil.tz import *

def main(event, context):

    now = datetime.datetime.utcnow()
    end_time = now
    start_time = now - datetime.timedelta(minutes=1)
    response = utils.get_metric_statistics('target_metric', start_time=start_time, end_time=end_time)

    value = response['Datapoints'][0]['ExtendedStatistics']['p70']
    timestamp = response['Datapoints'][0]['Timestamp'].isoformat()
    utils.put_custom_metric('p70_target_metric', value, timestamp)


if __name__=="__main__":
    # to run it locally (not on Lambda)
    main("","")


