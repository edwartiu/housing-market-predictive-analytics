# Developer: Edwar Tiu
# File created: 11/1/23


import unittest
from api_handler import ZillowAPI

class TestZillowAPI(unittest.TestCase):
    
    def test_initial(self):
        zillow = ZillowAPI("testKey")
        self.assertEqual(zillow._apiKey, "testKey")


if __name__ == "__main__":
    unittest.main()
