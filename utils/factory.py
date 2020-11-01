
class EntityFactory:
    def __init__(self):
        self._builders = {}

    def register_builder(self, key, builder):
        self._builders[key] = builder

    def get(self, key, **kwargs):
        if not key in self._builders:
            raise ValueError(f"{key} not registered")
        return self._builders[key](**kwargs)

