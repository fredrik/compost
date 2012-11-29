"""
These tests cover the very basics of compost management:
Synchronise a local directory to the backup location,
make sure that the files we expect to have been backed up are available
to list and retrieve.

Connects to an actual S3 bucket (as defined below) using any keys you might have
defined in your environment.
"""
from funcargs import compost


def test_empty_compost_is_empty(compost):
    assert compost.list() == []


def test_turning_a_compost_synchronises_local_files_with_remote_bucket(compost):
    compost.turn()
    known_files = compost.list()
    assert sorted(known_files) == ['desktop-20120828.bundle', 'home-20120828.bundle']


def test_read(compost):
    compost.turn()
    assert compost.read('home-20120828.bundle') == 'heh, what? this is not a binary bundle.\n'
    assert compost.read('desktop-20120828.bundle') == 'nor are we.\n'
