class LoadBalancer:
    def __init__(self, max_providers=10):
        self.max_providers = max_providers
        self.providers = []

    def add_provider(self, provider):
        """
        Add provider to the list is it is not full
        """
        if len(self.providers) >= self.max_providers:
            raise BufferError("Provider list is full.")
        else:
            self.providers.append(provider)
