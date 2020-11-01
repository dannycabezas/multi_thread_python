import json
import logging
import random

from utils import EntityFactory
from .base import BaseSource

# Initialize the logging
format = "%(asctime)s: %(message)s"
logging.basicConfig(format=format, level=logging.INFO,
                    datefmt="%H:%M:%S")


class DummyDB(BaseSource):
    def __init__(self, url, db_name):
        self.url = url
        self.db_name = db_name

    def ping(self):
        logging.info(f" Connection with {self.db_name} database has been established")

    def fetch_data(self):
        id = random.randint(1, 101)
        data = {"id": id, "msg": "Dummy event {}".format(str(id))}
        data = self.serialize(data)
        return data

    def serialize(self, data):
        return json.dumps(data)


class DummyDBBuilder:
    def __init__(self):
        self._instance = None

    def __call__(self, url, db_name, **_ignored):
        if not self._instance:
            self._instance = DummyDB(url, db_name)
        return self._instance

# Register the different sources
client = EntityFactory()
client.register_builder("DummyDB", DummyDBBuilder())
