import boto3

import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), "./vendored"))
import numpy as np
import utils
import time
import datetime


def main():
    while True:
        value = int(np.random.randint(low=1,high=100,size=(1),dtype='int')[0])
        utils.put_custom_metric("target_metric", value,
                                datetime.datetime.utcnow(), progress_bar=True)
        time.sleep(1)

if __name__=="__main__":
    main()