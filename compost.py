from boto.s3.bucket import Bucket


class Compost(object):
    def __init__(self, directory, bucket):
        self.directory = directory
        self.bucket = Bucket(bucket)
