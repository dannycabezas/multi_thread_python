import logging

from core import EventConsumer
from core import EventDispatcher
from core import EventProducer
from core import Sentinel
from core.settings import DATABASE_CONF
from core.settings import KINESIS_CONF
from core.settings import SENTINEL_CONFIG
from destinations import client as dc
from processors import client as pc
from sources import client as sc

# Initialize the logging
format = "%(asctime)s: %(message)s"
logging.basicConfig(format=format, level=logging.INFO,
                    datefmt="%H:%M:%S")

# Initialize the entities
source = sc.get("DummyDB", **DATABASE_CONF)
source.ping()
destination = dc.get("Kinesis", **KINESIS_CONF)
destination.ping()
processor = pc.get("MetaDecorator")


def start_etl(source, processor, destination, number_events=None):
    sentinel = Sentinel(**SENTINEL_CONFIG)
    producer = EventProducer(source, sentinel)
    consumer = EventConsumer(destination, processor, sentinel)
    dispatcher = EventDispatcher(producer, consumer, sentinel)
    dispatcher.dispatch(number_events)
    summary = {
            "TotalEventsProduced": sentinel.get_events_produced(),
            "TotalEventsConsumed": sentinel.get_events_consumed(),
            "SampleProcessingEvent": sentinel.sample_processing_event,
    }
    return summary


if __name__ == "__main__":
    # Multi-thread instances

    # Start a free consumer/producer version
    response = start_etl(source, processor, destination)

    # uncomment the line below to start a consumer/producer on demand --> 2000 events in this case
    # start_etl(source, processor, destination, 2000)
    print(response)
