import logging

from utils import EntityFactory
from .base import BaseDestination

# Initialize the logging
format = "%(asctime)s: %(message)s"
logging.basicConfig(format=format, level=logging.INFO,
                    datefmt="%H:%M:%S")


class Kinesis(BaseDestination):
    def __init__(self, client_key, client_secret):
        self.client_key = client_key
        self.client_secret = client_secret

    def ping(self):
        logging.info(" Connection with kinesis has been established")

    def send(self, data):
        logging.info(f"Sending the data: {data}")


class KinesisBuilder:
    def __init__(self):
        self._instance = None

    def __call__(self, client_key, client_secret, **_ignored):
        if not self._instance:
            self._instance = Kinesis(client_key, client_secret)
        return self._instance


# Register the different sources
client = EntityFactory()
client.register_builder("Kinesis", KinesisBuilder())
