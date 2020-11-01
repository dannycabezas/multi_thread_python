import queue
import threading
from time import sleep

from utils import AtomicCounter

class Sentinel:
    def __init__(self, max_workers, buffer_size=0, shutdown_time=0.1):
        self.max_workers = max_workers
        self.buffer_size = buffer_size
        self.shutdown_time = shutdown_time
        self._shutdown_signal = threading.Event()
        self._message_queue = queue.Queue(maxsize=self.buffer_size)
        self._events_produced = AtomicCounter()
        self._events_consumed = AtomicCounter()
        # TODO: this 'sample_processing_event' has the only intention of being able to have
        #  a sample of the processed events and only for simplicity of the challenge I decide to use it
        self.sample_processing_event = None

    def should_collector_shutdown(self):
        return self._shutdown_signal.is_set()

    def is_message_queue_empty(self):
        return self._message_queue.empty()

    def get_message(self):
        return self._message_queue.get()

    def put_message(self, message):
        self._message_queue.put(message)

    def increase_produced(self):
        self._events_produced.increment()

    def increase_consumed(self):
        self._events_consumed.increment()

    def shutdown(self):
        sleep(self.shutdown_time)
        self._shutdown_signal.set()

    def get_events_produced(self):
        return self._events_produced.value

    def get_events_consumed(self):
        return self._events_consumed.value

    def events_in_queue(self):
        return self._message_queue.qsize()
