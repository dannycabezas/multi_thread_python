import logging

from multithread_challenge.main import start_etl
from pytest_bdd import given
from pytest_bdd import scenario
from pytest_bdd import then
from pytest_bdd import when
from unittest import mock


def uppercase(data):
    return data.upper()


def lowercase(data):
    return data.lower()


def generate_database_data():
    return {"test": "data"}


def generate_log_file_data():
    return "This is a test log"


def metadata_decorator(data):
    return {"body": data, "metadata": {"test": 1}}


def check_json_metadata(data):
    return "body" in data


def check_lowercase(data):
    return data.islower()


WORK_FLOWS = {
        "DummyDB": {
                "generator": generate_database_data,
                "processors": {"metadata_decorator": metadata_decorator},
                "checker": check_json_metadata,
        },
        "TextFile": {
                "generator": generate_log_file_data,
                "processors": {"lowercase": lowercase},
                "checker": check_lowercase,
        }
}

# Initialize the logging
format = "%(asctime)s: %(message)s"
logging.basicConfig(format=format, level=logging.INFO,
                    datefmt="%H:%M:%S")


@scenario(feature_name="my_feature.feature",
          scenario_name="ETL between database and kinesis in free mode",
          example_converters=dict(source=str,
                                  destination=str,
                                  processor=str,
                                  ))
def test_free_version_scenario():
    logging.info("Starting scenario validation...")


@scenario(feature_name="my_feature.feature",
          scenario_name="ETL between database and kinesis with a defined batch of events",
          example_converters=dict(source=str,
                                  destination=str,
                                  processor=str,
                                  number_events=int,
                                  ))
def test_batch_events_scenario():
    print("Starting scenario validation...")


@given("an <source> as source")
def step_impl(bdd_context, source):
    mock_source = mock.Mock()
    workflow = WORK_FLOWS[source]
    generator = workflow["generator"]
    mock_source.fetch_data = generator
    bdd_context.source = mock_source
    bdd_context.workflow = workflow


@given("a <destination> as destination")
def step_impl(bdd_context, mock_destination, destination, mock_config):
    bdd_context.destination = mock_destination.get(destination, **mock_config)


@given("a <processor> processor")
def step_impl(bdd_context, processor):
    mock_processor = mock.Mock()
    processor = bdd_context.workflow["processors"][processor]
    mock_processor.process = processor
    bdd_context.processor = mock_processor


@when("I start ETL in free mode")
def step_impl(bdd_context):
    result = start_etl(bdd_context.source, bdd_context.processor, bdd_context.destination)
    bdd_context.result = result


@when("I start ETL with a batch of <number_events> events")
def step_impl(bdd_context, number_events):
    result = start_etl(bdd_context.source, bdd_context.processor, bdd_context.destination, number_events)
    bdd_context.result = result


@then("I get the same number of events produced as consumed")
def step_impl(bdd_context):
    assert bdd_context.result["TotalEventsProduced"] == bdd_context.result["TotalEventsConsumed"]
    checker = bdd_context.workflow["checker"]
    assert checker(bdd_context.result["SampleProcessingEvent"])
