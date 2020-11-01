import pytest


@pytest.fixture
def bdd_context():
    class Context(object):
        pass

    return Context()


@pytest.fixture()
def mock_source(mocker):
    source = mocker.patch(
            "multithread_challenge.main.sc"
    )
    return source


@pytest.fixture()
def mock_destination(mocker):
    destination = mocker.patch(
            "multithread_challenge.main.dc"
    )
    return destination


@pytest.fixture()
def mock_processor(mocker):
    processor = mocker.patch(
            "multithread_challenge.main.pc"
    )
    return processor


@pytest.fixture()
def mock_config():
    return {"fakeConfig": "fake"}
