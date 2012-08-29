from compost import Compost


def test_compost():
    """
    Test the very basics of compost management:
    Synchronise a local directory to the backup location,
    make sure that the files we expect to have been backed up are available
    to list and retrieve.
    """
    compost = Compost(
        directory='/data/git-repos',
        bucket='test-git-repos-51806ac9a7bba4c653688ff6f18d04f2'
    )

    assert compost.list() == []

    compost.turn()
    known_files = compost.list()
    assert known_files == ['home-20120828.bundle', 'desktop-20120828.bundle']

    assert compost.read('home-20120828.bundle') == 'heh, what? this is not a binary bundle.'
    assert compost.read('desktop-20120828.bundle') == 'nor are we.'
