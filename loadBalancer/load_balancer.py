import threading
from random import choice

class LoadBalancer:
    def __init__(self, max_providers=10):
        self.max_providers = max_providers
        self.providers = []
        self.free_providers = []
        self._lock = threading.Lock()

    def add_provider(self, provider):
        """
        Add provider to the list is it is not full
        """
        if len(self.providers) >= self.max_providers:
            raise BufferError("Provider list is full.")
        else:
            self.providers.append(provider)
            self.free_providers.append(len(self.free_providers))

    def _get_provider_random(self):
        """
        Return a random free provider
        """
        #We get a provider index at random
        free_provider_id = choice(range(len(self.free_providers)))
        provider_id = self.free_providers[free_provider_id]
        provider = self.providers[provider_id]
        self.free_providers[free_provider_id] = self.free_providers[-1]
        #We remove the index from the list
        self.free_providers.pop()

        return provider_id, provider

    def get(self):
        """
        Send the GET request to a provider
        """
        provider = None
        provider_id = None
        with self._lock:
            provider_id, provider = self._get_provider_random()

        val = provider.get()
        with self._lock:
            #The provider is now available again
            self.free_providers.append(provider_id)

        return val
