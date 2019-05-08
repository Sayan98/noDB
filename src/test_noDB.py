"""usage for noDB"""

from noDB import noDB


def test_noDB():
    db = noDB()
    record = {"test": "record"}

    db.add_record(record)
    assert db.get_records() == [record]

