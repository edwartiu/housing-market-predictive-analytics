# Developer: Edwar Tiu
# File created: 11/1/23

class ZillowAPI:
    """
    Instantiate a registered Zillow API.
    The ZillowAPI abstracts calls to Zillow server with simplified
    class methods.

    :param apiKey: The API key that will make calls to Zillow server
    :type string:
    """

    def __init__(self, apiKey):
        self._apiKey = apiKey

    
