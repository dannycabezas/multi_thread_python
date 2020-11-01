# **************** DISCLAIMER ***********************
# Most of these configurations should be configured through
# system environment variables, but for simplicity I decided
# to use variables with raw data (hardcode) :)

KINESIS_CONF = {"client_key": "1234", "client_secret": "my_secret"}
DATABASE_CONF = {"url": "fwjgyq5a.us-east-1.es.amazonaws.com", "db_name": "fake"}
MAX_THREADS = 3

MAX_WORKERS = 10
BUFFER_SIZE = 0
SHUTDOWN_TIME = 0.1

SENTINEL_CONFIG = {
        "max_workers": MAX_WORKERS,
        "buffer_size": BUFFER_SIZE,
        "shutdown_time": SHUTDOWN_TIME,
}
