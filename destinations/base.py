import abc


class BaseDestination(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def send(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def ping(self, *args, **kwargs):
        # just to check if the destination is available :)
        pass
