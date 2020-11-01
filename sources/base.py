import abc


class BaseSource(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def fetch_data(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def ping(self, *args, **kwargs):
        # just to check if the origin is available :)
        pass

    @abc.abstractmethod
    def serialize(self, *args, **kwargs):
        # the source must know in what format to deliver the data to me
        # this could be a factory method pattern itself
        pass

