import abc


class BaseProcessor(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def process(self, *args, **kwargs):
        pass

