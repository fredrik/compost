import os, shutil, tempfile

from compost import Compost
import helpers


def test_turning_compost_does_not_overwrite_changes():
    try:
        temporary_directory = tempfile.mkdtemp()
        compost = Compost(
            directory=temporary_directory,
            bucket='test-git-repos-51806ac9a7bba4c653688ff6f18d04f2'
        )
        helpers.delete_all(bucket_name='test-git-repos-51806ac9a7bba4c653688ff6f18d04f2')

        with open(os.path.join(temporary_directory, 'some-capitals'), 'w+') as f:
            f.write("budapest.\n")
        compost.turn()
        assert compost.read('some-capitals') == "budapest.\n"

        with open(os.path.join(temporary_directory, 'some-capitals'), 'w+') as f:
            f.write("bratislava.\n")
            f.write("vienna.\n")
        compost.turn()
        assert compost.read('some-capitals') == "budapest.\n"

    finally:
        shutil.rmtree(temporary_directory, ignore_errors=True)
