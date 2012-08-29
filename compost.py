from boto.s3.bucket import Bucket


class Compost(object):

    def __init__(self, directory, bucket):
        self.directory = directory
        self.bucket = Bucket(bucket)

    def turn(self):
        """
        'Turn' the compost, i.e. make a backup of all files in the local directory.
        """
        pass

    def list(self):
        """Return a list of known backed up files."""
        return []

    def read(self, filename):
        """
        Return the contents of named file, or the empty string if the files does not exist.
        """
        return ""
