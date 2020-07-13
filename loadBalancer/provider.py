import threading


class Provider:
    id = 0
    lock = threading.Lock()

    def __init__(self, alive=True, forever=True):
        """
        Create a provider with a unique ID
        For testing purposes, can define if provider is alive
        If forerver is false, will toggle the alive status after the first check
        """
        with Provider.lock:
            self._id = Provider.id
            Provider.id += 1

        self.alive = alive
        self.forever = forever

    def get(self):
        return f"{self._id}"

    def check(self):
        alive = self.alive

        if not self.forever:
            self.forever = True
            self.alive = not self.alive
        return alive
