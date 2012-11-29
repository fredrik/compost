from compost import Compost

from .helpers import empty_bucket


def test_compost():
    """
    Test the very basics of compost management:
    Synchronise a local directory to the backup location,
    make sure that the files we expect to have been backed up are available
    to list and retrieve.

    Connects to an actual S3 bucket (as defined below) using any keys you might have
    defined in your environment.
    """

    compost = Compost(
        directory='/data/git-repos',
        bucket='test-git-repos-51806ac9a7bba4c653688ff6f18d04f2'
    )

    assert compost.list() == []

    compost.turn()
    known_files = compost.list()
    assert sorted(known_files) == ['desktop-20120828.bundle', 'home-20120828.bundle']

    assert compost.read('home-20120828.bundle') == 'heh, what? this is not a binary bundle.\n'
    assert compost.read('desktop-20120828.bundle') == 'nor are we.\n'

    empty_bucket('test-git-repos-51806ac9a7bba4c653688ff6f18d04f2')
    assert compost.list() == []
