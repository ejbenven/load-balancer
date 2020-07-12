import threading

class Provider:
    id = 0
    lock = threading.Lock()

    def __init__(self):
        """
        Create a provider with a unique ID
        """
        with Provider.lock:
            self._id = Provider.id
            Provider.id += 1

    def get(self):
        return f'{self._id}'
