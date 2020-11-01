import threading


class AtomicCounter:
    """An atomic,thread-safe incrementing counter."""

    def __init__(self, initial=0):
        """Initialize a new atomic counter.

        Args:
            initial (int, optional): default value for atomic counter
        """
        self.value = initial
        self._lock = threading.Lock()

    def increment(self, num=1):
        """Atomically increment the counter.

        Args:
            num (int, optional): Value to increase counter

        Returns:
            int: the new increased value
        """
        with self._lock:
            self.value += num
            return self.value

    def get_and_set(self, new_value):
        """Atomically sets to the given value and returns the old value.

        Args:
            new_value : the new value

        Returns:
            int: the old value
        """
        with self._lock:
            old_value = self.value
            self.value = new_value
            return old_value
