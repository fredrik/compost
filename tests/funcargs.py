import pytest

from compost import Compost
from . import helpers


@pytest.fixture
def compost(request):
    """
    Returns a Compost object that is guaranteed to be empty.
    """
    # assumed pre-conditions:
    #  + the bucket test-git-repos-51806ac9a7bba4c653688ff6f18d04f2 exists and is writable.
    #  + /data/git-repos exists and contains some files (details below in actual tests).
    helpers.delete_all(bucket_name='test-git-repos-51806ac9a7bba4c653688ff6f18d04f2')
    return Compost(
        directory='/data/git-repos',
        bucket='test-git-repos-51806ac9a7bba4c653688ff6f18d04f2'
    )
