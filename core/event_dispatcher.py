import logging
from concurrent.futures import ThreadPoolExecutor

# Initialize the logging
format = "%(asctime)s: %(message)s"
logging.basicConfig(format=format, level=logging.INFO,
                    datefmt="%H:%M:%S")


class EventDispatcher:

    def __init__(self, producer, consumer, sentinel):
        self.producer = producer
        self.consumer = consumer
        self.sentinel = sentinel

    def dispatch(self, max_events=None):
        with ThreadPoolExecutor(max_workers=self.sentinel.max_workers) as executor:
            executor.submit(self.producer.produce, max_events)
            executor.submit(self.consumer.consume, max_events)
            self.shutdown()

    def shutdown(self):
        self.sentinel.shutdown()
