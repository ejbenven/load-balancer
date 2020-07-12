import unittest
from .context import loadBalancer

class ProviderTest(unittest.TestCase):

    def test_id(self):
        a = loadBalancer.Provider()
        b = loadBalancer.Provider()

        self.assertTrue(a.get() != b.get())

if __name__ == '__main__':
    unittest.main()
