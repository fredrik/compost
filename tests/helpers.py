import boto
from boto.s3.bucket import Bucket


def empty_bucket(bucket_name):
    """Destructive helper."""
    bucket = Bucket(connection=boto.connect_s3(), name=bucket_name)
    for key in bucket.get_all_keys():
        key.delete()
