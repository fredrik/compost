import os
import logging

import boto
from boto.s3.bucket import Bucket


logger = logging.getLogger('compost')


class Compost(object):

    def __init__(self, directory, bucket):
        self.directory = directory
        self.bucket = Bucket(connection=boto.connect_s3(), name=bucket)

    def turn(self):
        """
        'Turn' the compost, i.e. make a backup of all files in the local directory.
        """
        for filename, full_path in self._local_files():
            logger.debug('backing up {}'.format(filename))
            key = self.bucket.new_key(filename)
            key.set_contents_from_filename(full_path, replace=False)

    def list(self):
        """Return a list of known backed up files."""
        return [k.name for k in self.bucket.get_all_keys()]

    def read(self, filename):
        """
        Return the contents of named file, or the empty string if the files does not exist.
        """
        return self.bucket.get_key(filename).get_contents_as_string()


    def _local_files(self):
        for f in os.listdir(self.directory):
            yield f, os.path.join(self.directory, f)
