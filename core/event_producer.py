import logging

# Initialize the logging
format = "%(asctime)s: %(message)s"
logging.basicConfig(format=format, level=logging.INFO,
                    datefmt="%H:%M:%S")


class EventProducer:
    def __init__(self, source, sentinel):
        self.source = source
        self.sentinel = sentinel

    def get_event(self):
        return self.source.fetch_data()

    def produce_freely(self):
        while not self.sentinel.should_collector_shutdown():
            self._produce()

    def produce_on_demand(self, max_events):
        for _ in range(max_events):
            self._produce()

    def _produce(self):
        data = self.get_event()
        logging.info("Producer got data: %s", data)
        self.sentinel.put_message(data)
        self.sentinel.increase_produced()

    def produce(self, max_events=None):
        if max_events is not None:
            self.produce_on_demand(max_events)
        else:
            self.produce_freely()
        logging.info("Producer finished producing. Exiting")
