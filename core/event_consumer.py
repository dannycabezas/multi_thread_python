import logging

# Initialize the logging
format = "%(asctime)s: %(message)s"
logging.basicConfig(format=format, level=logging.INFO,
                    datefmt="%H:%M:%S")


class EventConsumer:
    """Represents a consumer."""

    def __init__(self, destination, processor, sentinel):
        """
        Initialize a consumer

        :param destination (obj): Destination where the events will be sent once consumed
        :param processor (obj): Process that will be applied to each of the events consumed
        :param sentinel (obj): Observer and buffer controller, records the consumed and produced events
        """
        self.destination = destination
        self.processor = processor
        self.sentinel = sentinel

    def consume_freely(self):
        while not self.sentinel.should_collector_shutdown() or not self.sentinel.is_message_queue_empty():
            self._consume()

    def _consume(self):
        message = self.sentinel.get_message()
        message = self.processor.process(message)
        self.destination.send(message)
        self.sentinel.increase_consumed()
        if self.sentinel.sample_processing_event is None:
            # get only a small piece of the processed events :)
            self.sentinel.sample_processing_event = message

    def consume_on_demand(self, max_events):
        for _ in range(max_events):
            self._consume()

    def consume(self, max_events=None):
        """
        Consumes the events stored in the buffer,
        processes them and sends them to their destination
        """
        if max_events is not None:
            self.consume_on_demand(max_events)
        else:
            self.consume_freely()
        logging.info("Consumer received event. Exiting")
