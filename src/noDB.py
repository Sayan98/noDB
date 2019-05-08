"""
noDB
"""

import json
import os
import time


DATA = """[]"""


class noDB:
    def __init__(self):
        self.data = json.loads(DATA)

    def add_record(self, record):
        """record: a valid JSON object"""
        self.data.append(record)

    def get_records(self):
        """return all items"""
        return self.data

    def commit(self):
        """commit changes to database (lol?)"""
        with open(__file__, "rt") as f:
            current_db = f.read()
            updated_db = current_db.replace(f'DATA = """{DATA}"""',
                                            f'DATA = """{json.dumps(self.data)}"""')
            # print(updated_db)
            with open (__file__, "wt") as of:
                of.write(updated_db)



if __name__ == '__main__':
    db = noDB()

    db.add_record({"first": 1})
    db.add_record({"second": 2})
    db.add_record({"third": 3})

    db.commit()
