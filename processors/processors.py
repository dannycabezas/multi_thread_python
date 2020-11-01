import datetime
import logging
import time

from utils import EntityFactory
from .base import BaseProcessor

# Initialize the logging
format = "%(asctime)s: %(message)s"
logging.basicConfig(format=format, level=logging.INFO,
                    datefmt="%H:%M:%S")


class MetadataDecorator(BaseProcessor):

    @staticmethod
    def process(body):
        logging.info(f"Processing: {body}")
        current_time = time.time()
        iso_timestamp = datetime.datetime.fromtimestamp(current_time).isoformat()
        obj = {
                "event": body,
                "metadata": {
                        "timestamplong": int(current_time * 1000),
                        "ISOtimestamptext": iso_timestamp
                }
        }
        logging.info(f"Result after processing: {obj}")
        return obj


class MetadataDecoratorBuilder:
    def __init__(self):
        self._instance = None

    def __call__(self, **_ignored):
        if not self._instance:
            self._instance = MetadataDecorator()
        return self._instance


# Register the different sources
client = EntityFactory()
client.register_builder("MetaDecorator", MetadataDecoratorBuilder())
